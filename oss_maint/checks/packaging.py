from __future__ import annotations

import configparser
import re

from packaging.licenses import InvalidLicenseExpression, canonicalize_license_expression

from oss_maint.core import Group, Repo, Result, failed, not_applicable, passed

group = Group("packaging", "Packaging", frozenset({"python"}))

NO_PROJECT_TABLE = "No [project] table in pyproject.toml."
# Prefixes of setup.cfg sections with setuptools configuration, as opposed to
# configuration of other tools, e.g. [flake8].
SETUPTOOLS_SECTION_PREFIXES = (
    "aliases",
    "bdist",
    "build",
    "easy_install",
    "egg_info",
    "install",
    "metadata",
    "options",
    "register",
    "sdist",
    "upload",
    "wheel",
)


@group.check(
    "Package metadata is in the [project] table of pyproject.toml, with no "
    "setup.py and no setuptools configuration in setup.cfg."
)
def pyproject_metadata(repo: Repo) -> Result:
    problems = []
    if not repo.project:
        problems.append("no [project] table in pyproject.toml")
    if repo.exists("setup.py"):
        problems.append("setup.py exists")
    setup_cfg = configparser.ConfigParser(interpolation=None)
    setup_cfg.read_string(repo.read_text("setup.cfg") or "")
    if sections := [
        f"[{s}]"
        for s in setup_cfg.sections()
        if s.startswith(SETUPTOOLS_SECTION_PREFIXES)
    ]:
        problems.append(f"setup.cfg has setuptools sections: {', '.join(sections)}")
    return failed("; ".join(problems)) if problems else passed()


# Configuration files that pyproject.toml replaces, or of tools that ruff
# replaces.
LEGACY_FILES = (
    ".bandit",
    ".bandit.yml",
    ".coveragerc",
    ".flake8",
    ".isort.cfg",
    ".mypy.ini",
    ".pylintrc",
    "mypy.ini",
    "pylintrc",
    "pytest.ini",
    "requirements-dev.txt",
)
# Sections of setup.cfg or tox.ini with tool configuration.
TOOL_SECTION_RE = re.compile(
    r"(tool:)?pytest|flake8|isort|mypy(-.+)?|coverage:.+|pycodestyle|pydocstyle"
    r"|pylint(\..+)?|bandit"
)


@group.check(
    "There are no legacy configuration files, e.g. .coveragerc, pytest.ini, "
    ".flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or "
    "tox.ini."
)
def no_legacy_config(repo: Repo) -> Result:
    problems = []
    if files := [f for f in LEGACY_FILES if repo.exists(f)]:
        problems.append(f"legacy files: {', '.join(files)}")
    backend = (repo.pyproject or {}).get("build-system", {}).get("build-backend")
    if backend and not backend.startswith("setuptools") and repo.exists("MANIFEST.in"):
        problems.append(f"MANIFEST.in, which {backend} ignores")
    for path in ("setup.cfg", "tox.ini"):
        config = configparser.ConfigParser(interpolation=None, strict=False)
        config.read_string(repo.read_text(path) or "")
        if sections := [
            f"[{s}]" for s in config.sections() if TOOL_SECTION_RE.fullmatch(s)
        ]:
            problems.append(f"tool sections in {path}: {', '.join(sections)}")
    return failed("; ".join(problems)) if problems else passed()


@group.info(
    "The license: the license field of package metadata, or else the license "
    "classifiers."
)
def license_(repo: Repo) -> str | None:
    if isinstance(value := repo.project.get("license"), str):
        return value
    if classifiers := [
        c.removeprefix("License :: ").removeprefix("OSI Approved :: ")
        for c in repo.classifiers
        if c.startswith("License ::")
    ]:
        return ", ".join(classifiers)
    if isinstance(value, dict) and "text" in value:
        return value["text"]
    if m := re.search(
        r"license\s*=\s*[\"']([^\"']+)", repo.read_text("setup.py") or ""
    ):
        return m.group(1)
    return None


