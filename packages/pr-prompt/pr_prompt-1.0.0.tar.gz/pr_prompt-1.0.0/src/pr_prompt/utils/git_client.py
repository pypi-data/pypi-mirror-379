from pathlib import Path
from typing import Optional

from git import Blob, Diff, DiffIndex, Repo


class GitClient:
    def __init__(
        self,
        base_ref: Optional[str] = None,
        head_ref: Optional[str] = None,
        *,
        repo_path: Optional[str] = None,
        remote: str = "origin",
    ):
        """Initialize GitClient with a repository path."""
        self.repo = Repo(repo_path)
        self.remote = self.repo.remote(remote)

        self.base_ref = self._strip_remote(base_ref) or self.get_default_branch()
        self.head_ref = self._strip_remote(head_ref) or self.repo.active_branch.name

        self.base_commit = self.repo.commit(f"{self.remote.name}/{self.base_ref}")
        self.head_commit = self.repo.commit(self.head_ref)

    def _strip_remote(self, ref: Optional[str]) -> Optional[str]:
        """Strip remote name from ref if present."""
        if not ref:
            return None
        return ref.removeprefix(f"{self.remote.name}/")

    def get_default_branch(self) -> str:
        """Get the default branch name from the remote."""
        try:
            remote_head = self.remote.refs.HEAD
            return remote_head.reference.remote_head  # type: ignore[attr-defined]  # noqa: TRY300
        except (AttributeError, IndexError) as err:
            # Fallback to common default branch names
            for default_name in ["main", "master"]:
                if f"{self.remote.name}/{default_name}" in [
                    ref.name for ref in self.remote.refs
                ]:
                    return default_name
            msg = "Could not determine default branch. Please specify base_ref."
            raise InferBaseBranchError(msg) from err

    def fetch_base_branch(self) -> None:
        self.fetch_branch(self.base_ref)

    def fetch_branch(self, branch: str) -> None:
        """Fetch a specific branch from a remote."""
        if branch:
            self.remote.fetch(branch)

    def get_commit_messages(self) -> list[str]:
        """Get list of commit messages between two refs."""
        commits = self.repo.iter_commits(f"{self.base_commit}..{self.head_commit}")
        return [
            ". ".join(commit.message.strip().split("\n"))
            for commit in commits
            if isinstance(commit.message, str)
        ]

    def get_repo_name(self) -> str:
        return Path(self.repo.working_dir).name

    def list_files(self, ref: str) -> list[str]:
        """List all files in the repository at a specific ref."""
        commit = self.repo.commit(ref)
        return [
            str(item.path) for item in commit.tree.traverse() if isinstance(item, Blob)
        ]

    def get_file_content(self, ref: str, file_path: str) -> str:
        commit = self.repo.commit(ref)
        blob = commit.tree[file_path]
        blob_data: bytes = blob.data_stream.read()
        return blob_data.decode("utf-8", errors="replace").strip()

    def get_diff_index(self, context_lines: int = 999999) -> DiffIndex[Diff]:
        return self.base_commit.diff(
            self.head_commit,
            create_patch=True,
            unified=context_lines,
            diff_algorithm="histogram",
            find_renames=50,
            function_context=True,
        )


class InferBaseBranchError(Exception):
    """Raised when unable to infer the default branch from the remote."""
