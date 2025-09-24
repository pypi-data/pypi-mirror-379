"""
🎪 GitHub API interface for circus tent label management

Handles all GitHub operations including PR fetching, label management,
and circus tent emoji state synchronization.
"""

import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import httpx

# Constants
DEFAULT_GITHUB_ACTOR = "unknown"


@dataclass
class GitHubError(Exception):
    """GitHub API error"""

    message: str
    status_code: Optional[int] = None


class GitHubInterface:
    """GitHub API client for circus tent label operations"""

    def __init__(
        self, token: Optional[str] = None, org: Optional[str] = None, repo: Optional[str] = None
    ):
        self.token = token or self._detect_token()
        self.org = org or os.getenv("GITHUB_ORG", "apache")
        self.repo = repo or os.getenv("GITHUB_REPO", "superset")
        self.base_url = "https://api.github.com"

        if not self.token:
            raise GitHubError("GitHub token required. Set GITHUB_TOKEN environment variable.")

    def _detect_token(self) -> Optional[str]:
        """Detect GitHub token from environment or gh CLI"""
        # 1. Environment variable (GHA style)
        token = os.getenv("GITHUB_TOKEN")
        if token:
            return token

        # 2. GitHub CLI (local development)
        try:
            import subprocess

            result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass  # gh CLI not installed

        return None

    # GitHub Actor Resolution
    @staticmethod
    def get_current_actor() -> str:
        """Get current GitHub actor with consistent fallback across the codebase"""
        return os.getenv("GITHUB_ACTOR", DEFAULT_GITHUB_ACTOR)

    @staticmethod
    def get_actor_debug_info() -> dict:
        """Get debug information about GitHub actor context"""
        raw_actor = os.getenv("GITHUB_ACTOR")  # Could be None/empty
        return {
            "actor": GitHubInterface.get_current_actor(),
            "is_github_actions": os.getenv("GITHUB_ACTIONS") == "true",
            "raw_actor": raw_actor or "none",
        }

    @property
    def headers(self) -> Dict[str, str]:
        """HTTP headers for GitHub API requests"""
        return {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def get_labels(self, pr_number: int) -> List[str]:
        """Get all labels for a PR"""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/issues/{pr_number}/labels"

        with httpx.Client() as client:
            response = client.get(url, headers=self.headers)
            response.raise_for_status()

            labels_data = response.json()
            return [label["name"] for label in labels_data]

    def add_label(self, pr_number: int, label: str) -> None:
        """Add a label to a PR (automatically creates label definition if needed)"""

        # Ensure label definition exists with proper color/description
        self._ensure_label_definition_exists(label)

        url = f"{self.base_url}/repos/{self.org}/{self.repo}/issues/{pr_number}/labels"

        with httpx.Client() as client:
            response = client.post(url, headers=self.headers, json={"labels": [label]})
            response.raise_for_status()

    def _ensure_label_definition_exists(self, label: str) -> None:
        """Ensure label definition exists in repository with proper color/description"""
        from .label_colors import get_label_color, get_label_description

        try:
            color = get_label_color(label)
            description = get_label_description(label)
            self.create_or_update_label(label, color, description)
        except Exception:
            # If label creation fails, continue anyway - label might already exist
            pass

    def remove_label(self, pr_number: int, label: str) -> None:
        """Remove a label from a PR"""
        # URL encode the label name for special characters like emojis
        import urllib.parse

        encoded_label = urllib.parse.quote(label, safe="")
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/issues/{pr_number}/labels/{encoded_label}"

        with httpx.Client() as client:
            response = client.delete(url, headers=self.headers)
            # 404 is OK - label might not exist
            if response.status_code not in (200, 204, 404):
                response.raise_for_status()

    def get_latest_commit_sha(self, pr_number: int) -> str:
        """Get the latest commit SHA for a PR"""
        pr_data = self.get_pr_data(pr_number)
        return str(pr_data["head"]["sha"])

    def get_pr_data(self, pr_number: int) -> Dict[str, Any]:
        """Get full PR data including description"""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/pulls/{pr_number}"

        with httpx.Client() as client:
            response = client.get(url, headers=self.headers)
            response.raise_for_status()
            result: Dict[str, Any] = response.json()
            return result

    def get_circus_labels(self, pr_number: int) -> List[str]:
        """Get only circus tent emoji labels for a PR"""
        all_labels = self.get_labels(pr_number)
        return [label for label in all_labels if label.startswith("🎪 ")]

    def remove_circus_labels(self, pr_number: int) -> None:
        """Remove all circus tent labels from a PR"""
        circus_labels = self.get_circus_labels(pr_number)
        for label in circus_labels:
            self.remove_label(pr_number, label)

    def find_prs_with_shows(self) -> List[int]:
        """Find all PRs that have circus tent labels"""
        # Search for issues with circus tent labels (updated for SHA-first format)
        url = f"{self.base_url}/search/issues"
        # Search for PRs with any circus tent labels
        params = {
            "q": f"repo:{self.org}/{self.repo} is:pr is:open 🎪",
            "per_page": "100",
        }  # Only open PRs - closed PRs should have cleaned up labels

        with httpx.Client() as client:
            response = client.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            issues = response.json()["items"]
            return [issue["number"] for issue in issues]

    def post_comment(self, pr_number: int, body: str) -> None:
        """Post a comment on a PR"""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/issues/{pr_number}/comments"

        with httpx.Client() as client:
            response = client.post(url, headers=self.headers, json={"body": body})
            response.raise_for_status()

    def validate_connection(self) -> bool:
        """Test GitHub API connection"""
        try:
            url = f"{self.base_url}/repos/{self.org}/{self.repo}"
            with httpx.Client() as client:
                response = client.get(url, headers=self.headers)
                response.raise_for_status()
                return True
        except Exception:
            return False

    def get_repository_labels(self) -> List[str]:
        """Get all labels defined in the repository"""
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/labels"

        with httpx.Client() as client:
            response = client.get(url, headers=self.headers, params={"per_page": 100})
            response.raise_for_status()

            labels_data = response.json()
            return [label["name"] for label in labels_data]

    def delete_repository_label(self, label_name: str) -> bool:
        """Delete a label definition from the repository"""
        import urllib.parse

        encoded_label = urllib.parse.quote(label_name, safe="")
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/labels/{encoded_label}"

        with httpx.Client() as client:
            response = client.delete(url, headers=self.headers)
            # 404 is OK - label might not exist
            if response.status_code in (200, 204):
                return True
            elif response.status_code == 404:
                return False  # Label doesn't exist
            else:
                response.raise_for_status()
                return False  # Should never reach here

    def cleanup_sha_labels(self, dry_run: bool = False) -> List[str]:
        """Clean up all circus tent labels with SHA patterns from repository"""
        import re

        all_labels = self.get_repository_labels()
        sha_labels = []

        # Find labels with SHA patterns (7+ hex chars anywhere in label)
        sha_pattern = re.compile(r"^🎪 .*[a-f0-9]{7,}.*$")

        for label in all_labels:
            if sha_pattern.match(label):
                sha_labels.append(label)

        if not dry_run:
            deleted_labels = []
            for label in sha_labels:
                if self.delete_repository_label(label):
                    deleted_labels.append(label)
            return deleted_labels

        return sha_labels

    def find_orphaned_labels(self, dry_run: bool = False) -> List[str]:
        """Find labels that exist in repository but aren't used on any PR"""
        import re

        print("🔍 Scanning repository labels...")

        # 1. Get all repository labels with SHA patterns
        all_repo_labels = self.get_repository_labels()
        sha_pattern = re.compile(r"^🎪 .*[a-f0-9]{7,}.*$")
        sha_repo_labels = {label for label in all_repo_labels if sha_pattern.match(label)}

        print(f"📋 Found {len(sha_repo_labels)} SHA-containing labels in repository")

        # 2. Get all labels actually used on PRs with circus labels
        print("🔍 Scanning PRs with circus labels...")

        # Import here to avoid circular import
        import importlib

        pull_request_module = importlib.import_module("showtime.core.pull_request")
        PullRequest = pull_request_module.PullRequest

        try:
            pr_numbers = PullRequest.find_all_with_environments()
            print(f"📋 Found {len(pr_numbers)} PRs with circus labels")

            used_labels = set()
            for pr_number in pr_numbers:
                pr_labels = self.get_labels(pr_number)
                circus_labels = {label for label in pr_labels if label.startswith("🎪 ")}
                used_labels.update(circus_labels)

            print(f"📋 Found {len(used_labels)} circus labels actually used on PRs")

            # 3. Set difference to find orphaned labels
            orphaned_labels = sha_repo_labels - used_labels

            print(f"🗑️ Found {len(orphaned_labels)} truly orphaned labels")

            # Debug: Show some examples if in dry run
            if dry_run and orphaned_labels:
                print("🔍 Examples of orphaned labels:")
                for label in list(orphaned_labels)[:5]:
                    print(f"  • {label}")
            if dry_run and used_labels:
                print("🔍 Examples of used labels:")
                for label in list(used_labels)[:5]:
                    print(f"  • {label}")

            if not dry_run and orphaned_labels:
                deleted_labels = []
                for label in orphaned_labels:
                    if self.delete_repository_label(label):
                        deleted_labels.append(label)
                return deleted_labels

            return list(orphaned_labels)

        except Exception as e:
            print(f"⚠️ Error during orphan detection: {e}")
            # Fallback to old pattern-based method
            return self.cleanup_sha_labels(dry_run)

    def create_or_update_label(self, name: str, color: str, description: str) -> bool:
        """Create or update a label with color and description"""
        import urllib.parse

        # Check if label exists
        encoded_name = urllib.parse.quote(name, safe="")
        url = f"{self.base_url}/repos/{self.org}/{self.repo}/labels/{encoded_name}"

        label_data = {"name": name, "color": color, "description": description}

        with httpx.Client() as client:
            # Try to update first (if exists)
            response = client.patch(url, headers=self.headers, json=label_data)

            if response.status_code == 200:
                return False  # Updated existing
            elif response.status_code == 404:
                # Label doesn't exist, create it
                create_url = f"{self.base_url}/repos/{self.org}/{self.repo}/labels"
                response = client.post(create_url, headers=self.headers, json=label_data)
                response.raise_for_status()
                return True  # Created new
            else:
                response.raise_for_status()
                return False