@group.check(
    "The license is declared as an SPDX expression (PEP 639), without license "
    "classifiers."
)
def pep639_license(repo: Repo) -> Result:
    if not repo.project:
        return not_applicable(NO_PROJECT_TABLE)
    problems = []
    value = repo.project.get("license")
    if value is None:
        if "license" not in repo.project.get("dynamic", []):
            problems.append("no license field")
    elif not isinstance(value, str):
        problems.append("license is a table, not an SPDX expression")
    else:
        try:
            canonicalize_license_expression(value)
        except InvalidLicenseExpression:
            problems.append(f"license {value!r} is not a valid SPDX expression")
    if classifiers := [c for c in repo.classifiers if c.startswith("License ::")]:
        problems.append(f"has license classifiers: {', '.join(classifiers)}")
    return failed("; ".join(problems)) if problems else passed()


@group.check("The build backend is hatchling.")
def hatchling(repo: Repo) -> Result:
    if repo.pyproject is None:
        return failed("no pyproject.toml")
    backend = repo.pyproject.get("build-system", {}).get("build-backend")
    if backend is None:
        return failed("no build-backend in pyproject.toml")
    if backend != "hatchling.build":
        return failed(f"build backend is {backend}")
    return passed()


# Paths that the sdist must include if they exist, to run the tests and build
# the docs from it.
SDIST_REQUIRED = ("tests", "docs", "tox.ini", "tox.toml")


def _covers(patterns: list[str], path: str) -> bool:
    """Whether hatch build *patterns*, all root paths ("/tests") or
    directories ("tests/**"), cover the top-level *path*."""
    roots = (pattern.removesuffix("/**").strip("/") for pattern in patterns)
    return any(path == root or path.startswith(f"{root}/") for root in roots)


@group.check(
    "The sdist includes only listed files, which include the tests, the docs and "
    "the tox configuration.",
    tags={"released"},
)
def sdist_contents(repo: Repo) -> Result:
    pyproject = repo.pyproject or {}
    if pyproject.get("build-system", {}).get("build-backend") != "hatchling.build":
        return not_applicable("The build backend is not hatchling.")
    sdist = (
        pyproject.get("tool", {})
        .get("hatch", {})
        .get("build", {})
        .get("targets", {})
        .get("sdist", {})
    )
    include = [*sdist.get("include", []), *sdist.get("only-include", [])]
    if not include:
        return failed("no include in [tool.hatch.build.targets.sdist]")
    exclude = sdist.get("exclude", [])
    if missing := [
        path
        for path in SDIST_REQUIRED
        if repo.exists(path) and (not _covers(include, path) or _covers(exclude, path))
    ]:
        return failed(f"not included: {', '.join(missing)}")
    return passed()


# Labels of [project.urls] that PyPI recognizes, normalized as in PEP 753, by
# the kind of link they are.
URL_LABELS = {
    "source": {"source", "repository", "sourcecode", "github"},
    "issues": {"issues", "bugs", "issue", "tracker", "issuetracker", "bugtracker"},
    "changelog": {"changelog", "changes", "whatsnew", "history", "releasenotes"},
    "documentation": {"documentation", "docs"},
}


def _normalize_label(label: str) -> str:
    return "".join(c for c in label.lower() if c.isalnum())


@group.check(
    "[project.urls] links to the source, the issue tracker, the changelog and, if "
    "there are Sphinx docs, the documentation, with labels that PyPI recognizes.",
    tags={"released"},
)
def project_urls(repo: Repo) -> Result:
    if not repo.project:
        return not_applicable(NO_PROJECT_TABLE)
    if "urls" in repo.project.get("dynamic", []):
        return passed("[project.urls] is dynamic")
    urls = repo.project.get("urls") or {}
    if not urls:
        return failed("no [project.urls] table")
    labels = {_normalize_label(label) for label in urls}
    # A homepage that is the repository is the source.
    if repo.url in (str(url).rstrip("/").removesuffix(".git") for url in urls.values()):
        labels.add("source")
    kinds = [k for k in URL_LABELS if k != "documentation" or repo.has_sphinx_docs]
    if missing := [k for k in kinds if not labels & URL_LABELS[k]]:
        return failed(f"missing URLs: {', '.join(missing)}")
    return passed()


@group.check(
    "`twine check` validates the built distributions in tox.", tags={"released"}
)
def twine_check(repo: Repo) -> Result:
    if any("twine check" in s for s in repo.tox_strings):
        return passed()
    if any("twine check" in s for s in repo.workflow_strings):
        return failed("twine check runs in a workflow, not in tox")
    return failed("no twine check in tox config")
