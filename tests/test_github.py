from __future__ import annotations

from typing import TYPE_CHECKING

from oss_maint import github, pythons
from oss_maint.github import public_members

if TYPE_CHECKING:
    import pytest


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
