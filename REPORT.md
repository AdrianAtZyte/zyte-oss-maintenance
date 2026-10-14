# Maintenance report

Generated on 2026-10-14 with `oss-maint report`. Do not edit by hand. See [PROJECTS.md](PROJECTS.md) for what fails in each project.

✅ passes · ❌ fails · ➖ not applicable · ⚠️ check error · yes/no or a value: result of an informational check. Click a symbol for details.

## Reference data

Values that checks compare projects against.

- Latest Python: 3.15
- Upcoming Python, with a release candidate: none
- Supported Python versions, with EOL dates: 3.11 (2027-10-31), 3.12 (2028-10-31), 3.13 (2029-10-31), 3.14 (2030-10-31), 3.15 (2031-10-31)
- Python versions of the latest PyPy release: 3.11, 3.12
- End-of-life PyPy Python versions: 3.6, 3.7, 3.8, 3.9, 3.10
- Minimum pre-commit hook versions, the newest releases at least 180 days old: ruff 0.15.11, zizmor 1.24.1
- Latest sphinx-scrapy: 0.14.0

## Summary

Checks passing per group.

| Project | [Python versions](#python-versions) | [Packaging](#packaging) | [Dependencies](#dependencies) | [Typing](#typing) | [Tests and coverage](#tests-and-coverage) | [Linting](#linting) | [Documentation](#documentation) | [Releases](#releases) | Failing | Commit |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | --- |
| **Scrapy and its deps** | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [❌ 4/5](#python-versions) | [✅ 6/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [✅ 4/4](#tests-and-coverage) | [❌ 8/9](#linting) | [❌ 3/4](#documentation) | [✅ 4/4](#releases) | [5](PROJECTS.md#scrapyscrapy) | [`cc4238c`](https://github.com/scrapy/scrapy/commit/cc4238c3a27a788e655caff354f0f8112b18804b) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌ 4/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 0/2](#documentation) | [✅ 4/4](#releases) | [6](PROJECTS.md#scrapycssselect) | [`805705c`](https://github.com/scrapy/cssselect/commit/805705c5a204721d3c486250377a756bd6fa54a5) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [✅ 5/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [✅ 4/4](#typing) | [✅ 4/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [0](PROJECTS.md#scrapyformerly) | [`7a6e30b`](https://github.com/scrapy/formerly/commit/7a6e30b1f9821e90c26e0e81cecfd5f560c19d84) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [❌ 4/5](#python-versions) | [✅ 6/6](#packaging) | [✅ 1/1](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [❌ 3/4](#releases) | [5](PROJECTS.md#scrapyitemadapter) | [`fc9b3e9`](https://github.com/scrapy/itemadapter/commit/fc9b3e9919a458f6a135464304b39be6b4b9d2c4) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌ 1/5](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 0/2](#documentation) | [❌ 2/4](#releases) | [11](PROJECTS.md#scrapyitemloaders) | [`f3e6800`](https://github.com/scrapy/itemloaders/commit/f3e680016d0fd49f24a656f440938ec14c0cd9db) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | [❌ 4/5](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 3/4](#documentation) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyparsel) | [`893eb22`](https://github.com/scrapy/parsel/commit/893eb22ffbb58c12e7ab470fab2e9a004246f85e) |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌ 3/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyprotego) | [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌ 3/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyqueuelib) | [`885ef61`](https://github.com/scrapy/queuelib/commit/885ef61c6ad9b61682329074f539cbb8c262a580) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌ 4/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 0/2](#documentation) | [✅ 4/4](#releases) | [6](PROJECTS.md#scrapyw3lib) | [`cc62486`](https://github.com/scrapy/w3lib/commit/cc624868ea9e41af55d226e8c084bcc722fd6817) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 6/7](#linting) | [➖](#documentation) | [❌ 3/4](#releases) | [13](PROJECTS.md#scrapysphinx-scrapy) | [`9231605`](https://github.com/scrapy/sphinx-scrapy/commit/9231605ac5f164edf053998ed9ba4b61b385f691) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌ 2/3](#python-versions) | [❌ 5/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 6/7](#linting) | [➖](#documentation) | [❌ 3/4](#releases) | [10](PROJECTS.md#scrapysphinx-llm-friendly) | [`2f5b77c`](https://github.com/scrapy/sphinx-llm-friendly/commit/2f5b77c315d5230429761063b475c7c1b015ca79) |
| **scrapy-poet and its deps** | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | [❌ 1/3](#python-versions) | [❌ 4/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 6/8](#linting) | [❌ 3/4](#documentation) | [❌ 3/4](#releases) | [12](PROJECTS.md#scrapinghubscrapy-poet) | [`e87c2d0`](https://github.com/scrapinghub/scrapy-poet/commit/e87c2d01f60855652bd756c918cf11c93256d283) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌ 2/3](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapinghubandi) | [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌ 0/3](#python-versions) | [❌ 4/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 8/9](#linting) | [❌ 3/4](#documentation) | [❌ 3/4](#releases) | [12](PROJECTS.md#scrapinghubweb-poet) | [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | [✅ 3/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 3/4](#documentation) | [✅ 4/4](#releases) | [3](PROJECTS.md#zytedataurl-matcher) | [`f3805d7`](https://github.com/zytedata/url-matcher/commit/f3805d78f101a0594cdfe1fcbf9b7789a0680aae) |
| **Zyte API** | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | [✅ 3/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 3/4](#documentation) | [❌ 3/4](#releases) | [5](PROJECTS.md#scrapy-pluginsscrapy-zyte-api) | [`681d145`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/681d14500b804f291a09306cc2cb9378f0203217) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | [✅ 3/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 5/8](#linting) | [❌ 3/4](#documentation) | [❌ 3/4](#releases) | [10](PROJECTS.md#zytedatapython-zyte-api) | [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 1/6](#linting) | [❌ 0/2](#documentation) | [❌ 3/4](#releases) | [19](PROJECTS.md#scrapy-pluginsscrapy-zyte-smartproxy) | [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [✅ 3/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 1/4](#documentation) | [✅ 4/4](#releases) | [7](PROJECTS.md#zytedatazyte-common-items) | [`f15bcc5`](https://github.com/zytedata/zyte-common-items/commit/f15bcc5008f6d24ce725ab340f0160ec93c6c381) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌ 0/3](#python-versions) | [✅ 6/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 0/2](#documentation) | [✅ 4/4](#releases) | [9](PROJECTS.md#zytedatazyte-parsers) | [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌ 0/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [5](PROJECTS.md#zytedataclear-html) | [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌ 0/3](#python-versions) | [✅ 6/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 3/6](#linting) | [➖](#documentation) | [❌ 2/4](#releases) | [13](PROJECTS.md#zytedatahtml-text) | [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 5/7](#linting) | [➖](#documentation) | [❌ 2/4](#releases) | [12](PROJECTS.md#scrapinghubprice-parser) | [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) |
| **Scrapy Cloud** | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌ 1/5](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 0/6](#linting) | [❌ 3/4](#documentation) | [✅ 4/4](#releases) | [21](PROJECTS.md#scrapinghubpython-scrapinghub) | [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌ 0/3](#python-versions) | [❌ 3/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 0/6](#linting) | [❌ 3/4](#documentation) | [❌ 2/4](#releases) | [21](PROJECTS.md#scrapinghubshub) | [`80a4cad`](https://github.com/scrapinghub/shub/commit/80a4cad661f2a669739c8c3805fd33c67e62674e) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 0/3](#linting) | [➖](#documentation) | [❌ 2/4](#releases) | [17](PROJECTS.md#scrapinghubscrapinghub-entrypoint-scrapy) | [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) |
| **Others** | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 9/9](#linting) | [❌ 0/2](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#scrapyform2request) | [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌ 2/3](#python-versions) | [✅ 4/4](#packaging) | [❌ 1/2](#dependencies) | [❌ 1/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 4/6](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [9](PROJECTS.md#scrapyfrostwork) | [`eaf5cff`](https://github.com/scrapy/frostwork/commit/eaf5cffc3727568d2651273502c2852b660e3738) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [➖](#linting) | [➖](#documentation) | [✅ 1/1](#releases) | [0](PROJECTS.md#scrapyscrapy-agent-plugin) | [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌ 0/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 3/4](#tests-and-coverage) | [❌ 8/9](#linting) | [❌ 1/4](#documentation) | [❌ 3/4](#releases) | [11](PROJECTS.md#scrapyscrapy-lint) | [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌ 2/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [3](PROJECTS.md#scrapyscrapy-mcp-official) | [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [✅ 5/5](#linting) | [➖](#documentation) | [✅ 1/1](#releases) | [0](PROJECTS.md#scrapyunattended-pr-guard) | [`1e3c311`](https://github.com/scrapy/unattended-pr-guard/commit/1e3c31134253813934af43f3505d4492eee26c2a) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌ 1/5](#python-versions) | [✅ 6/6](#packaging) | [➖](#dependencies) | [❌ 1/3](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 5/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [11](PROJECTS.md#scrapyxtractmime) | [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [✅ 3/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/4](#tests-and-coverage) | [✅ 7/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [2](PROJECTS.md#scrapy-pluginsscrapy-download-handlers-incubator) | [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌ 0/3](#python-versions) | [❌ 3/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 0/3](#linting) | [➖](#documentation) | [❌ 1/4](#releases) | [17](PROJECTS.md#scrapy-pluginsscrapy-playwright) | [`d99f38d`](https://github.com/scrapy-plugins/scrapy-playwright/commit/d99f38d3483118881add4e2bcbc595d45091f196) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌ 1/5](#python-versions) | [❌ 3/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 3/8](#linting) | [❌ 0/2](#documentation) | [❌ 2/4](#releases) | [19](PROJECTS.md#scrapy-pluginsscrapy-spider-metadata) | [`63b3991`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/63b3991dc8f181b2ef358e3b09aeda13261dd7c3) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 0/3](#linting) | [➖](#documentation) | [❌ 0/4](#releases) | [18](PROJECTS.md#scrapy-pluginszyte-spidermon) | [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌ 0/3](#python-versions) | [❌ 3/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/3](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 6/9](#linting) | [❌ 0/2](#documentation) | [❌ 3/4](#releases) | [15](PROJECTS.md#scrapinghubdateparser) | [`ac08823`](https://github.com/scrapinghub/dateparser/commit/ac0882372d11a10e5f7d167ae9fa60be6e9c43a8) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 1/4](#linting) | [➖](#documentation) | [❌ 1/4](#releases) | [17](PROJECTS.md#scrapinghubextruct) | [`dc3bf7d`](https://github.com/scrapinghub/extruct/commit/dc3bf7d2209ecf421222afc90d3d2dd8c6fd23cf) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 4/6](#linting) | [➖](#documentation) | [❌ 0/4](#releases) | [17](PROJECTS.md#scrapinghubnumber-parser) | [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌ 0/3](#python-versions) | [✅ 6/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/4](#tests-and-coverage) | [❌ 5/8](#linting) | [❌ 1/4](#documentation) | [❌ 2/4](#releases) | [16](PROJECTS.md#scrapinghubscrapyrt) | [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 3/4](#tests-and-coverage) | [❌ 7/8](#linting) | [❌ 0/2](#documentation) | [❌ 3/4](#releases) | [11](PROJECTS.md#scrapinghubspidermon) | [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 8/9](#linting) | [❌ 3/4](#documentation) | [❌ 3/4](#releases) | [13](PROJECTS.md#zytedataagent-exam) | [`c88fec1`](https://github.com/zytedata/agent-exam/commit/c88fec170ff9683dad9d769601206088fdbaeb7d) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌ 0/3](#python-versions) | [❌ 5/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 6/7](#linting) | [➖](#documentation) | [✅ 4/4](#releases) | [12](PROJECTS.md#zytedataclaude-measure-usage) | [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌ 0/3](#python-versions) | [❌ 3/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/4](#tests-and-coverage) | [❌ 1/4](#linting) | [➖](#documentation) | [❌ 1/4](#releases) | [16](PROJECTS.md#zytedataduplicate-url-discarder) | [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌ 1/3](#python-versions) | [❌ 5/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 0/4](#linting) | [➖](#documentation) | [❌ 3/4](#releases) | [16](PROJECTS.md#zytedataharness-run) | [`4028849`](https://github.com/zytedata/harness-run/commit/4028849faf48ac448b1634140cfe3a9cac8f2749) |

## Python versions

| Check | Statement | Results |
| --- | --- | --- |
| [`no-eol-python`](#no-eol-python) | Support for end-of-life Python versions is dropped. | 13/44 passing |
| [`latest-python`](#latest-python) | The latest stable Python version is declared as supported and tested in CI. | 17/44 passing |
| [`unreleased-python`](#unreleased-python) | The upcoming Python version is tested in CI, once it has a release candidate. | 0/0 passing |
| [`python-classifiers`](#python-classifiers) | Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes. | 17/42 passing |
| [`supports-pypy`](#supports-pypy) | The project supports PyPy: it has the PyPy classifier or tests PyPy in CI. | 12/44 yes |
| [`latest-pypy`](#latest-pypy) | The latest PyPy version is declared as supported and tested in CI. | 1/12 passing |
| [`no-eol-pypy`](#no-eol-pypy) | End-of-life PyPy versions are not tested in CI. | 12/12 passing |

| Project | [no-eol-python](#no-eol-python) | [latest-python](#latest-python) | [unreleased-python](#unreleased-python) | [python-classifiers](#python-classifiers) | [supports-pypy](#supports-pypy) | [latest-pypy](#latest-pypy) | [no-eol-pypy](#no-eol-pypy) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | yes | [❌](#latest-pypy) | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Others** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |

### no-eol-python

Support for end-of-life Python versions is dropped.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/protego](https://github.com/scrapy/protego): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): requires-python is not declared
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): requires-python is not declared
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### latest-python

The latest stable Python version is declared as supported and tested in CI.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### unreleased-python

The upcoming Python version is tested in CI, once it has a release candidate.

- ➖ No upcoming Python version has a release candidate. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/parsel](https://github.com/scrapy/parsel), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### python-classifiers

Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no classifiers for 3.15
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no classifiers for 3.15
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no classifiers for 3.15
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no classifiers for 3.14, 3.15
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no classifiers for 3.15
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no classifiers for 3.15
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no classifiers for 3.15
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no classifiers for 3.15
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no classifiers for 3.15
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no classifiers for 3.14, 3.15
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no classifiers for 3.15
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no classifiers for 3.15
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no classifiers for 3.15
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no classifiers for 3.15
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no classifiers for 3.15
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no classifiers for 3.15
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no classifiers for 3.14, 3.15
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no classifiers for 3.14, 3.15
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ requires-python is not declared. [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser)

### supports-pypy

The project supports PyPy: it has the PyPy classifier or tests PyPy in CI.

- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### latest-pypy

The latest PyPy version is declared as supported and tested in CI.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/protego](https://github.com/scrapy/protego): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): PyPy 3.12 not found in CI workflows or tox config
- ➖ Does not support PyPy. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-eol-pypy

End-of-life PyPy versions are not tested in CI.

- ➖ Does not support PyPy. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Packaging

| Check | Statement | Results |
| --- | --- | --- |
| [`pyproject-metadata`](#pyproject-metadata) | Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg. | 37/44 passing |
| [`no-legacy-config`](#no-legacy-config) | There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini. | 31/44 passing |
| [`license`](#license) | The license: the license field of package metadata, or else the license classifiers. | BSD-3-Clause (22), Apache-2.0 (10), BSD License (8), MIT (3), no (1) |
| [`pep639-license`](#pep639-license) | The license is declared as an SPDX expression (PEP 639), without license classifiers. | 29/38 passing |
| [`hatchling`](#hatchling) | The build backend is hatchling. | 33/43 passing |
| [`project-urls`](#project-urls) | Project URLs are declared in [project.urls]. | 38/38 passing |
| [`twine-check`](#twine-check) | `twine check` validates the built distributions in tox. | 32/43 passing |

| Project | [pyproject-metadata](#pyproject-metadata) | [no-legacy-config](#no-legacy-config) | [license](#license) | [pep639-license](#pep639-license) | [hatchling](#hatchling) | [project-urls](#project-urls) | [twine-check](#twine-check) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#twine-check) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | [❌](#twine-check) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | [❌](#no-legacy-config) | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | BSD License | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#twine-check) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#twine-check) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#pyproject-metadata) | ✅ | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| **Others** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | ✅ | Apache-2.0 | ✅ | [➖](#hatchling) | ✅ | [➖](#twine-check) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#project-urls) | [➖](#twine-check) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#project-urls) | [➖](#twine-check) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | ✅ | [❌](#twine-check) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#no-legacy-config) | BSD License | [❌](#pep639-license) | [❌](#hatchling) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | ✅ |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | [❌](#twine-check) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#no-legacy-config) | BSD License | [❌](#pep639-license) | [❌](#hatchling) | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | [❌](#twine-check) |

### pyproject-metadata

Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): setup.py exists
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-legacy-config

There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini.

- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): legacy files: requirements-dev.txt
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): legacy files: requirements-dev.txt
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): legacy files: requirements-dev.txt
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): legacy files: .bandit.yml, .flake8, .isort.cfg; tool sections in setup.cfg: [mypy], [mypy-pytest.*], [mypy-scrapy.*], [mypy-twisted.*], [mypy-w3lib.*]
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): legacy files: requirements-dev.txt
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): legacy files: pytest.ini
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): tool sections in setup.cfg: [flake8]
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): tool sections in tox.ini: [pytest]
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): legacy files: .coveragerc, pytest.ini
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): legacy files: .coveragerc, .isort.cfg, pytest.ini, requirements-dev.txt
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): legacy files: .coveragerc
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): legacy files: .coveragerc, .flake8
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### license

The license: the license field of package metadata, or else the license classifiers.

- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pep639-license

The license is declared as an SPDX expression (PEP 639), without license classifiers.

- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### hatchling

The build backend is hatchling.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no build-backend in pyproject.toml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no build-backend in pyproject.toml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no pyproject.toml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): build backend is setuptools.build_meta
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no build-backend in pyproject.toml
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no build-backend in pyproject.toml
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): build backend is setuptools.build_meta
- ➖ Rust extension, built with maturin. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### project-urls

Project URLs are declared in [project.urls].

- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### twine-check

`twine check` validates the built distributions in tox.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no twine check in tox config
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no twine check in tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no twine check in tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): twine check runs in a workflow, not in tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no twine check in tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no twine check in tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no twine check in tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no twine check in tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): twine check runs in a workflow, not in tox
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): twine check runs in a workflow, not in tox
- ➖ Wheels are built per platform by maturin in CI, where twine check runs on them. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Dependencies

| Check | Statement | Results |
| --- | --- | --- |
| [`dependency-lower-bounds`](#dependency-lower-bounds) | Every runtime dependency has a lower bound. | 23/30 passing |
| [`min-deps-env`](#min-deps-env) | A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it). | 25/37 passing |

| Project | [dependency-lower-bounds](#dependency-lower-bounds) | [min-deps-env](#min-deps-env) |
| --- | :---: | :---: |
| **Scrapy and its deps** | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#dependency-lower-bounds) | ✅ |
| **scrapy-poet and its deps** | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ |
| **Zyte API** | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [➖](#dependency-lower-bounds) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#min-deps-env) |
| **Scrapy Cloud** | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Others** | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#min-deps-env) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#min-deps-env) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |

### dependency-lower-bounds

Every runtime dependency has a lower bound.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no lower bound: packaging, tldextract
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no lower bound: docutils, tabulate
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no lower bound: lxml, lxml-html-clean
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no lower bound: click, docker, importlib-metadata, packaging, pip, PyYAML, requests, retrying, setuptools, toml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ➖ No runtime dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/xtractmime](https://github.com/scrapy/xtractmime)
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### min-deps-env

A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it).

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment for minimum dependency versions
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no tox environment for minimum dependency versions
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no tox environment for minimum dependency versions
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment for minimum dependency versions
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no tox environment for minimum dependency versions
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no tox environment for minimum dependency versions
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no tox environment for minimum dependency versions
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no tox environment for minimum dependency versions
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no tox environment for minimum dependency versions
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no tox environment for minimum dependency versions
- ➖ No dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/xtractmime](https://github.com/scrapy/xtractmime)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Typing

| Check | Statement | Results |
| --- | --- | --- |
| [`py-typed`](#py-typed) | The package ships type hints (a py.typed marker). | 26/44 passing |
| [`typed-classifier`](#typed-classifier) | A package with a py.typed marker has the 'Typing :: Typed' classifier. | 3/26 passing |
| [`mypy`](#mypy) | mypy runs in tox, CI workflows or pre-commit. | 36/43 passing |
| [`mypy-strict`](#mypy-strict) | mypy runs in strict mode: strict = true in its config, or --strict. | 22/36 passing |

| Project | [py-typed](#py-typed) | [typed-classifier](#typed-classifier) | [mypy](#mypy) | [mypy-strict](#mypy-strict) |
| --- | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **Others** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |

### py-typed

The package ships type hints (a py.typed marker).

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no py.typed file
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no py.typed file
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no py.typed file
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no py.typed file
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no py.typed file
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no py.typed file
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no py.typed file
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no py.typed file
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no py.typed file
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no py.typed file
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no py.typed file
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no py.typed file
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no py.typed file
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no py.typed file
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no py.typed file
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no py.typed file
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no py.typed file
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no py.typed file
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### typed-classifier

A package with a py.typed marker has the 'Typing :: Typed' classifier.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no 'Typing :: Typed' classifier
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no 'Typing :: Typed' classifier
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no 'Typing :: Typed' classifier
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no 'Typing :: Typed' classifier
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Typing :: Typed' classifier
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Typing :: Typed' classifier
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Typing :: Typed' classifier
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Typing :: Typed' classifier
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no 'Typing :: Typed' classifier
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Typing :: Typed' classifier
- ➖ No py.typed file. [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### mypy

mypy runs in tox, CI workflows or pre-commit.

- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): mypy not found
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): mypy not found
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): mypy not found
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): mypy not found
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): mypy not found
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): mypy not found
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): mypy not found
- ➖ Runs mypy through make py, in CI. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### mypy-strict

mypy runs in strict mode: strict = true in its config, or --strict.

- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no strict = true in mypy config, and no --strict
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no strict = true in mypy config, and no --strict
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no strict = true in mypy config, and no --strict
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no strict = true in mypy config, and no --strict
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no strict = true in mypy config, and no --strict
- ➖ Does not run mypy. [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Agent plugin, not a Python package. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Tests and coverage

| Check | Statement | Results |
| --- | --- | --- |
| [`codecov`](#codecov) | Test coverage is uploaded to Codecov in CI workflows. | 37/44 passing |
| [`codecov-test-results`](#codecov-test-results) | Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results). | 14/44 passing |
| [`branch-coverage`](#branch-coverage) | Branch coverage is enabled. | 27/44 passing |
| [`warnings-as-errors`](#warnings-as-errors) | pytest turns warnings into errors: "error" in filterwarnings, or -W error. | 8/44 passing |

| Project | [codecov](#codecov) | [codecov-test-results](#codecov-test-results) | [branch-coverage](#branch-coverage) | [warnings-as-errors](#warnings-as-errors) |
| --- | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| **Others** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#branch-coverage) | [➖](#warnings-as-errors) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | [❌](#branch-coverage) | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#branch-coverage) | [➖](#warnings-as-errors) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | [❌](#codecov-test-results) | [❌](#branch-coverage) | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#codecov-test-results) | ✅ | [❌](#warnings-as-errors) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#codecov) | [❌](#codecov-test-results) | [❌](#branch-coverage) | [❌](#warnings-as-errors) |

### codecov

Test coverage is uploaded to Codecov in CI workflows.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step for coverage
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step for coverage
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step for coverage
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no codecov/codecov-action step for coverage
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step for coverage
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step for coverage
- ➖ Agent plugin, has no code to test. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-test-results

Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results).

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step with report_type: test_results
- ➖ Agent plugin, has no code to test. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### branch-coverage

Branch coverage is enabled.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no branch = true in coverage config, and no --cov-branch
- ➖ Agent plugin, has no code to test. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### warnings-as-errors

pytest turns warnings into errors: "error" in filterwarnings, or -W error.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no "error" in pytest filterwarnings, and no -W error
- ➖ Agent plugin, has no code to test. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Linting

| Check | Statement | Results |
| --- | --- | --- |
| [`ruff`](#ruff) | ruff-check and ruff-format are used, instead of tools that ruff replaces. | 34/44 passing |
| [`ruff-rules`](#ruff-rules) | ruff enables rules beyond its defaults, with select or extend-select. | 32/35 passing |
| [`pylint`](#pylint) | A tox environment runs pylint. | 10/44 yes |
| [`pre-commit-in-ci`](#pre-commit-in-ci) | pre-commit runs in CI workflows, directly or through tox. | 37/41 passing |
| [`pre-commit-updates`](#pre-commit-updates) | The ruff and zizmor pre-commit hooks are updated within 180 days of a new release. | 29/36 passing |
| [`actionlint`](#actionlint) | GitHub Actions workflows are linted with actionlint. | 26/45 passing |
| [`zizmor`](#zizmor) | GitHub Actions workflows are audited with zizmor. | 29/45 passing |
| [`dependabot`](#dependabot) | Dependabot updates GitHub Actions, which zizmor requires pinning. | 27/29 passing |
| [`has-sphinx-docs`](#has-sphinx-docs) | The project has Sphinx docs (docs/conf.py). | 22/46 yes |
| [`blacken-docs`](#blacken-docs) | Code examples in the docs are formatted with blacken-docs. | 17/22 passing |
| [`sphinx-lint`](#sphinx-lint) | The docs are linted with sphinx-lint. | 17/22 passing |

| Project | [ruff](#ruff) | [ruff-rules](#ruff-rules) | [pylint](#pylint) | [pre-commit-in-ci](#pre-commit-in-ci) | [pre-commit-updates](#pre-commit-updates) | [actionlint](#actionlint) | [zizmor](#zizmor) | [dependabot](#dependabot) | [has-sphinx-docs](#has-sphinx-docs) | [blacken-docs](#blacken-docs) | [sphinx-lint](#sphinx-lint) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | yes | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **scrapy-poet and its deps** | | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | ✅ | [❌](#zizmor) | [➖](#dependabot) | yes | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | no | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| **Zyte API** | | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | no | [❌](#pre-commit-in-ci) | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy Cloud** | | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Others** | | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | [➖](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | yes | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#ruff-rules) | no | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#ruff) | [➖](#ruff-rules) | yes | [➖](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ | no | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | ✅ | no | ✅ | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | yes | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | yes | ✅ | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#zizmor) | [➖](#dependabot) | yes | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | yes | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#ruff-rules) | no | ✅ | ✅ | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#ruff) | [❌](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |

### ruff

ruff-check and ruff-format are used, instead of tools that ruff replaces.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ Agent plugin, has no Python code. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### ruff-rules

ruff enables rules beyond its defaults, with select or extend-select.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): only the default rules are enabled
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): only the default rules are enabled
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): only the default rules are enabled
- ➖ Does not use ruff. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)

### pylint

A tox environment runs pylint.

- ➖ Agent plugin, has no Python code. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ JavaScript GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pre-commit-in-ci

pre-commit runs in CI workflows, directly or through tox.

- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): not run in CI workflows or tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): not run in CI workflows or tox
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): not run in CI workflows or tox
- ➖ No .pre-commit-config.yaml. [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-updates

The ruff and zizmor pre-commit hooks are updated within 180 days of a new release.

- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): outdated: ruff v0.11.13 (0.15.11 or later expected)
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): outdated: ruff v0.11.13 (0.15.11 or later expected)
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): outdated: ruff v0.15.6 (0.15.11 or later expected)
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): outdated: ruff v0.11.2 (0.15.11 or later expected)
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): outdated: ruff v0.12.5 (0.15.11 or later expected)
- ➖ No checked hooks. [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder)
- ➖ No .pre-commit-config.yaml. [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### actionlint

GitHub Actions workflows are linted with actionlint.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing pre-commit hooks: actionlint
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: actionlint
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: actionlint
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### zizmor

GitHub Actions workflows are audited with zizmor.

- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): missing pre-commit hooks: zizmor
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: zizmor
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): missing pre-commit hooks: zizmor
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: zizmor
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### dependabot

Dependabot updates GitHub Actions, which zizmor requires pinning.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no .github/dependabot.yml
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no .github/dependabot.yml
- ➖ Does not use zizmor. [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ No GitHub Actions workflows. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### has-sphinx-docs

The project has Sphinx docs (docs/conf.py).

Nothing to report.

### blacken-docs

Code examples in the docs are formatted with blacken-docs.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: blacken-docs
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: blacken-docs
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### sphinx-lint

The docs are linted with sphinx-lint.

- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: sphinx-lint
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

## Documentation

| Check | Statement | Results |
| --- | --- | --- |
| [`docs-requirements-in`](#docs-requirements-in) | Sphinx docs requirements are defined in docs/requirements.in. | 10/22 passing |
| [`sphinx-scrapy`](#sphinx-scrapy) | Sphinx docs use sphinx-scrapy. | 13/22 passing |
| [`sphinx-scrapy-pins`](#sphinx-scrapy-pins) | sphinx-scrapy is pinned to the same version in the tox requires, the docs requirements and the pre-commit hook rev. | 10/13 passing |
| [`sphinx-scrapy-latest`](#sphinx-scrapy-latest) | sphinx-scrapy is pinned to its latest release. | 0/13 passing |

| Project | [docs-requirements-in](#docs-requirements-in) | [sphinx-scrapy](#sphinx-scrapy) | [sphinx-scrapy-pins](#sphinx-scrapy-pins) | [sphinx-scrapy-latest](#sphinx-scrapy-latest) |
| --- | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapy/protego](https://github.com/scrapy/protego) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| **Others** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) |

### docs-requirements-in

Sphinx docs requirements are defined in docs/requirements.in.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no docs/requirements.in
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no docs/requirements.in
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no docs/requirements.in
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no docs/requirements.in
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no docs/requirements.in
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no docs/requirements.in
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no docs/requirements.in
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no docs/requirements.in
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no docs/requirements.in
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no docs/requirements.in
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no docs/requirements.in
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no docs/requirements.in
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### sphinx-scrapy

Sphinx docs use sphinx-scrapy.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### sphinx-scrapy-pins

sphinx-scrapy is pinned to the same version in the tox requires, the docs requirements and the pre-commit hook rev.

- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### sphinx-scrapy-latest

sphinx-scrapy is pinned to its latest release.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): pinned to 0.8.4, latest is 0.14.0
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): pinned to 0.8.12, latest is 0.14.0
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): pinned to 0.8.12, latest is 0.14.0
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): pinned to 0.13.0, latest is 0.14.0
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): pinned to 0.7.1, latest is 0.14.0
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): pinned to 0.8.4, latest is 0.14.0
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): pinned to 0.8.10, latest is 0.14.0
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/harness-run](https://github.com/zytedata/harness-run)

## Releases

| Check | Statement | Results |
| --- | --- | --- |
| [`latest-release`](#latest-release) | The latest release on PyPI, with its date. | 43/46 yes |
| [`trusted-publishing`](#trusted-publishing) | Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment. | 33/44 passing |
| [`publish-on-tag`](#publish-on-tag) | Publishing is triggered by pushing a tag, not by creating a GitHub release. | 39/44 passing |
| [`separate-build-job`](#separate-build-job) | The publish workflow builds distributions in a separate job from the one that publishes them. | 21/44 passing |
| [`bump-my-version`](#bump-my-version) | bump-my-version is configured, in pyproject.toml or .bumpversion.toml. | 41/46 passing |

| Project | [latest-release](#latest-release) | [trusted-publishing](#trusted-publishing) | [publish-on-tag](#publish-on-tag) | [separate-build-job](#separate-build-job) | [bump-my-version](#bump-my-version) |
| --- | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 2.19.0 (2026-09-10) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | 1.6.0 (2026-10-09) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | 0.1.0 (2026-08-05) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | 0.13.1 (2026-01-08) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | 1.5.0 (2026-09-29) | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | 1.12.1 (2026-09-28) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | 0.7.0 (2026-09-21) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | 1.10.0 (2026-08-24) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | 2.5.0 (2026-09-30) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | 0.14.0 (2026-10-14) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | 0.7.0 (2026-10-03) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **scrapy-poet and its deps** | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | 0.27.2 (2026-04-28) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | 0.9.0 (2026-09-17) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | 0.24.1 (2026-04-28) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | 0.6.0 (2025-02-14) | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | 0.36.0 (2026-08-20) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | 0.11.0 (2026-07-23) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | 2.4.1 (2025-03-24) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | 0.30.0 (2026-10-14) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | 0.6.0 (2025-10-24) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | 0.5.0 (2025-10-24) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | 0.7.1 (2025-10-06) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | 0.5.1 (2026-03-19) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Scrapy Cloud** | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | 2.9.0 (2026-08-12) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | 2.18.1 (2026-07-08) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | 0.18.1 (2026-01-28) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Others** | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | 0.2.0 (2024-07-15) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | 0.1.6 (2026-09-23) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | no | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | 0.1.1 (2026-01-27) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | 0.1.2 (2026-09-07) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | no | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | 0.2.1 (2024-01-16) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | 0.5.1 (2026-09-11) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | 0.0.48 (2026-07-10) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | 0.2.0 (2024-09-26) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | no | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | 1.4.3 (2026-09-03) | ✅ | [❌](#publish-on-tag) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | 0.18.0 (2024-11-08) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | 0.3.2 (2023-03-28) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | 0.18.1 (2026-06-29) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | 1.27.0 (2026-08-10) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | 0.2.0 (2026-08-17) | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | 0.1.1 (2026-09-14) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | 0.3.0 (2024-12-30) | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | 0.4.0 (2026-09-23) | ✅ | ✅ | ✅ | [❌](#bump-my-version) |

### latest-release

The latest release on PyPI, with its date.

Nothing to report.

### trusted-publishing

Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment.

- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml uses an API token
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ➖ Agent plugin, not published to PyPI. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action, not published to PyPI. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### publish-on-tag

Publishing is triggered by pushing a tag, not by creating a GitHub release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml is triggered by GitHub releases
- ➖ Agent plugin, not published to PyPI. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action, not published to PyPI. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### separate-build-job

The publish workflow builds distributions in a separate job from the one that publishes them.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ➖ Agent plugin, not published to PyPI. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action, not published to PyPI. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### bump-my-version

bump-my-version is configured, in pyproject.toml or .bumpversion.toml.

- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): only legacy (bump2version) configuration, in setup.cfg
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
