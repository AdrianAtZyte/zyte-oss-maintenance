"""Checks, one module per group of related checks.

A group module defines a :class:`~oss_maint.core.Group` and adds checks to it
with its ``check`` decorator::

    group = Group("python-versions", "Python versions")


    @group.check("Support for end-of-life Python versions is dropped.")
    def no_eol_python(repo: Repo) -> Result: ...

A check's ID is its function name with underscores replaced by hyphens. Its
statement describes the up-to-date state, and the check passes if it holds.
It returns ``passed()``, ``failed()`` or ``not_applicable()`` from
:mod:`oss_maint.core`; exceptions are reported as check errors.

Informational checks, added with the group's ``info`` decorator, return
whether their statement is true, and are reported as "yes" or "no" rather
than passing or failing. They show facts that other checks depend on, such as
whether a project has docs.

Facts, added with the group's ``fact`` decorator, return values that checks
compare projects against, such as the latest Python version. They are
reported once, at the start of the report.

Groups are reported in the order of :data:`GROUPS`, and checks in the order in
which they are defined.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import replace
from typing import TYPE_CHECKING

from oss_maint.checks import (
    dependencies,
    docs,
    linting,
    packaging,
    python,
    releases,
    testing,
    type_checking,
)

if TYPE_CHECKING:
    from oss_maint.core import Group

GROUPS: list[Group] = [
    python.group,
    packaging.group,
    dependencies.group,
    type_checking.group,
    testing.group,
    linting.group,
    docs.group,
    releases.group,
]

# Group IDs, check IDs and check tags share a namespace, since all can be used
# to select or skip checks.
_tags = {t for g in GROUPS for c in g.checks for t in c.tags}
_ids = Counter(
    [*_tags, *(g.id for g in GROUPS), *(c.id for g in GROUPS for c in g.checks)]
)
if duplicates := sorted(i for i, n in _ids.items() if n > 1):
    raise RuntimeError(f"duplicate group or check IDs: {', '.join(duplicates)}")
ALL_IDS = set(_ids)


def select_groups(ids: list[str]) -> list[Group]:
    """Return copies of :data:`GROUPS` limited to the checks matching *ids*,
    which may be group IDs, check IDs or check tags."""
    if unknown := sorted(set(ids) - ALL_IDS):
        raise ValueError(f"unknown checks: {', '.join(unknown)}")
    groups = []
    for group in GROUPS:
        checks = [
            c
            for c in group.checks
            if group.id in ids or c.id in ids or not c.tags.isdisjoint(ids)
        ]
        if checks:
            groups.append(replace(group, checks=checks))
    return groups
