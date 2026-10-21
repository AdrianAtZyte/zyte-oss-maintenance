from __future__ import annotations

from typing import TYPE_CHECKING

from oss_maint import github
from oss_maint.runner import _prefetch_wikis

if TYPE_CHECKING:
    import pytest


def test_prefetch_wikis(monkeypatch: pytest.MonkeyPatch) -> None:
    checked = []

    def has_wiki(name: str) -> bool:
        checked.append(name)
        if name == "org/error":
            raise RuntimeError
        return True

    monkeypatch.setattr(github, "has_wiki", has_wiki)
    _prefetch_wikis(["org/a", "org/error", "org/b"])
    assert sorted(checked) == ["org/a", "org/b", "org/error"]
