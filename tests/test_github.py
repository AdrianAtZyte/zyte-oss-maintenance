from __future__ import annotations

import pytest

from oss_maint import github, pythons, sync
from oss_maint.github import has_wiki, public_members


def test_public_members(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(github, "PAGE_SIZE", 2)
    pages = {
        github.PUBLIC_MEMBERS_URL.format("org", 2, 1): [
            {"login": "Alice"},
            {"login": "bob"},
        ],
        github.PUBLIC_MEMBERS_URL.format("org", 2, 2): [{"login": "carol"}],
    }
    monkeypatch.setattr(pythons, "_get_json", pages.__getitem__)
    assert public_members.__wrapped__("org") == {"alice", "bob", "carol"}


@pytest.mark.parametrize(
    ("error", "expected"),
    [
        (None, True),
        ("remote: Repository not found.\nfatal: repository '…' not found", False),
    ],
)
def test_has_wiki(
    monkeypatch: pytest.MonkeyPatch, error: str | None, expected: bool
) -> None:
    def git(*args: str) -> str:
        assert args == ("ls-remote", "https://github.com/org/repo.wiki.git", "HEAD")
        if error:
            raise sync.SyncError(error)
        return ""

    monkeypatch.setattr(sync, "_git", git)
    assert has_wiki.__wrapped__("org/repo") is expected


def test_has_wiki_error(monkeypatch: pytest.MonkeyPatch) -> None:
    def git(*args: str) -> str:
        raise sync.SyncError("fatal: unable to access")

    monkeypatch.setattr(sync, "_git", git)
    with pytest.raises(sync.SyncError):
        has_wiki.__wrapped__("org/repo")
