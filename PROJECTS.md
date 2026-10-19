# Maintenance report by project

Generated on 2026-10-19 with `oss-maint report`. Do not edit by hand. Lists failing checks and notes for each project; see [REPORT.md](REPORT.md) for all results.

## Scrapy and its deps

### scrapy/scrapy

[Repository](https://github.com/scrapy/scrapy) · commit [`c7ec9ea`](https://github.com/scrapy/scrapy/commit/c7ec9ea9136927ae9c37647a677e1fa074d47dc9) · 39/45 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 2.19.0 (2026-09-10) · unreleased-changes: yes

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: packaging, tldextract

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

### scrapy/cssselect

[Repository](https://github.com/scrapy/cssselect) · commit [`ec61e4b`](https://github.com/scrapy/cssselect/commit/ec61e4b5deed6494431f4054bb6161f7b80e4dbf) · 34/43 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.6.0 (2026-10-09) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/formerly

[Repository](https://github.com/scrapy/formerly) · commit [`7a6e30b`](https://github.com/scrapy/formerly/commit/7a6e30b1f9821e90c26e0e81cecfd5f560c19d84) · 36/37 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.1.0 (2026-08-05) · unreleased-changes: yes

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml

### scrapy/itemadapter

[Repository](https://github.com/scrapy/itemadapter) · commit [`01cac64`](https://github.com/scrapy/itemadapter/commit/01cac645712c992acfc5c9dcba754b1ea0bbe11a) · 31/39 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no · latest-release: 0.13.1 (2026-01-08) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/itemloaders

[Repository](https://github.com/scrapy/itemloaders) · commit [`cb6f387`](https://github.com/scrapy/itemloaders/commit/cb6f38739aade299f6c2468b0dfa96812fa5bbb3) · 33/46 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.5.0 (2026-09-29) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/parsel

[Repository](https://github.com/scrapy/parsel) · commit [`4932123`](https://github.com/scrapy/parsel/commit/49321235a2e448c49f23ee068c9cdfc2d35a4317) · 43/48 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.12.1 (2026-09-28) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests-macos.yml, .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in pyproject.toml

### scrapy/protego

[Repository](https://github.com/scrapy/protego) · commit [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) · 32/37 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-09-21) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/comparison.yml, .github/workflows/tests.yml

### scrapy/queuelib

[Repository](https://github.com/scrapy/queuelib) · commit [`2f900bd`](https://github.com/scrapy/queuelib/commit/2f900bdc0bbb18f99c20ca53d3477f5fc27ef30f) · 30/37 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no · latest-release: 1.10.0 (2026-08-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: tox.ini

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

### scrapy/w3lib

[Repository](https://github.com/scrapy/w3lib) · commit [`9ded4ea`](https://github.com/scrapy/w3lib/commit/9ded4ea3137a6db9dc04e32d3186f61007f3cb4d) · 35/44 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 2.5.0 (2026-09-30) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/test.yml
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in pyproject.toml

### scrapy/xtractmime

[Repository](https://github.com/scrapy/xtractmime) · commit [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) · 24/36 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.2.1 (2024-01-16) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`dependabot`](REPORT.md#dependabot): no .github/dependabot.yml

## Scrapy plugins

### scrapy-plugins/scrapy-download-handlers-incubator

[Repository](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) · commit [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) · 34/38 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.5.1 (2026-09-11) · unreleased-changes: yes

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

### scrapy-plugins/scrapy-playwright

[Repository](https://github.com/scrapy-plugins/scrapy-playwright) · commit [`390f452`](https://github.com/scrapy-plugins/scrapy-playwright/commit/390f452b0b30afcfa0f6c714b12f4a083f56b161) · 17/43 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 0.0.48 (2026-07-10) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.9.0, latest is 0.14.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-spider-metadata

[Repository](https://github.com/scrapy-plugins/scrapy-spider-metadata) · commit [`bde680a`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/bde680ab6865e920b06b970417125ace5c03ce71) · 36/47 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-09-26) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/duplicate-url-discarder

[Repository](https://github.com/zytedata/duplicate-url-discarder) · commit [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) · 12/33 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.3.0 (2024-12-30) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### zytedata/duplicate-url-discarder-rules

[Repository](https://github.com/zytedata/duplicate-url-discarder-rules) · commit [`7281048`](https://github.com/zytedata/duplicate-url-discarder-rules/commit/7281048b2cfa0538c0b355e8f91185f27367649d) · 10/30 checks passing

supports-pypy: no · license: MIT License · pylint: no · has-sphinx-docs: no · latest-release: 2024.11.5 (2024-11-05) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in setup.cfg: [flake8]
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

## Scrapy tools

### scrapy/scrapy-lint

[Repository](https://github.com/scrapy/scrapy-lint) · commit [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) · 30/44 checks passing

supports-pypy: no · license: MIT · pylint: yes · has-sphinx-docs: yes · latest-release: 0.1.1 (2026-01-27) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: documentation

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapyrt

[Repository](https://github.com/scrapinghub/scrapyrt) · commit [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) · 24/43 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 0.18.1 (2026-06-29) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.12.5 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Feed exporters

### scrapy-plugins/scrapy-feedexport-warc

[Repository](https://github.com/scrapy-plugins/scrapy-feedexport-warc) · commit [`ad7956f`](https://github.com/scrapy-plugins/scrapy-feedexport-warc/commit/ad7956f4825fa2c4671c1849a8ad7a4eb2cc34d1) · 8/32 checks passing

supports-pypy: no · license: Apache Software License · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.8.4 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/release.yml is not triggered by tag pushes
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/release.yml: job 'release' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-azure-storage

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) · commit [`4f36ff8`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage/commit/4f36ff805239bace39bacc8c1e02cc8c876013b4) · 2/22 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-dropbox

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) · commit [`4e4cca6`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox/commit/4e4cca6f5240d790708219c0344b812eb76a854f) · 1/20 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-google-drive

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) · commit [`ee13d9d`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive/commit/ee13d9dfc0ef378cfa68fba15e33a1df6078677b) · 2/24 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): no license field
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): no [project.urls] table
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: google-api-python-client, google-auth, scrapy
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-google-sheets

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) · commit [`25f2a8c`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets/commit/25f2a8c6079e85823c7e640b17eea2ad5ed8f767) · 1/21 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-onedrive

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) · commit [`9b5fdd6`](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive/commit/9b5fdd62704aa1c666419f3d6ea201ce3f534132) · 1/21 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy-plugins/scrapy-feedexporter-sftp

[Repository](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) · commit [`38c9e5b`](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp/commit/38c9e5b244bfa363de9ede92f7069ae7bcbce469) · 14/34 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 1.1.0 (2025-02-12) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.9.3 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## scrapy-poet and its deps

### scrapinghub/scrapy-poet

[Repository](https://github.com/scrapinghub/scrapy-poet) · commit [`e87c2d0`](https://github.com/scrapinghub/scrapy-poet/commit/e87c2d01f60855652bd756c918cf11c93256d283) · 31/45 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.27.2 (2026-04-28) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt
- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.15.6 (0.15.11 or later expected)
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/scrapy-unreleased.yml, .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/andi

[Repository](https://github.com/scrapinghub/andi) · commit [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) · 29/35 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.9.0 (2026-09-17) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

### scrapinghub/web-poet

[Repository](https://github.com/scrapinghub/web-poet) · commit [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) · 30/45 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.24.1 (2026-04-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt
- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests-ubuntu.yml, .github/workflows/tests-windows.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/url-matcher

[Repository](https://github.com/zytedata/url-matcher) · commit [`f3805d7`](https://github.com/zytedata/url-matcher/commit/f3805d78f101a0594cdfe1fcbf9b7789a0680aae) · 40/45 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-02-14) · unreleased-changes: yes

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0
- ❌ [`changelog-date`](REPORT.md#changelog-date): no file replacement of (unreleased) with {now:%Y-%m-%d}

### scrapy/frostwork

[Repository](https://github.com/scrapy/frostwork) · commit [`eaf5cff`](https://github.com/scrapy/frostwork/commit/eaf5cffc3727568d2651273502c2852b660e3738) · 18/30 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.6 (2026-09-23) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

## Zyte API

### scrapy-plugins/scrapy-zyte-api

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-api) · commit [`681d145`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/681d14500b804f291a09306cc2cb9378f0203217) · 38/46 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.36.0 (2026-08-20) · unreleased-changes: yes

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.14.0
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/python-zyte-api

[Repository](https://github.com/zytedata/python-zyte-api) · commit [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) · 31/44 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 0.11.0 (2026-07-23) · unreleased-changes: yes

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-zyte-smartproxy

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) · commit [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) · 13/36 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 2.4.1 (2025-03-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .bandit.yml, .flake8, .isort.cfg; tool sections in setup.cfg: [mypy], [mypy-pytest.*], [mypy-scrapy.*], [mypy-twisted.*], [mypy-w3lib.*]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/zyte-common-items

[Repository](https://github.com/zytedata/zyte-common-items) · commit [`297cb86`](https://github.com/zytedata/zyte-common-items/commit/297cb86af88b26106899eb231d50c7b96d164f78) · 35/45 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.31.0 (2026-10-16) · unreleased-changes: no

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst

## Scrapy Cloud

### scrapinghub/python-scrapinghub

[Repository](https://github.com/scrapinghub/python-scrapinghub) · commit [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) · 13/38 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 2.9.0 (2026-08-12) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: pytest.ini
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.7.1, latest is 0.14.0

### scrapinghub/shub

[Repository](https://github.com/scrapinghub/shub) · commit [`4facd31`](https://github.com/scrapinghub/shub/commit/4facd31c84dfc1ef78fac43710a592a87753fcc5) · 20/42 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 2.18.1 (2026-07-08) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docker, importlib-metadata, packaging, PyYAML, requests, retrying, setuptools, toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.14.0

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapinghub-entrypoint-scrapy

[Repository](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) · commit [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) · 6/26 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.18.1 (2026-01-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/shub-workflow

[Repository](https://github.com/scrapinghub/shub-workflow) · commit [`237107e`](https://github.com/scrapinghub/shub-workflow/commit/237107e06250247a00bfd04368af3b0ed26468b6) · 3/24 checks passing

supports-pypy: no · license: Apache Software License · pylint: no · has-sphinx-docs: no · latest-release: 1.14.43 (2026-10-13) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in setup.cfg: [flake8], [tool:pytest], [coverage:run]
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/python-app.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/scrapy-frontera

[Repository](https://github.com/scrapinghub/scrapy-frontera) · commit [`56ea2e1`](https://github.com/scrapinghub/scrapy-frontera/commit/56ea2e1ef39a174eac61da2edcdb21d1f1ecf5e5) · 9/31 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.3.0 (2025-06-06) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01)
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no Python version classifiers

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.9.4 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/tests.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/frontera

[Repository](https://github.com/scrapinghub/frontera) · commit [`c94beae`](https://github.com/scrapinghub/frontera/commit/c94beae2f438492139d24759729d0201779ccf1c) · 3/24 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.8.1 (2019-04-05) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc; tool sections in tox.ini: [flake8], [pytest]
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/hcf-backend

[Repository](https://github.com/scrapinghub/hcf-backend) · commit [`bbdc50c`](https://github.com/scrapinghub/hcf-backend/commit/bbdc50cd1d250742234aacc2d5da10c4fe4d9508) · 9/29 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.6.1 (2025-10-31) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.12 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Data extraction

### zytedata/zyte-parsers

[Repository](https://github.com/zytedata/zyte-parsers) · commit [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) · 31/43 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-10-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

### zytedata/clear-html

[Repository](https://github.com/zytedata/clear-html) · commit [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) · 30/37 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.5.0 (2025-10-24) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

### zytedata/html-text

[Repository](https://github.com/zytedata/html-text) · commit [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) · 20/36 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no · latest-release: 0.7.1 (2025-10-06) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: lxml, lxml-html-clean
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/price-parser

[Repository](https://github.com/scrapinghub/price-parser) · commit [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) · 23/38 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.5.1 (2026-03-19) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/dateparser

[Repository](https://github.com/scrapinghub/dateparser) · commit [`07b40b2`](https://github.com/scrapinghub/dateparser/commit/07b40b2f01773d830321538ac9d2d6219edbe10e) · 21/42 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 1.4.3 (2026-09-03) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, pytest.ini
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, documentation

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/cifuzz.yml, .github/workflows/main.yml
- ❌ [`pr-guard-trusted-users`](REPORT.md#pr-guard-trusted-users): public members of trusted orgs: kishan3
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases

### scrapinghub/extruct

[Repository](https://github.com/scrapinghub/extruct) · commit [`d24f541`](https://github.com/scrapinghub/extruct/commit/d24f5414fd32c874989492ebd04cb1deb6d7d04e) · 8/28 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.18.0 (2024-11-08) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .isort.cfg, pytest.ini, requirements-dev.txt
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/python-package.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in setup.cfg

### scrapinghub/number-parser

[Repository](https://github.com/scrapinghub/number-parser) · commit [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) · 8/29 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.3.2 (2023-03-28) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc
- ❌ [`hatchling`](REPORT.md#hatchling): no build-backend in pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

## Forms

### scrapy/form2request

[Repository](https://github.com/scrapy/form2request) · commit [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) · 31/43 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-07-15) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

### scrapinghub/Formasaurus

[Repository](https://github.com/scrapinghub/Formasaurus) · commit [`4bb46a9`](https://github.com/scrapinghub/Formasaurus/commit/4bb46a95c7851622bb63ca7459d4d6d2587297ab) · 10/34 checks passing

supports-pypy: no · license: MIT License · pylint: no · has-sphinx-docs: yes · latest-release: 0.10.0 (2024-11-07) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.13, 3.14, 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8; tool sections in setup.cfg: [isort]
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`readthedocs`](REPORT.md#readthedocs): the README does not link to Formasaurus.readthedocs.io or Formasaurus.readthedocs.org
- ❌ [`changelog-date`](REPORT.md#changelog-date): no file replacement of (unreleased) with {now:%Y-%m-%d}

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/sklearn-crfsuite

[Repository](https://github.com/scrapinghub/sklearn-crfsuite) · commit [`e18a02a`](https://github.com/scrapinghub/sklearn-crfsuite/commit/e18a02ae11b61f703c0ec460c44cfdd90db00591) · 8/32 checks passing

supports-pypy: no · license: MIT License · pylint: no · has-sphinx-docs: yes · latest-release: 0.5.0 (2024-06-18) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [`pre-commit-hooks`](REPORT.md#pre-commit-hooks): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/test.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`readthedocs`](REPORT.md#readthedocs): no .readthedocs.yml
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### scrapinghub/python-crfsuite

[Repository](https://github.com/scrapinghub/python-crfsuite) · commit [`c2eee32`](https://github.com/scrapinghub/python-crfsuite/commit/c2eee3267750c585d3ef5eebaf632d3ee7855249) · 5/32 checks passing

supports-pypy: no · license: MIT License · pylint: no · has-sphinx-docs: yes · latest-release: 0.9.12 (2025-12-23) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .flake8
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues, changelog, documentation
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/build_and_upload.yml, .github/workflows/tests.yml
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): no .pre-commit-config.yaml
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): no .pre-commit-config.yaml

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`readthedocs`](REPORT.md#readthedocs): no .readthedocs.yml; the README does not link to python-crfsuite.readthedocs.io or python-crfsuite.readthedocs.org

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/build_and_upload.yml: job 'upload_to_pypi' has no environment; .github/workflows/build_and_upload.yml uses an API token; .github/workflows/build_and_upload.yml lacks the id-token: write permission
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/build_and_upload.yml is triggered by GitHub releases

## Monitoring

### scrapinghub/spidermon

[Repository](https://github.com/scrapinghub/spidermon) · commit [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) · 27/42 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 1.27.0 (2026-08-10) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`scrapy-master`](REPORT.md#scrapy-master): no CI workflow or tox environment installs Scrapy master

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [`docs-stable-links`](REPORT.md#docs-stable-links): links to latest in README.rst; latest in pyproject.toml

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/zyte-spidermon

[Repository](https://github.com/scrapy-plugins/zyte-spidermon) · commit [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) · 2/23 checks passing

supports-pypy: no · license: no · pylint: no · has-sphinx-docs: no · latest-release: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python is not declared
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): no [project] table in pyproject.toml; setup.py exists
- ❌ [`hatchling`](REPORT.md#hatchling): no pyproject.toml
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/main.yml

**Documentation**

- ❌ [`changelog`](REPORT.md#changelog): no changelog file

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

## AI agents

### scrapy/scrapy-agent-plugin

[Repository](https://github.com/scrapy/scrapy-agent-plugin) · commit [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) · 3/3 checks passing

has-sphinx-docs: no

All applicable checks pass.

### scrapy/scrapy-mcp-official

[Repository](https://github.com/scrapy/scrapy-mcp-official) · commit [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) · 32/37 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.2 (2026-09-07) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-status`](REPORT.md#codecov-status): no Codecov config
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml

### zytedata/agent-exam

[Repository](https://github.com/zytedata/agent-exam) · commit [`c88fec1`](https://github.com/zytedata/agent-exam/commit/c88fec170ff9683dad9d769601206088fdbaeb7d) · 26/42 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2026-08-17) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: issues

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`dependabot`](REPORT.md#dependabot): no .github/dependabot.yml
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.10, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/claude-measure-usage

[Repository](https://github.com/zytedata/claude-measure-usage) · commit [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) · 18/34 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.1 (2026-09-14) · unreleased-changes: yes

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: docs, tox.ini
- ❌ [`project-urls`](REPORT.md#project-urls): missing URLs: changelog
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/checks.yml, .github/workflows/tests.yml

### zytedata/harness-run

[Repository](https://github.com/zytedata/harness-run) · commit [`4028849`](https://github.com/zytedata/harness-run/commit/4028849faf48ac448b1634140cfe3a9cac8f2749) · 11/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.4.0 (2026-09-23) · unreleased-changes: yes

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`twine-check`](REPORT.md#twine-check): twine check runs in a workflow, not in tox

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapy/sphinx-llm-friendly

[Repository](https://github.com/scrapy/sphinx-llm-friendly) · commit [`2f5b77c`](https://github.com/scrapy/sphinx-llm-friendly/commit/2f5b77c315d5230429761063b475c7c1b015ca79) · 23/35 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-10-03) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): not included: tox.ini
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docutils, tabulate

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.11 or later expected)

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Maintenance

### scrapy/sphinx-scrapy

[Repository](https://github.com/scrapy/sphinx-scrapy) · commit [`9231605`](https://github.com/scrapy/sphinx-scrapy/commit/9231605ac5f164edf053998ed9ba4b61b385f691) · 20/35 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.14.0 (2026-10-14) · unreleased-changes: no

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`sdist-contents`](REPORT.md#sdist-contents): no include in [tool.hatch.build.targets.sdist]
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.11 or later expected)

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/unattended-pr-guard

[Repository](https://github.com/scrapy/unattended-pr-guard) · commit [`1e3c311`](https://github.com/scrapy/unattended-pr-guard/commit/1e3c31134253813934af43f3505d4492eee26c2a) · 9/11 checks passing

has-sphinx-docs: no

**Linting**

- ❌ [`pre-commit-tox`](REPORT.md#pre-commit-tox): no tox environment runs pre-commit run --all-files
- ❌ [`workflow-concurrency`](REPORT.md#workflow-concurrency): no cancel-in-progress: .github/workflows/ci.yml

### zytedata/zyte-oss-maintenance

[Repository](https://github.com/zytedata/zyte-oss-maintenance) · commit [`1bc82c6`](https://github.com/zytedata/zyte-oss-maintenance/commit/1bc82c664c1dc1bf7d9657bac088cccd34350c0c) · 15/21 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier

**Typing**

- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov`](REPORT.md#codecov): no codecov/codecov-action step for coverage
- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error
