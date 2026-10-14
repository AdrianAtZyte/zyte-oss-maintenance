# Maintenance report by project

Generated on 2026-10-14 with `oss-maint report`. Do not edit by hand. Lists failing checks and notes for each project; see [REPORT.md](REPORT.md) for all results.

## Scrapy and its deps

### scrapy/scrapy

[Repository](https://github.com/scrapy/scrapy) · commit [`cc4238c`](https://github.com/scrapy/scrapy/commit/cc4238c3a27a788e655caff354f0f8112b18804b) · 33/38 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 2.19.0 (2026-09-10)

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: packaging, tldextract

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

### scrapy/cssselect

[Repository](https://github.com/scrapy/cssselect) · commit [`805705c`](https://github.com/scrapy/cssselect/commit/805705c5a204721d3c486250377a756bd6fa54a5) · 28/34 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.6.0 (2026-10-09)

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/formerly

[Repository](https://github.com/scrapy/formerly) · commit [`7a6e30b`](https://github.com/scrapy/formerly/commit/7a6e30b1f9821e90c26e0e81cecfd5f560c19d84) · 30/30 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.1.0 (2026-08-05)

All applicable checks pass.

### scrapy/itemadapter

[Repository](https://github.com/scrapy/itemadapter) · commit [`fc9b3e9`](https://github.com/scrapy/itemadapter/commit/fc9b3e9919a458f6a135464304b39be6b4b9d2c4) · 26/31 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no · latest-release: 0.13.1 (2026-01-08)

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/itemloaders

[Repository](https://github.com/scrapy/itemloaders) · commit [`f3e6800`](https://github.com/scrapy/itemloaders/commit/f3e680016d0fd49f24a656f440938ec14c0cd9db) · 25/36 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.5.0 (2026-09-29)

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

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/parsel

[Repository](https://github.com/scrapy/parsel) · commit [`893eb22`](https://github.com/scrapy/parsel/commit/893eb22ffbb58c12e7ab470fab2e9a004246f85e) · 35/38 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 1.12.1 (2026-09-28)

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

### scrapy/protego

[Repository](https://github.com/scrapy/protego) · commit [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) · 26/30 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-09-21)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### scrapy/queuelib

[Repository](https://github.com/scrapy/queuelib) · commit [`885ef61`](https://github.com/scrapy/queuelib/commit/885ef61c6ad9b61682329074f539cbb8c262a580) · 26/30 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no · latest-release: 1.10.0 (2026-08-24)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### scrapy/w3lib

[Repository](https://github.com/scrapy/w3lib) · commit [`cc62486`](https://github.com/scrapy/w3lib/commit/cc624868ea9e41af55d226e8c084bcc722fd6817) · 28/34 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 2.5.0 (2026-09-30)

**Python versions**

- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/sphinx-scrapy

[Repository](https://github.com/scrapy/sphinx-scrapy) · commit [`9231605`](https://github.com/scrapy/sphinx-scrapy/commit/9231605ac5f164edf053998ed9ba4b61b385f691) · 16/29 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.14.0 (2026-10-14)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

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

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.11 or later expected)

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/sphinx-llm-friendly

[Repository](https://github.com/scrapy/sphinx-llm-friendly) · commit [`2f5b77c`](https://github.com/scrapy/sphinx-llm-friendly/commit/2f5b77c315d5230429761063b475c7c1b015ca79) · 19/29 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no · latest-release: 0.7.0 (2026-10-03)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Packaging**

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

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.13 (0.15.11 or later expected)

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## scrapy-poet and its deps

### scrapinghub/scrapy-poet

[Repository](https://github.com/scrapinghub/scrapy-poet) · commit [`e87c2d0`](https://github.com/scrapinghub/scrapy-poet/commit/e87c2d01f60855652bd756c918cf11c93256d283) · 23/35 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.27.2 (2026-04-28)

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
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.15.6 (0.15.11 or later expected)
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/andi

[Repository](https://github.com/scrapinghub/andi) · commit [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) · 25/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.9.0 (2026-09-17)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### scrapinghub/web-poet

[Repository](https://github.com/scrapinghub/web-poet) · commit [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) · 24/36 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.24.1 (2026-04-28)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### zytedata/url-matcher

[Repository](https://github.com/zytedata/url-matcher) · commit [`f3805d7`](https://github.com/zytedata/url-matcher/commit/f3805d78f101a0594cdfe1fcbf9b7789a0680aae) · 33/36 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-02-14)

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

## Zyte API

### scrapy-plugins/scrapy-zyte-api

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-api) · commit [`681d145`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/681d14500b804f291a09306cc2cb9378f0203217) · 31/36 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.36.0 (2026-08-20)

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.12, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/python-zyte-api

[Repository](https://github.com/zytedata/python-zyte-api) · commit [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) · 25/35 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 0.11.0 (2026-07-23)

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.13.0, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-zyte-smartproxy

[Repository](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) · commit [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) · 8/27 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 2.4.1 (2025-03-24)

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/zyte-common-items

[Repository](https://github.com/zytedata/zyte-common-items) · commit [`f15bcc5`](https://github.com/zytedata/zyte-common-items/commit/f15bcc5008f6d24ce725ab340f0160ec93c6c381) · 29/36 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 0.30.0 (2026-10-14)

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: requirements-dev.txt

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

### zytedata/zyte-parsers

[Repository](https://github.com/zytedata/zyte-parsers) · commit [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) · 25/34 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.6.0 (2025-10-24)

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

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### zytedata/clear-html

[Repository](https://github.com/zytedata/clear-html) · commit [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) · 25/30 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.5.0 (2025-10-24)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### zytedata/html-text

[Repository](https://github.com/zytedata/html-text) · commit [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) · 16/29 checks passing

supports-pypy: no · license: MIT · pylint: no · has-sphinx-docs: no · latest-release: 0.7.1 (2025-10-06)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: lxml, lxml-html-clean
- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapinghub/price-parser

[Repository](https://github.com/scrapinghub/price-parser) · commit [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) · 18/30 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.5.1 (2026-03-19)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`min-deps-env`](REPORT.md#min-deps-env): no tox environment for minimum dependency versions

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Scrapy Cloud

### scrapinghub/python-scrapinghub

[Repository](https://github.com/scrapinghub/python-scrapinghub) · commit [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) · 9/30 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 2.9.0 (2026-08-12)

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.7.1, latest is 0.14.0

### scrapinghub/shub

[Repository](https://github.com/scrapinghub/shub) · commit [`80a4cad`](https://github.com/scrapinghub/shub/commit/80a4cad661f2a669739c8c3805fd33c67e62674e) · 10/31 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 2.18.1 (2026-07-08)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in setup.cfg: [flake8]
- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Dependencies**

- ❌ [`dependency-lower-bounds`](REPORT.md#dependency-lower-bounds): no lower bound: click, docker, importlib-metadata, packaging, pip, PyYAML, requests, retrying, setuptools, toml

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy`](REPORT.md#mypy): mypy not found

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [`pre-commit-in-ci`](REPORT.md#pre-commit-in-ci): not run in CI workflows or tox
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.4, latest is 0.14.0

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/scrapinghub-entrypoint-scrapy

[Repository](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) · commit [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) · 4/21 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.18.1 (2026-01-28)

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

## Others

### scrapy/form2request

[Repository](https://github.com/scrapy/form2request) · commit [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) · 26/34 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-07-15)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

### scrapy/frostwork

[Repository](https://github.com/scrapy/frostwork) · commit [`eaf5cff`](https://github.com/scrapy/frostwork/commit/eaf5cffc3727568d2651273502c2852b660e3738) · 16/25 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.6 (2026-09-23)

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

### scrapy/scrapy-agent-plugin

[Repository](https://github.com/scrapy/scrapy-agent-plugin) · commit [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) · 1/1 checks passing

has-sphinx-docs: no · latest-release: no

All applicable checks pass.

### scrapy/scrapy-lint

[Repository](https://github.com/scrapy/scrapy-lint) · commit [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) · 24/35 checks passing

supports-pypy: no · license: MIT · pylint: yes · has-sphinx-docs: yes · latest-release: 0.1.1 (2026-01-27)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy/scrapy-mcp-official

[Repository](https://github.com/scrapy/scrapy-mcp-official) · commit [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) · 27/30 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.2 (2026-09-07)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### scrapy/unattended-pr-guard

[Repository](https://github.com/scrapy/unattended-pr-guard) · commit [`1e3c311`](https://github.com/scrapy/unattended-pr-guard/commit/1e3c31134253813934af43f3505d4492eee26c2a) · 6/6 checks passing

has-sphinx-docs: no · latest-release: no

All applicable checks pass.

### scrapy/xtractmime

[Repository](https://github.com/scrapy/xtractmime) · commit [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) · 18/29 checks passing

supports-pypy: yes · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.2.1 (2024-01-16)

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff-rules`](REPORT.md#ruff-rules): only the default rules are enabled
- ❌ [`dependabot`](REPORT.md#dependabot): no .github/dependabot.yml

### scrapy-plugins/scrapy-download-handlers-incubator

[Repository](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) · commit [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) · 28/30 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: no · latest-release: 0.5.1 (2026-09-11)

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

### scrapy-plugins/scrapy-playwright

[Repository](https://github.com/scrapy-plugins/scrapy-playwright) · commit [`d99f38d`](https://github.com/scrapy-plugins/scrapy-playwright/commit/d99f38d3483118881add4e2bcbc595d45091f196) · 8/25 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: no · latest-release: 0.0.48 (2026-07-10)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta
- ❌ [`twine-check`](REPORT.md#twine-check): no twine check in tox config

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapy-plugins/scrapy-spider-metadata

[Repository](https://github.com/scrapy-plugins/scrapy-spider-metadata) · commit [`63b3991`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/63b3991dc8f181b2ef358e3b09aeda13261dd7c3) · 16/35 checks passing

supports-pypy: yes · license: BSD License · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2024-09-26)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15
- ❌ [`latest-pypy`](REPORT.md#latest-pypy): PyPy 3.12 not found in CI workflows or tox config

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): tool sections in tox.ini: [pytest]
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.11.2 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes

### scrapy-plugins/zyte-spidermon

[Repository](https://github.com/scrapy-plugins/zyte-spidermon) · commit [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) · 2/20 checks passing

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
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): no .pre-commit-config.yaml
- ❌ [`actionlint`](REPORT.md#actionlint): no .pre-commit-config.yaml
- ❌ [`zizmor`](REPORT.md#zizmor): no .pre-commit-config.yaml

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): no workflow publishes to PyPI
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): no workflow publishes to PyPI
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): no workflow publishes to PyPI
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml

### scrapinghub/dateparser

[Repository](https://github.com/scrapinghub/dateparser) · commit [`ac08823`](https://github.com/scrapinghub/dateparser/commit/ac0882372d11a10e5f7d167ae9fa60be6e9c43a8) · 18/33 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 1.4.3 (2026-09-03)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pyproject-metadata`](REPORT.md#pyproject-metadata): setup.py exists
- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, pytest.ini
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`py-typed`](REPORT.md#py-typed): no py.typed file

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`branch-coverage`](REPORT.md#branch-coverage): no branch = true in coverage config, and no --cov-branch

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`blacken-docs`](REPORT.md#blacken-docs): missing pre-commit hooks: blacken-docs
- ❌ [`sphinx-lint`](REPORT.md#sphinx-lint): missing pre-commit hooks: sphinx-lint

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases

### scrapinghub/extruct

[Repository](https://github.com/scrapinghub/extruct) · commit [`dc3bf7d`](https://github.com/scrapinghub/extruct/commit/dc3bf7d2209ecf421222afc90d3d2dd8c6fd23cf) · 6/23 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.18.0 (2024-11-08)

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
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in setup.cfg

### scrapinghub/number-parser

[Repository](https://github.com/scrapinghub/number-parser) · commit [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) · 7/24 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.3.2 (2023-03-28)

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
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [`publish-on-tag`](REPORT.md#publish-on-tag): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### scrapinghub/scrapyrt

[Repository](https://github.com/scrapinghub/scrapyrt) · commit [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) · 18/34 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: yes · has-sphinx-docs: yes · latest-release: 0.18.1 (2026-06-29)

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

**Linting**

- ❌ [`pre-commit-updates`](REPORT.md#pre-commit-updates): outdated: ruff v0.12.5 (0.15.11 or later expected)
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy-pins`](REPORT.md#sphinx-scrapy-pins): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): not pinned

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml uses an API token
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### scrapinghub/spidermon

[Repository](https://github.com/scrapinghub/spidermon) · commit [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) · 21/32 checks passing

supports-pypy: no · license: BSD-3-Clause · pylint: no · has-sphinx-docs: yes · latest-release: 1.27.0 (2026-08-10)

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

**Linting**

- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Documentation**

- ❌ [`docs-requirements-in`](REPORT.md#docs-requirements-in): no docs/requirements.in
- ❌ [`sphinx-scrapy`](REPORT.md#sphinx-scrapy): sphinx_scrapy not in docs/conf.py or docs/requirements.in

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/agent-exam

[Repository](https://github.com/zytedata/agent-exam) · commit [`c88fec1`](https://github.com/zytedata/agent-exam/commit/c88fec170ff9683dad9d769601206088fdbaeb7d) · 21/34 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: yes · latest-release: 0.2.0 (2026-08-17)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

- ❌ [`pep639-license`](REPORT.md#pep639-license): has license classifiers: License :: OSI Approved :: Apache Software License

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

**Documentation**

- ❌ [`sphinx-scrapy-latest`](REPORT.md#sphinx-scrapy-latest): pinned to 0.8.10, latest is 0.14.0

**Releases**

- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'publish' builds and publishes

### zytedata/claude-measure-usage

[Repository](https://github.com/zytedata/claude-measure-usage) · commit [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) · 16/28 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.1.1 (2026-09-14)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.15

**Packaging**

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

### zytedata/duplicate-url-discarder

[Repository](https://github.com/zytedata/duplicate-url-discarder) · commit [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) · 11/27 checks passing

supports-pypy: no · license: BSD License · pylint: no · has-sphinx-docs: no · latest-release: 0.3.0 (2024-12-30)

**Python versions**

- ❌ [`no-eol-python`](REPORT.md#no-eol-python): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

- ❌ [`no-legacy-config`](REPORT.md#no-legacy-config): legacy files: .coveragerc, .flake8
- ❌ [`pep639-license`](REPORT.md#pep639-license): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [`hatchling`](REPORT.md#hatchling): build backend is setuptools.build_meta

**Typing**

- ❌ [`typed-classifier`](REPORT.md#typed-classifier): no 'Typing :: Typed' classifier
- ❌ [`mypy-strict`](REPORT.md#mypy-strict): no strict = true in mypy config, and no --strict

**Tests and coverage**

- ❌ [`codecov-test-results`](REPORT.md#codecov-test-results): no codecov/codecov-action step with report_type: test_results
- ❌ [`warnings-as-errors`](REPORT.md#warnings-as-errors): no "error" in pytest filterwarnings, and no -W error

**Linting**

- ❌ [`ruff`](REPORT.md#ruff): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [`actionlint`](REPORT.md#actionlint): missing pre-commit hooks: actionlint
- ❌ [`zizmor`](REPORT.md#zizmor): missing pre-commit hooks: zizmor

**Releases**

- ❌ [`trusted-publishing`](REPORT.md#trusted-publishing): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [`separate-build-job`](REPORT.md#separate-build-job): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [`bump-my-version`](REPORT.md#bump-my-version): only legacy (bump2version) configuration, in .bumpversion.cfg

### zytedata/harness-run

[Repository](https://github.com/zytedata/harness-run) · commit [`4028849`](https://github.com/zytedata/harness-run/commit/4028849faf48ac448b1634140cfe3a9cac8f2749) · 9/25 checks passing

supports-pypy: no · license: Apache-2.0 · pylint: no · has-sphinx-docs: no · latest-release: 0.4.0 (2026-09-23)

**Python versions**

- ❌ [`latest-python`](REPORT.md#latest-python): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [`python-classifiers`](REPORT.md#python-classifiers): no classifiers for 3.14, 3.15

**Packaging**

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
