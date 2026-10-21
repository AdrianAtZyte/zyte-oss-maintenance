from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from contextlib import suppress
from dataclasses import dataclass
from typing import TYPE_CHECKING

from oss_maint import github
from oss_maint.core import Repo, Result, Status, not_applicable
from oss_maint.sync import sync_repos

if TYPE_CHECKING:
    from pathlib import Path

    from oss_maint.core import Group


@dataclass(frozen=True)
class ProjectResults:
    name: str
    #: Checked commit, None if the checkout could not be synced.
    sha: str | None
    #: By check ID.
    results: dict[str, Result]

    @property
    def url(self) -> str:
        return f"https://github.com/{self.name}"


def run_checks(
    repos: list[str],
    groups: list[Group],
    skip: dict[str, dict[str, str]],
    cache_dir: Path,
    *,
    sync: bool,
) -> list[ProjectResults]:
    """Return results for *repos*. *skip* maps repos to {check or group ID:
    reason} for checks that do not apply to them."""
    checks = [(g, c) for g in groups for c in g.checks]
    errors = sync_repos(repos, cache_dir) if sync else {}
    if any(c.id == "no-wiki" for _, c in checks):
        _prefetch_wikis(repos)
    results = []
    for name in repos:
        path = cache_dir / name
        if name not in errors and not (path / ".git").is_dir():
            errors[name] = "not synced yet"
        if name in errors:
            error = Result(Status.ERROR, f"sync failed: {errors[name]}")
            results.append(ProjectResults(name, None, {c.id: error for _, c in checks}))
            continue
        repo = Repo(name, path)
        project_skip = skip.get(name, {})
        project_results = {}
        for group, check in checks:
            reason = project_skip.get(check.id, project_skip.get(group.id))
            for tag in sorted(check.tags):
                reason = reason or project_skip.get(tag)
            project_results[check.id] = (
                not_applicable(reason) if reason else check.run(repo)
            )
        results.append(ProjectResults(name, repo.sha, project_results))
    return results


def _prefetch_wikis(repos: list[str], jobs: int = 8) -> None:
    """Fill the :func:`github.has_wiki` cache for *repos* in parallel."""

    def prefetch(name: str) -> None:
        # Errors are not cached, so the check gets them again and reports them.
        with suppress(Exception):
            github.has_wiki(name)

    with ThreadPoolExecutor(jobs) as executor:
        list(executor.map(prefetch, repos))
