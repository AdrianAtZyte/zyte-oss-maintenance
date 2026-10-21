from __future__ import annotations

from functools import cache
from itertools import count

from oss_maint import pythons, sync

PUBLIC_MEMBERS_URL = "https://api.github.com/orgs/{}/public_members?per_page={}&page={}"
PAGE_SIZE = 100


@cache
def public_members(org: str) -> frozenset[str]:
    """Lowercase logins of the public members of the *org* GitHub
    organization."""
    members: set[str] = set()
    for page in count(1):
        batch = pythons._get_json(PUBLIC_MEMBERS_URL.format(org, PAGE_SIZE, page))
        members.update(member["login"].lower() for member in batch)
        if len(batch) < PAGE_SIZE:
            return frozenset(members)
    raise AssertionError


@cache
def has_wiki(repo: str) -> bool:
    """Whether the *repo* GitHub repository has a wiki with pages."""
    try:
        sync._git("ls-remote", f"https://github.com/{repo}.wiki.git", "HEAD")
    except sync.SyncError as e:
        # Also the error when the wiki is enabled but has no pages.
        if "Repository not found" in str(e):
            return False
        raise
    return True
