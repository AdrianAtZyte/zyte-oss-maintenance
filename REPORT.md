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
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [❌ 4/5](#tests-and-coverage) | [❌ 10/12](#linting) | [❌ 6/7](#documentation) | [✅ 4/4](#releases) | [7](PROJECTS.md#scrapyscrapy) | [`3f12941`](https://github.com/scrapy/scrapy/commit/3f129418859a0757fa6835f78a25d99bdc1f7bce) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌ 4/5](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 2/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 4/6](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#scrapycssselect) | [`6a859d5`](https://github.com/scrapy/cssselect/commit/6a859d51b5bdd3810ac5b45541069bbcc20321ae) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [✅ 5/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [✅ 4/4](#typing) | [❌ 4/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [1](PROJECTS.md#scrapyformerly) | [`7a6e30b`](https://github.com/scrapy/formerly/commit/7a6e30b1f9821e90c26e0e81cecfd5f560c19d84) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 1/1](#dependencies) | [❌ 3/4](#typing) | [❌ 2/6](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [❌ 3/4](#releases) | [7](PROJECTS.md#scrapyitemadapter) | [`d0565e1`](https://github.com/scrapy/itemadapter/commit/d0565e1c70618cbb36246358314fb38d16372f88) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌ 1/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 3/6](#documentation) | [❌ 2/4](#releases) | [12](PROJECTS.md#scrapyitemloaders) | [`f3e6800`](https://github.com/scrapy/itemloaders/commit/f3e680016d0fd49f24a656f440938ec14c0cd9db) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 4/5](#tests-and-coverage) | [✅ 12/12](#linting) | [❌ 6/8](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyparsel) | [`893eb22`](https://github.com/scrapy/parsel/commit/893eb22ffbb58c12e7ab470fab2e9a004246f85e) |
| [scrapy/protego](https://github.com/scrapy/protego) | [❌ 3/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 4/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyprotego) | [`53d6df8`](https://github.com/scrapy/protego/commit/53d6df88ea74a29561d4c415d45ee77ddc86c1af) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [❌ 3/5](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [6](PROJECTS.md#scrapyqueuelib) | [`885ef61`](https://github.com/scrapy/queuelib/commit/885ef61c6ad9b61682329074f539cbb8c262a580) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌ 4/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [❌ 11/12](#linting) | [❌ 3/6](#documentation) | [✅ 4/4](#releases) | [8](PROJECTS.md#scrapyw3lib) | [`cc62486`](https://github.com/scrapy/w3lib/commit/cc624868ea9e41af55d226e8c084bcc722fd6817) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌ 1/5](#python-versions) | [✅ 7/7](#packaging) | [➖](#dependencies) | [❌ 1/3](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 7/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [12](PROJECTS.md#scrapyxtractmime) | [`9d50fcb`](https://github.com/scrapy/xtractmime/commit/9d50fcb0d7abd7a96f7dee746d9285faba4af6db) |
| **Scrapy plugins** | | | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [✅ 3/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/6](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapy-pluginsscrapy-download-handlers-incubator) | [`f585f8d`](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator/commit/f585f8da60d14ec804c4b3b7d105c4ce55d5238b) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 0/3](#linting) | [✅ 2/2](#documentation) | [❌ 1/4](#releases) | [20](PROJECTS.md#scrapy-pluginsscrapy-playwright) | [`d99f38d`](https://github.com/scrapy-plugins/scrapy-playwright/commit/d99f38d3483118881add4e2bcbc595d45091f196) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌ 1/5](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 4/10](#linting) | [❌ 2/6](#documentation) | [❌ 2/4](#releases) | [25](PROJECTS.md#scrapy-pluginsscrapy-spider-metadata) | [`63b3991`](https://github.com/scrapy-plugins/scrapy-spider-metadata/commit/63b3991dc8f181b2ef358e3b09aeda13261dd7c3) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 2/6](#linting) | [✅ 1/1](#documentation) | [❌ 1/4](#releases) | [20](PROJECTS.md#zytedataduplicate-url-discarder) | [`8db08b3`](https://github.com/zytedata/duplicate-url-discarder/commit/8db08b3edf638f34ee6ad7393612f579b5bfb90f) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 2/6](#linting) | [✅ 1/1](#documentation) | [❌ 1/4](#releases) | [19](PROJECTS.md#zytedataduplicate-url-discarder-rules) | [`7281048`](https://github.com/zytedata/duplicate-url-discarder-rules/commit/7281048b2cfa0538c0b355e8f91185f27367649d) |
| **Scrapy tools** | | | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌ 0/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 3/5](#tests-and-coverage) | [❌ 10/11](#linting) | [❌ 5/8](#documentation) | [❌ 3/4](#releases) | [13](PROJECTS.md#scrapyscrapy-lint) | [`30a3872`](https://github.com/scrapy/scrapy-lint/commit/30a387279f0be38a48237d31725b1d52a2bcf297) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 7/10](#linting) | [❌ 4/8](#documentation) | [❌ 2/4](#releases) | [18](PROJECTS.md#scrapinghubscrapyrt) | [`066cdaf`](https://github.com/scrapinghub/scrapyrt/commit/066cdafb9dc5e864f3e1dd19cb7fafec7fefb7fe) |
| **Feed exporters** | | | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 4/8](#linting) | [❌ 0/1](#documentation) | [❌ 1/4](#releases) | [23](PROJECTS.md#scrapy-pluginsscrapy-feedexport-warc) | [`ad7956f`](https://github.com/scrapy-plugins/scrapy-feedexport-warc/commit/ad7956f4825fa2c4671c1849a8ad7a4eb2cc34d1) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-azure-storage) | [`4f36ff8`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage/commit/4f36ff805239bace39bacc8c1e02cc8c876013b4) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [19](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-dropbox) | [`4e4cca6`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox/commit/4e4cca6f5240d790708219c0344b812eb76a854f) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [22](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-google-drive) | [`ee13d9d`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive/commit/ee13d9dfc0ef378cfa68fba15e33a1df6078677b) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-google-sheets) | [`25f2a8c`](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets/commit/25f2a8c6079e85823c7e640b17eea2ad5ed8f767) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/5](#tests-and-coverage) | [❌ 0/1](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-onedrive) | [`9b5fdd6`](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive/commit/9b5fdd62704aa1c666419f3d6ea201ce3f534132) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 4/8](#linting) | [✅ 2/2](#documentation) | [❌ 3/4](#releases) | [19](PROJECTS.md#scrapy-pluginsscrapy-feedexporter-sftp) | [`38c9e5b`](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp/commit/38c9e5b244bfa363de9ede92f7069ae7bcbce469) |
| **scrapy-poet and its deps** | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | [❌ 1/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 8/10](#linting) | [❌ 7/8](#documentation) | [❌ 3/4](#releases) | [13](PROJECTS.md#scrapinghubscrapy-poet) | [`e87c2d0`](https://github.com/scrapinghub/scrapy-poet/commit/e87c2d01f60855652bd756c918cf11c93256d283) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌ 2/3](#python-versions) | [❌ 6/7](#packaging) | [➖](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [5](PROJECTS.md#scrapinghubandi) | [`7a07b33`](https://github.com/scrapinghub/andi/commit/7a07b339ca1cc5e3c6495635b02eb01b5c483ebd) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 10/11](#linting) | [❌ 7/8](#documentation) | [❌ 3/4](#releases) | [14](PROJECTS.md#scrapinghubweb-poet) | [`b3cc347`](https://github.com/scrapinghub/web-poet/commit/b3cc347952b9bc6cf534e44543b789d2f5f2fafb) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [✅ 4/4](#typing) | [❌ 4/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 6/8](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#zytedataurl-matcher) | [`f3805d7`](https://github.com/zytedata/url-matcher/commit/f3805d78f101a0594cdfe1fcbf9b7789a0680aae) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌ 2/3](#python-versions) | [✅ 4/4](#packaging) | [❌ 1/2](#dependencies) | [❌ 1/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 4/8](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [11](PROJECTS.md#scrapyfrostwork) | [`eaf5cff`](https://github.com/scrapy/frostwork/commit/eaf5cffc3727568d2651273502c2852b660e3738) |
| **Zyte API** | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 5/6](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 6/8](#documentation) | [❌ 3/4](#releases) | [7](PROJECTS.md#scrapy-pluginsscrapy-zyte-api) | [`681d145`](https://github.com/scrapy-plugins/scrapy-zyte-api/commit/681d14500b804f291a09306cc2cb9378f0203217) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | [✅ 3/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 7/10](#linting) | [❌ 7/8](#documentation) | [❌ 3/4](#releases) | [12](PROJECTS.md#zytedatapython-zyte-api) | [`efc4fdc`](https://github.com/zytedata/python-zyte-api/commit/efc4fdc6cebf36de26a946d0e665d539cafbecf9) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 2/8](#linting) | [❌ 4/6](#documentation) | [❌ 3/4](#releases) | [22](PROJECTS.md#scrapy-pluginsscrapy-zyte-smartproxy) | [`debd444`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy/commit/debd4445343d0c3a1eba9fa0ce269613bb3b9d5c) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [✅ 3/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 4/8](#documentation) | [✅ 4/4](#releases) | [9](PROJECTS.md#zytedatazyte-common-items) | [`f15bcc5`](https://github.com/zytedata/zyte-common-items/commit/f15bcc5008f6d24ce725ab340f0160ec93c6c381) |
| **Scrapy Cloud** | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌ 1/5](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/8](#linting) | [❌ 7/8](#documentation) | [✅ 4/4](#releases) | [24](PROJECTS.md#scrapinghubpython-scrapinghub) | [`d0d7b29`](https://github.com/scrapinghub/python-scrapinghub/commit/d0d7b29153e40bbb0f9c56ab23caab86393f853e) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌ 0/3](#python-versions) | [❌ 3/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/8](#linting) | [❌ 7/8](#documentation) | [❌ 2/4](#releases) | [25](PROJECTS.md#scrapinghubshub) | [`910ccff`](https://github.com/scrapinghub/shub/commit/910ccffccb3da12e093a70b18c2dfe93e4ac64f6) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 0/3](#linting) | [✅ 2/2](#documentation) | [❌ 2/4](#releases) | [19](PROJECTS.md#scrapinghubscrapinghub-entrypoint-scrapy) | [`bf9632c`](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy/commit/bf9632c78355b545126363ce557106c1b9c3bb54) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/3](#linting) | [✅ 1/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapinghubshub-workflow) | [`237107e`](https://github.com/scrapinghub/shub-workflow/commit/237107e06250247a00bfd04368af3b0ed26468b6) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌ 0/3](#python-versions) | [❌ 0/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/6](#tests-and-coverage) | [❌ 3/8](#linting) | [✅ 2/2](#documentation) | [❌ 2/4](#releases) | [21](PROJECTS.md#scrapinghubscrapy-frontera) | [`56ea2e1`](https://github.com/scrapinghub/scrapy-frontera/commit/56ea2e1ef39a174eac61da2edcdb21d1f1ecf5e5) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/6](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 0/1](#documentation) | [❌ 1/4](#releases) | [20](PROJECTS.md#scrapinghubfrontera) | [`c94beae`](https://github.com/scrapinghub/frontera/commit/c94beae2f438492139d24759729d0201779ccf1c) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 3/8](#linting) | [✅ 2/2](#documentation) | [❌ 2/4](#releases) | [19](PROJECTS.md#scrapinghubhcf-backend) | [`bbdc50c`](https://github.com/scrapinghub/hcf-backend/commit/bbdc50cd1d250742234aacc2d5da10c4fe4d9508) |
| **Data extraction** | | | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 3/6](#documentation) | [✅ 4/4](#releases) | [11](PROJECTS.md#zytedatazyte-parsers) | [`4f5d08d`](https://github.com/zytedata/zyte-parsers/commit/4f5d08d1be951fa438f0aedd598d61a61c360ea0) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌ 0/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [6](PROJECTS.md#zytedataclear-html) | [`6b820b1`](https://github.com/zytedata/clear-html/commit/6b820b13221145ceb0814e47e9583e5574d28865) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌ 0/3](#python-versions) | [❌ 6/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 5/8](#linting) | [✅ 2/2](#documentation) | [❌ 2/4](#releases) | [15](PROJECTS.md#zytedatahtml-text) | [`2dc4e94`](https://github.com/zytedata/html-text/commit/2dc4e94dd92a8b15476a237f0a1693b051f53d6f) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 3/4](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 8/10](#linting) | [✅ 2/2](#documentation) | [❌ 2/4](#releases) | [14](PROJECTS.md#scrapinghubprice-parser) | [`6718bfe`](https://github.com/scrapinghub/price-parser/commit/6718bfe8447f2de17ecc152d3ad2a4c51520c755) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌ 0/3](#python-versions) | [❌ 2/6](#packaging) | [✅ 2/2](#dependencies) | [❌ 2/3](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 7/11](#linting) | [❌ 3/6](#documentation) | [❌ 3/4](#releases) | [19](PROJECTS.md#scrapinghubdateparser) | [`ac08823`](https://github.com/scrapinghub/dateparser/commit/ac0882372d11a10e5f7d167ae9fa60be6e9c43a8) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 2/6](#linting) | [✅ 1/1](#documentation) | [❌ 1/4](#releases) | [19](PROJECTS.md#scrapinghubextruct) | [`dc3bf7d`](https://github.com/scrapinghub/extruct/commit/dc3bf7d2209ecf421222afc90d3d2dd8c6fd23cf) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌ 0/2](#python-versions) | [❌ 0/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 1/3](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 4/8](#linting) | [✅ 1/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapinghubnumber-parser) | [`a126357`](https://github.com/scrapinghub/number-parser/commit/a1263578628a7743054879095e50532fba1cdb67) |
| **Forms** | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 11/11](#linting) | [❌ 3/6](#documentation) | [✅ 4/4](#releases) | [11](PROJECTS.md#scrapyform2request) | [`a251597`](https://github.com/scrapy/form2request/commit/a251597d9fa44cbd03736ec1da37f85593dfe820) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌ 0/3](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 2/8](#linting) | [❌ 2/6](#documentation) | [❌ 2/4](#releases) | [23](PROJECTS.md#scrapinghubformasaurus) | [`4bb46a9`](https://github.com/scrapinghub/Formasaurus/commit/4bb46a95c7851622bb63ca7459d4d6d2587297ab) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [✅ 1/1](#dependencies) | [❌ 0/2](#typing) | [❌ 2/5](#tests-and-coverage) | [❌ 2/8](#linting) | [❌ 1/5](#documentation) | [❌ 1/4](#releases) | [23](PROJECTS.md#scrapinghubsklearn-crfsuite) | [`e18a02a`](https://github.com/scrapinghub/sklearn-crfsuite/commit/e18a02ae11b61f703c0ec460c44cfdd90db00591) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌ 0/3](#python-versions) | [❌ 0/6](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 0/5](#linting) | [❌ 3/6](#documentation) | [❌ 2/4](#releases) | [26](PROJECTS.md#scrapinghubpython-crfsuite) | [`c2eee32`](https://github.com/scrapinghub/python-crfsuite/commit/c2eee3267750c585d3ef5eebaf632d3ee7855249) |
| **Monitoring** | | | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌ 0/3](#python-versions) | [❌ 6/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 1/3](#typing) | [❌ 3/6](#tests-and-coverage) | [❌ 8/10](#linting) | [❌ 3/6](#documentation) | [❌ 3/4](#releases) | [15](PROJECTS.md#scrapinghubspidermon) | [`5bac6dd`](https://github.com/scrapinghub/spidermon/commit/5bac6dd768463ece308ca67dc9fd18525364c940) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌ 0/2](#python-versions) | [❌ 1/4](#packaging) | [❌ 0/1](#dependencies) | [❌ 0/2](#typing) | [❌ 1/5](#tests-and-coverage) | [❌ 0/3](#linting) | [❌ 0/1](#documentation) | [❌ 0/4](#releases) | [20](PROJECTS.md#scrapy-pluginszyte-spidermon) | [`8186fbe`](https://github.com/scrapy-plugins/zyte-spidermon/commit/8186fbe6d1c9233dc576ec725d3b2e046de032dd) |
| **AI agents** | | | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [➖](#linting) | [✅ 2/2](#documentation) | [✅ 1/1](#releases) | [0](PROJECTS.md#scrapyscrapy-agent-plugin) | [`d424e42`](https://github.com/scrapy/scrapy-agent-plugin/commit/d424e42a35116c108e986614b75ec7cd9cf9909e) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌ 2/3](#python-versions) | [✅ 7/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 3/4](#typing) | [❌ 3/5](#tests-and-coverage) | [✅ 9/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [4](PROJECTS.md#scrapyscrapy-mcp-official) | [`5530c67`](https://github.com/scrapy/scrapy-mcp-official/commit/5530c671a7078f4f06479422c623d10b846d3db9) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [✅ 2/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 10/11](#linting) | [❌ 7/8](#documentation) | [❌ 3/4](#releases) | [15](PROJECTS.md#zytedataagent-exam) | [`c88fec1`](https://github.com/zytedata/agent-exam/commit/c88fec170ff9683dad9d769601206088fdbaeb7d) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌ 0/3](#python-versions) | [❌ 4/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 7/9](#linting) | [✅ 2/2](#documentation) | [✅ 4/4](#releases) | [15](PROJECTS.md#zytedataclaude-measure-usage) | [`6b4310a`](https://github.com/zytedata/claude-measure-usage/commit/6b4310afeaf2e9c81acd861f8d9bd62006357bf7) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌ 1/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 0/2](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 0/4](#linting) | [✅ 1/1](#documentation) | [❌ 3/4](#releases) | [17](PROJECTS.md#zytedataharness-run) | [`4028849`](https://github.com/zytedata/harness-run/commit/4028849faf48ac448b1634140cfe3a9cac8f2749) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌ 2/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 1/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 7/9](#linting) | [✅ 2/2](#documentation) | [❌ 3/4](#releases) | [12](PROJECTS.md#scrapysphinx-llm-friendly) | [`2f5b77c`](https://github.com/scrapy/sphinx-llm-friendly/commit/2f5b77c315d5230429761063b475c7c1b015ca79) |
| **Maintenance** | | | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌ 0/3](#python-versions) | [❌ 5/7](#packaging) | [❌ 0/2](#dependencies) | [❌ 2/3](#typing) | [❌ 0/4](#tests-and-coverage) | [❌ 7/9](#linting) | [✅ 2/2](#documentation) | [❌ 3/4](#releases) | [15](PROJECTS.md#scrapysphinx-scrapy) | [`9231605`](https://github.com/scrapy/sphinx-scrapy/commit/9231605ac5f164edf053998ed9ba4b61b385f691) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#python-versions) | [➖](#packaging) | [➖](#dependencies) | [➖](#typing) | [➖](#tests-and-coverage) | [❌ 6/7](#linting) | [✅ 2/2](#documentation) | [✅ 1/1](#releases) | [1](PROJECTS.md#scrapyunattended-pr-guard) | [`1e3c311`](https://github.com/scrapy/unattended-pr-guard/commit/1e3c31134253813934af43f3505d4492eee26c2a) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [❌ 1/2](#python-versions) | [✅ 4/4](#packaging) | [➖](#dependencies) | [❌ 0/1](#typing) | [❌ 0/4](#tests-and-coverage) | [✅ 9/9](#linting) | [➖](#documentation) | [➖](#releases) | [6](PROJECTS.md#zytedatazyte-oss-maintenance) | [`23e650e`](https://github.com/zytedata/zyte-oss-maintenance/commit/23e650ea1131a05a10c22f83b67d7c533ea93844) |

## Release candidates

Projects with commits since their latest release, oldest release first.

- [scrapinghub/frontera](https://github.com/scrapinghub/frontera): 0.8.1 (2019-04-05)
- [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): 0.3.2 (2023-03-28)
- [scrapy/xtractmime](https://github.com/scrapy/xtractmime): 0.2.1 (2024-01-16)
- [scrapy/form2request](https://github.com/scrapy/form2request): 0.2.0 (2024-07-15)
- [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): 0.2.0 (2024-09-26)
- [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): 2024.11.5 (2024-11-05)
- [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): 0.10.0 (2024-11-07)
- [scrapinghub/extruct](https://github.com/scrapinghub/extruct): 0.18.0 (2024-11-08)
- [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): 0.3.0 (2024-12-30)
- [zytedata/url-matcher](https://github.com/zytedata/url-matcher): 0.6.0 (2025-02-14)
- [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): 2.4.1 (2025-03-24)
- [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): 0.3.0 (2025-06-06)
- [zytedata/html-text](https://github.com/zytedata/html-text): 0.7.1 (2025-10-06)
- [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): 0.6.0 (2025-10-24)
- [zytedata/clear-html](https://github.com/zytedata/clear-html): 0.5.0 (2025-10-24)
- [scrapy/itemadapter](https://github.com/scrapy/itemadapter): 0.13.1 (2026-01-08)
- [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): 0.1.1 (2026-01-27)
- [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): 0.18.1 (2026-01-28)
- [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): 0.5.1 (2026-03-19)
- [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): 0.27.2 (2026-04-28)
- [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): 0.24.1 (2026-04-28)
- [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): 0.18.1 (2026-06-29)
- [scrapinghub/shub](https://github.com/scrapinghub/shub): 2.18.1 (2026-07-08)
- [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): 0.0.48 (2026-07-10)
- [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): 0.11.0 (2026-07-23)
- [scrapy/formerly](https://github.com/scrapy/formerly): 0.1.0 (2026-08-05)
- [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): 1.27.0 (2026-08-10)
- [zytedata/agent-exam](https://github.com/zytedata/agent-exam): 0.2.0 (2026-08-17)
- [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): 0.36.0 (2026-08-20)
- [scrapy/queuelib](https://github.com/scrapy/queuelib): 1.10.0 (2026-08-24)
- [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): 1.4.3 (2026-09-03)
- [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): 0.1.2 (2026-09-07)
- [scrapy/scrapy](https://github.com/scrapy/scrapy): 2.19.0 (2026-09-10)
- [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): 0.5.1 (2026-09-11)
- [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): 0.1.1 (2026-09-14)
- [scrapinghub/andi](https://github.com/scrapinghub/andi): 0.9.0 (2026-09-17)
- [scrapy/protego](https://github.com/scrapy/protego): 0.7.0 (2026-09-21)
- [scrapy/frostwork](https://github.com/scrapy/frostwork): 0.1.6 (2026-09-23)
- [zytedata/harness-run](https://github.com/zytedata/harness-run): 0.4.0 (2026-09-23)
- [scrapy/parsel](https://github.com/scrapy/parsel): 1.12.1 (2026-09-28)
- [scrapy/itemloaders](https://github.com/scrapy/itemloaders): 1.5.0 (2026-09-29)
- [scrapy/w3lib](https://github.com/scrapy/w3lib): 2.5.0 (2026-09-30)
- [scrapy/cssselect](https://github.com/scrapy/cssselect): 1.6.0 (2026-10-09)

## Python versions

| Check | Statement | Results |
| --- | --- | --- |
| [`no-eol-python`](#no-eol-python) | Support for end-of-life Python versions is dropped. | 14/60 passing |
| [`latest-python`](#latest-python) | The latest stable Python version is declared as supported and tested in CI. | 17/60 passing |
| [`unreleased-python`](#unreleased-python) | The upcoming Python version is tested in CI, once it has a release candidate. | 0/0 passing |
| [`python-classifiers`](#python-classifiers) | Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes. | 17/52 passing |
| [`supports-pypy`](#supports-pypy) | The project supports PyPy: it has the PyPy classifier or tests PyPy in CI. | 12/60 yes |
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
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| **Scrapy plugins** | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy tools** | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Feed exporters** | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **scrapy-poet and its deps** | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Zyte API** | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Scrapy Cloud** | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | yes | [❌](#latest-pypy) | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Data extraction** | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Forms** | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Monitoring** | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **AI agents** | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#no-eol-python) | ✅ | [➖](#unreleased-python) | ✅ | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| **Maintenance** | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#no-eol-python) | [❌](#latest-python) | [➖](#unreleased-python) | [❌](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#no-eol-python) | [➖](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | [➖](#supports-pypy) | [➖](#latest-pypy) | [➖](#no-eol-pypy) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | [❌](#latest-python) | [➖](#unreleased-python) | [➖](#python-classifiers) | no | [➖](#latest-pypy) | [➖](#no-eol-pypy) |

### no-eol-python

Support for end-of-life Python versions is dropped.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/protego](https://github.com/scrapy/protego): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): requires-python is not declared
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01)
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): requires-python is not declared
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01)
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): requires-python is not declared
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): requires-python is not declared
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): requires-python '>=3.8' allows 3.8 (EOL 2024-10-07), 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.8, 3.9, 3.10
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): requires-python is not declared
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): requires-python '>=3.9' allows 3.9 (EOL 2025-10-31), 3.10 (EOL 2026-10-01); classifiers list 3.9, 3.10
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): requires-python is not declared
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): requires-python is not declared
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): requires-python '>=3.10' allows 3.10 (EOL 2026-10-01); classifiers list 3.10
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### latest-python

The latest stable Python version is declared as supported and tested in CI.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no 'Programming Language :: Python :: 3.15' classifier
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no 'Programming Language :: Python :: 3.15' classifier; 3.15 not found in CI workflows or tox config
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no 'Programming Language :: Python :: 3.15' classifier
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### unreleased-python

The upcoming Python version is tested in CI, once it has a release candidate.

- ➖ No upcoming Python version has a release candidate. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/parsel](https://github.com/scrapy/parsel), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### python-classifiers

Python version classifiers match requires-python: there is one for every supported Python version it allows, and none for versions it excludes.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no classifiers for 3.15
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no classifiers for 3.14, 3.15
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no classifiers for 3.14, 3.15
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no classifiers for 3.14, 3.15
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no classifiers for 3.15
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no classifiers for 3.14, 3.15
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no Python version classifiers
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no classifiers for 3.15
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no classifiers for 3.15
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no classifiers for 3.15
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no classifiers for 3.14, 3.15
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no Python version classifiers
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no classifiers for 3.15
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no classifiers for 3.15
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no classifiers for 3.15
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no classifiers for 3.15
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no classifiers for 3.15
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no classifiers for 3.15
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no classifiers for 3.13, 3.14, 3.15
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no classifiers for 3.15
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no classifiers for 3.15
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no classifiers for 3.15
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no classifiers for 3.15
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no classifiers for 3.14, 3.15
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no classifiers for 3.15
- ➖ requires-python is not declared. [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### supports-pypy

The project supports PyPy: it has the PyPy classifier or tests PyPy in CI.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

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
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): PyPy 3.12 not found in CI workflows or tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): PyPy 3.12 not found in CI workflows or tox config
- ➖ Does not support PyPy. [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-eol-pypy

End-of-life PyPy versions are not tested in CI.

- ➖ Does not support PyPy. [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Packaging

| Check | Statement | Results |
| --- | --- | --- |
| [`pyproject-metadata`](#pyproject-metadata) | Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg. | 42/60 passing |
| [`no-legacy-config`](#no-legacy-config) | There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini. | 39/60 passing |
| [`license`](#license) | The license: the license field of package metadata, or else the license classifiers. | BSD-3-Clause (22), BSD License (12), Apache-2.0 (11), no (6), MIT License (4), MIT (3), Apache Software License (2) |
| [`pep639-license`](#pep639-license) | The license is declared as an SPDX expression (PEP 639), without license classifiers. | 30/44 passing |
| [`hatchling`](#hatchling) | The build backend is hatchling. | 34/59 passing |
| [`sdist-contents`](#sdist-contents) | The sdist includes only listed files, which include the tests, the docs and the tox configuration. | 27/33 passing |
| [`project-urls`](#project-urls) | [project.urls] links to the source, the issue tracker, the changelog and, if there are Sphinx docs, the documentation, with labels that PyPI recognizes. | 22/43 passing |
| [`twine-check`](#twine-check) | `twine check` validates the built distributions in tox. | 35/58 passing |

| Project | [pyproject-metadata](#pyproject-metadata) | [no-legacy-config](#no-legacy-config) | [license](#license) | [pep639-license](#pep639-license) | [hatchling](#hatchling) | [sdist-contents](#sdist-contents) | [project-urls](#project-urls) | [twine-check](#twine-check) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | [❌](#sdist-contents) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Scrapy plugins** | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#no-legacy-config) | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#no-legacy-config) | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#no-legacy-config) | MIT License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| **Scrapy tools** | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Feed exporters** | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | ✅ | Apache Software License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | ✅ | ✅ | no | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ | BSD License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| **scrapy-poet and its deps** | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | [❌](#no-legacy-config) | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | ✅ | Apache-2.0 | ✅ | [➖](#hatchling) | [➖](#sdist-contents) | ✅ | [➖](#twine-check) |
| **Zyte API** | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | BSD License | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#no-legacy-config) | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | [❌](#twine-check) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#pyproject-metadata) | ✅ | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | Apache Software License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **Data extraction** | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | MIT | ✅ | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | ✅ | [❌](#project-urls) | [❌](#twine-check) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD-3-Clause | ✅ | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | BSD License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **Forms** | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | ✅ | [❌](#project-urls) | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | ✅ |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#pyproject-metadata) | [❌](#no-legacy-config) | MIT License | [❌](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| **Monitoring** | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | BSD-3-Clause | [❌](#pep639-license) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#pyproject-metadata) | ✅ | no | [➖](#pep639-license) | [❌](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [❌](#twine-check) |
| **AI agents** | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | Apache-2.0 | [❌](#pep639-license) | ✅ | [❌](#sdist-contents) | [❌](#project-urls) | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [❌](#sdist-contents) | [❌](#project-urls) | [❌](#twine-check) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | MIT | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| **Maintenance** | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | BSD-3-Clause | ✅ | ✅ | [❌](#sdist-contents) | ✅ | [❌](#twine-check) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#pyproject-metadata) | [➖](#no-legacy-config) | [➖](#license) | [➖](#pep639-license) | [➖](#hatchling) | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | ✅ | Apache-2.0 | ✅ | ✅ | [➖](#sdist-contents) | [➖](#project-urls) | [➖](#twine-check) |

### pyproject-metadata

Package metadata is in the [project] table of pyproject.toml, with no setup.py and no setuptools configuration in setup.cfg.

- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata], [bdist_wheel]
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel], [sdist_dsc]
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [metadata]
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no [project] table in pyproject.toml; setup.py exists
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): setup.py exists
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [wheel]
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no [project] table in pyproject.toml; setup.py exists; setup.cfg has setuptools sections: [bdist_wheel]
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): setup.py exists
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [project] table in pyproject.toml; setup.py exists
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### no-legacy-config

There are no legacy configuration files, e.g. .coveragerc, pytest.ini, .flake8 or requirements-dev.txt, and no tool configuration in setup.cfg or tox.ini.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): legacy files: pylintrc; tool sections in setup.cfg: [flake8]
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): tool sections in tox.ini: [pytest]
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): legacy files: .coveragerc, .flake8
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): tool sections in setup.cfg: [flake8]
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): legacy files: requirements-dev.txt
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): legacy files: requirements-dev.txt
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): legacy files: requirements-dev.txt
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): legacy files: .bandit.yml, .flake8, .isort.cfg; tool sections in setup.cfg: [mypy], [mypy-pytest.*], [mypy-scrapy.*], [mypy-twisted.*], [mypy-w3lib.*]
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): legacy files: requirements-dev.txt
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): legacy files: pytest.ini
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): tool sections in setup.cfg: [flake8]
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): tool sections in setup.cfg: [flake8], [tool:pytest], [coverage:run]
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): legacy files: .flake8
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): legacy files: .coveragerc; tool sections in tox.ini: [flake8], [pytest]
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): legacy files: .flake8
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): legacy files: .coveragerc, pytest.ini
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): legacy files: .coveragerc, .isort.cfg, pytest.ini, requirements-dev.txt
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): legacy files: .coveragerc
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): legacy files: .coveragerc, .flake8; tool sections in setup.cfg: [isort]
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): legacy files: .coveragerc, .flake8
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): legacy files: .flake8
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### license

The license: the license field of package metadata, or else the license classifiers.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pep639-license

The license is declared as an SPDX expression (PEP 639), without license classifiers.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no license field
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): has license classifiers: License :: OSI Approved :: Apache Software License
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): license is a table, not an SPDX expression; has license classifiers: License :: OSI Approved :: MIT License
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): has license classifiers: License :: OSI Approved :: BSD License
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): has license classifiers: License :: OSI Approved :: Apache Software License
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### hatchling

The build backend is hatchling.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): build backend is setuptools.build_meta
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): build backend is setuptools.build_meta
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no pyproject.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no build-backend in pyproject.toml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no build-backend in pyproject.toml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no build-backend in pyproject.toml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no build-backend in pyproject.toml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no pyproject.toml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no build-backend in pyproject.toml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): build backend is setuptools.build_meta
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no build-backend in pyproject.toml
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no build-backend in pyproject.toml
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): build backend is setuptools.build_meta
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no pyproject.toml
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): build backend is setuptools.build_meta
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no pyproject.toml
- ➖ Rust extension, built with maturin. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### sdist-contents

The sdist includes only listed files, which include the tests, the docs and the tox configuration.

- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): not included: tox.ini
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no include in [tool.hatch.build.targets.sdist]
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): not included: docs, tox.ini
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no include in [tool.hatch.build.targets.sdist]
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): not included: tox.ini
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no include in [tool.hatch.build.targets.sdist]
- ➖ The build backend is not hatchling. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### project-urls

[project.urls] links to the source, the issue tracker, the changelog and, if there are Sphinx docs, the documentation, with labels that PyPI recognizes.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): missing URLs: issues, changelog, documentation
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): missing URLs: issues, changelog
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing URLs: issues, changelog, documentation
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing URLs: issues, changelog
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing URLs: issues, changelog
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing URLs: documentation
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing URLs: changelog
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no [project.urls] table
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing URLs: issues, changelog
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): missing URLs: changelog
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing URLs: issues, changelog
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): missing URLs: issues, changelog
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing URLs: issues, changelog
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing URLs: changelog
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing URLs: issues, changelog
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing URLs: changelog
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing URLs: issues, documentation
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): missing URLs: issues, changelog
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): missing URLs: issues, changelog, documentation
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): missing URLs: issues
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): missing URLs: changelog
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### twine-check

`twine check` validates the built distributions in tox.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): twine check runs in a workflow, not in tox
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no twine check in tox config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no twine check in tox config
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): twine check runs in a workflow, not in tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no twine check in tox config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no twine check in tox config
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no twine check in tox config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no twine check in tox config
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no twine check in tox config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no twine check in tox config
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no twine check in tox config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no twine check in tox config
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no twine check in tox config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no twine check in tox config
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): twine check runs in a workflow, not in tox
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): twine check runs in a workflow, not in tox
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no twine check in tox config
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no twine check in tox config
- ➖ Wheels are built per platform by maturin in CI, where twine check runs on them. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Dependencies

| Check | Statement | Results |
| --- | --- | --- |
| [`dependency-lower-bounds`](#dependency-lower-bounds) | Every runtime dependency has a lower bound. | 25/33 passing |
| [`min-deps-env`](#min-deps-env) | A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it). | 30/51 passing |

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
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| **Scrapy plugins** | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| **Scrapy tools** | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ |
| **Feed exporters** | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ |
| **scrapy-poet and its deps** | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#min-deps-env) |
| **Zyte API** | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [➖](#dependency-lower-bounds) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ |
| **Scrapy Cloud** | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#dependency-lower-bounds) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [➖](#dependency-lower-bounds) | ✅ |
| **Data extraction** | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#min-deps-env) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Forms** | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [➖](#dependency-lower-bounds) | ✅ |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **Monitoring** | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [➖](#dependency-lower-bounds) | [❌](#min-deps-env) |
| **AI agents** | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#min-deps-env) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#dependency-lower-bounds) | ✅ |
| **Maintenance** | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#dependency-lower-bounds) | [❌](#min-deps-env) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#dependency-lower-bounds) | [➖](#min-deps-env) |

### dependency-lower-bounds

Every runtime dependency has a lower bound.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no lower bound: packaging, tldextract
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no lower bound: google-api-python-client, google-auth, scrapy
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no lower bound: click, docker, importlib-metadata, packaging, pip, PyYAML, requests, retrying, setuptools, toml
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no lower bound: html-text, lxml, parsel, six, w3lib
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no lower bound: lxml, lxml-html-clean
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no lower bound: google-cloud-storage, google-auth, packaging, pyyaml, jsonschema
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no lower bound: docutils, tabulate
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no lower bound: docutils, packaging, sphinx-copybutton, sphinx-design, sphinx-sitemap, sphinxcontrib-youtube, tomli
- ➖ No runtime dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite)
- ➖ No [project] table in pyproject.toml. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### min-deps-env

A tox environment tests the minimum versions of dependencies (its name has min, minimum, lowest or pinned in it).

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no tox environment for minimum dependency versions
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment for minimum dependency versions
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no tox environment for minimum dependency versions
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no tox environment for minimum dependency versions
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no tox environment for minimum dependency versions
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no tox environment for minimum dependency versions
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no tox environment for minimum dependency versions
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no tox environment for minimum dependency versions
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no tox environment for minimum dependency versions
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no tox environment for minimum dependency versions
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no tox environment for minimum dependency versions
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no tox environment for minimum dependency versions
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no tox environment for minimum dependency versions
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment for minimum dependency versions
- ➖ No dependencies. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/andi](https://github.com/scrapinghub/andi)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Typing

| Check | Statement | Results |
| --- | --- | --- |
| [`py-typed`](#py-typed) | The package ships type hints (a py.typed marker). | 28/59 passing |
| [`typed-classifier`](#typed-classifier) | A package with a py.typed marker has the 'Typing :: Typed' classifier. | 3/28 passing |
| [`mypy`](#mypy) | mypy runs in tox, CI workflows or pre-commit. | 38/59 passing |
| [`mypy-strict`](#mypy-strict) | mypy runs in strict mode: strict = true in its config, or --strict. | 23/38 passing |

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
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| **Scrapy plugins** | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| **Scrapy tools** | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| **Feed exporters** | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **scrapy-poet and its deps** | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | ✅ | [❌](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| **Zyte API** | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | [❌](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| **Scrapy Cloud** | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | ✅ | [❌](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **Data extraction** | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| **Forms** | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **Monitoring** | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | [❌](#mypy-strict) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| **AI agents** | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | [❌](#typed-classifier) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| **Maintenance** | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#py-typed) | [➖](#typed-classifier) | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#py-typed) | [➖](#typed-classifier) | [➖](#mypy) | [➖](#mypy-strict) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#py-typed) | [➖](#typed-classifier) | [❌](#mypy) | [➖](#mypy-strict) |

### py-typed

The package ships type hints (a py.typed marker).

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no py.typed file
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no py.typed file
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no py.typed file
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no py.typed file
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no py.typed file
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no py.typed file
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no py.typed file
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no py.typed file
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no py.typed file
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no py.typed file
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no py.typed file
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no py.typed file
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no py.typed file
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no py.typed file
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no py.typed file
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no py.typed file
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no py.typed file
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no py.typed file
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no py.typed file
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no py.typed file
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no py.typed file
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no py.typed file
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no py.typed file
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no py.typed file
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no py.typed file
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### typed-classifier

A package with a py.typed marker has the 'Typing :: Typed' classifier.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): no 'Typing :: Typed' classifier
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no 'Typing :: Typed' classifier
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no 'Typing :: Typed' classifier
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no 'Typing :: Typed' classifier
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no 'Typing :: Typed' classifier
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no 'Typing :: Typed' classifier
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no 'Typing :: Typed' classifier
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no 'Typing :: Typed' classifier
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no 'Typing :: Typed' classifier
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no 'Typing :: Typed' classifier
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no 'Typing :: Typed' classifier
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no 'Typing :: Typed' classifier
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no 'Typing :: Typed' classifier
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no 'Typing :: Typed' classifier
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no 'Typing :: Typed' classifier
- ➖ No py.typed file. [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### mypy

mypy runs in tox, CI workflows or pre-commit.

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): mypy not found
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): mypy not found
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): mypy not found
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): mypy not found
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): mypy not found
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): mypy not found
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): mypy not found
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): mypy not found
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): mypy not found
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): mypy not found
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): mypy not found
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): mypy not found
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): mypy not found
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): mypy not found
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): mypy not found
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): mypy not found
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): mypy not found
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): mypy not found
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): mypy not found
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): mypy not found
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): mypy not found
- ➖ Runs mypy through make py, in CI. [scrapy/frostwork](https://github.com/scrapy/frostwork)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### mypy-strict

mypy runs in strict mode: strict = true in its config, or --strict.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no strict = true in mypy config, and no --strict
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no strict = true in mypy config, and no --strict
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no strict = true in mypy config, and no --strict
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no strict = true in mypy config, and no --strict
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no strict = true in mypy config, and no --strict
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no strict = true in mypy config, and no --strict
- ➖ Does not run mypy. [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Tests and coverage

| Check | Statement | Results |
| --- | --- | --- |
| [`codecov`](#codecov) | Test coverage is uploaded to Codecov in CI workflows. | 44/60 passing |
| [`codecov-test-results`](#codecov-test-results) | Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results). | 14/60 passing |
| [`codecov-status`](#codecov-status) | The Codecov config disables the patch status and sets a 100% target for the project status. | 6/44 passing |
| [`branch-coverage`](#branch-coverage) | Branch coverage is enabled. | 31/60 passing |
| [`warnings-as-errors`](#warnings-as-errors) | pytest turns warnings into errors: "error" in filterwarnings, or -W error. | 8/60 passing |
| [`scrapy-master`](#scrapy-master) | CI tests against Scrapy installed from its master branch. | 2/21 passing |

| Project | [codecov](#codecov) | [codecov-test-results](#codecov-test-results) | [codecov-status](#codecov-status) | [branch-coverage](#branch-coverage) | [warnings-as-errors](#warnings-as-errors) | [scrapy-master](#scrapy-master) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | [❌](#codecov-status) | ✅ | ✅ | [➖](#scrapy-master) |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | [❌](#codecov-status) | ✅ | ✅ | [➖](#scrapy-master) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy plugins** | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy tools** | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | ✅ | [❌](#scrapy-master) |
| **Feed exporters** | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| **scrapy-poet and its deps** | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Zyte API** | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | [❌](#codecov-test-results) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Scrapy Cloud** | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [❌](#scrapy-master) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Data extraction** | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | ✅ | [➖](#scrapy-master) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Forms** | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Monitoring** | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | ✅ | ✅ | [❌](#scrapy-master) |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | ✅ | [❌](#codecov-test-results) | [❌](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **AI agents** | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#codecov-status) | [➖](#branch-coverage) | [➖](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | [❌](#codecov-status) | ✅ | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| **Maintenance** | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#codecov) | [➖](#codecov-test-results) | [➖](#codecov-status) | [➖](#branch-coverage) | [➖](#warnings-as-errors) | [➖](#scrapy-master) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [❌](#codecov) | [❌](#codecov-test-results) | [➖](#codecov-status) | [❌](#branch-coverage) | [❌](#warnings-as-errors) | [➖](#scrapy-master) |

### codecov

Test coverage is uploaded to Codecov in CI workflows.

- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no codecov/codecov-action step for coverage
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no codecov/codecov-action step for coverage
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no codecov/codecov-action step for coverage
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no codecov/codecov-action step for coverage
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no codecov/codecov-action step for coverage
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step for coverage
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step for coverage
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step for coverage
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step for coverage
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no codecov/codecov-action step for coverage
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-test-results

Test results are uploaded to Codecov in CI workflows (codecov/codecov-action with report_type: test_results).

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no codecov/codecov-action step with report_type: test_results
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no codecov/codecov-action step with report_type: test_results
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no codecov/codecov-action step with report_type: test_results
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### codecov-status

The Codecov config disables the patch status and sets a 100% target for the project status.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no Codecov config
- ❌ [scrapy/formerly](https://github.com/scrapy/formerly): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no Codecov config
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no Codecov config
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no Codecov config
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no Codecov config
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no Codecov config
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no Codecov config
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no Codecov config
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no Codecov config
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no Codecov config
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no Codecov config
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no Codecov config
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): patch status not disabled, project status target not 100% in .codecov.yml
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no Codecov config
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no Codecov config
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no Codecov config
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no Codecov config
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no Codecov config
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no Codecov config
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no Codecov config
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no Codecov config
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no Codecov config
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no Codecov config
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): patch status not disabled, project status target not 100% in codecov.yml
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no Codecov config
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no Codecov config
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no Codecov config
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no Codecov config
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no Codecov config
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no Codecov config
- ➖ Coverage is not uploaded to Codecov. [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### branch-coverage

Branch coverage is enabled.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no branch = true in coverage config, and no --cov-branch
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no branch = true in coverage config, and no --cov-branch
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no branch = true in coverage config, and no --cov-branch
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### warnings-as-errors

pytest turns warnings into errors: "error" in filterwarnings, or -W error.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/protego](https://github.com/scrapy/protego): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/queuelib](https://github.com/scrapy/queuelib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/andi](https://github.com/scrapinghub/andi): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/clear-html](https://github.com/zytedata/clear-html): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no "error" in pytest filterwarnings, and no -W error
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no "error" in pytest filterwarnings, and no -W error
- ❌ [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance): no "error" in pytest filterwarnings, and no -W error
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### scrapy-master

CI tests against Scrapy installed from its master branch.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no CI workflow or tox environment installs Scrapy master
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no CI workflow or tox environment installs Scrapy master
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no CI workflow or tox environment installs Scrapy master
- ➖ Does not depend on Scrapy. [scrapy/scrapy](https://github.com/scrapy/scrapy), [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/parsel](https://github.com/scrapy/parsel), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

## Linting

| Check | Statement | Results |
| --- | --- | --- |
| [`ruff`](#ruff) | ruff-check and ruff-format are used, instead of tools that ruff replaces. | 39/60 passing |
| [`ruff-rules`](#ruff-rules) | ruff enables rules beyond its defaults, with select or extend-select. | 36/40 passing |
| [`pylint`](#pylint) | A tox environment runs pylint. | 10/60 yes |
| [`pre-commit-in-ci`](#pre-commit-in-ci) | pre-commit runs in CI workflows, directly or through tox, or in pre-commit.ci. | 45/49 passing |
| [`pre-commit-tox`](#pre-commit-tox) | A tox environment runs pre-commit on all files. | 37/49 passing |
| [`pre-commit-hooks`](#pre-commit-hooks) | The hooks of https://github.com/pre-commit/pre-commit-hooks are used. | 35/49 passing |
| [`pre-commit-updates`](#pre-commit-updates) | The ruff and zizmor pre-commit hooks are updated within 180 days of a new release. | 30/41 passing |
| [`actionlint`](#actionlint) | GitHub Actions workflows are linted with actionlint. | 27/56 passing |
| [`zizmor`](#zizmor) | GitHub Actions workflows are audited with zizmor. | 30/56 passing |
| [`dependabot`](#dependabot) | Dependabot updates GitHub Actions, which zizmor requires pinning. | 28/30 passing |
| [`pr-guard-trusted-users`](#pr-guard-trusted-users) | The trusted-users of scrapy/unattended-pr-guard include no public members of its trusted-orgs, which it trusts already. | 2/4 passing |
| [`has-sphinx-docs`](#has-sphinx-docs) | The project has Sphinx docs (docs/conf.py). | 25/62 yes |
| [`blacken-docs`](#blacken-docs) | Code examples in the docs are formatted with blacken-docs. | 17/25 passing |
| [`sphinx-lint`](#sphinx-lint) | The docs are linted with sphinx-lint. | 17/25 passing |

| Project | [ruff](#ruff) | [ruff-rules](#ruff-rules) | [pylint](#pylint) | [pre-commit-in-ci](#pre-commit-in-ci) | [pre-commit-tox](#pre-commit-tox) | [pre-commit-hooks](#pre-commit-hooks) | [pre-commit-updates](#pre-commit-updates) | [actionlint](#actionlint) | [zizmor](#zizmor) | [dependabot](#dependabot) | [pr-guard-trusted-users](#pr-guard-trusted-users) | [has-sphinx-docs](#has-sphinx-docs) | [blacken-docs](#blacken-docs) | [sphinx-lint](#sphinx-lint) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | [❌](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | yes | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | ✅ | [❌](#ruff-rules) | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy plugins** | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [❌](#ruff) | [➖](#ruff-rules) | yes | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Scrapy tools** | | | | | | | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | ✅ | ✅ | yes | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| **Feed exporters** | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **scrapy-poet and its deps** | | | | | | | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | ✅ | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | [❌](#actionlint) | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Zyte API** | | | | | | | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | no | [❌](#pre-commit-in-ci) | ✅ | ✅ | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | [❌](#ruff) | [➖](#ruff-rules) | no | [❌](#pre-commit-in-ci) | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | ✅ | [❌](#ruff-rules) | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Data extraction** | | | | | | | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/html-text](https://github.com/zytedata/html-text) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | ✅ | ✅ | no | ✅ | ✅ | ✅ | [❌](#pre-commit-updates) | [❌](#actionlint) | ✅ | ✅ | ✅ | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | ✅ | ✅ | no | ✅ | ✅ | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | [❌](#pre-commit-hooks) | ✅ | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Forms** | | | | | | | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#ruff) | [➖](#ruff-rules) | no | ✅ | ✅ | [❌](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | [❌](#blacken-docs) | [❌](#sphinx-lint) |
| **Monitoring** | | | | | | | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [❌](#ruff) | [➖](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **AI agents** | | | | | | | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [➖](#actionlint) | [➖](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [❌](#dependabot) | [➖](#pr-guard-trusted-users) | yes | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | ✅ | [❌](#ruff-rules) | no | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [❌](#ruff) | [❌](#ruff-rules) | no | [➖](#pre-commit-in-ci) | [➖](#pre-commit-tox) | [➖](#pre-commit-hooks) | [➖](#pre-commit-updates) | [❌](#actionlint) | [❌](#zizmor) | [➖](#dependabot) | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| **Maintenance** | | | | | | | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | ✅ | ✅ | no | ✅ | [❌](#pre-commit-tox) | ✅ | [❌](#pre-commit-updates) | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#ruff) | [➖](#ruff-rules) | [➖](#pylint) | ✅ | [❌](#pre-commit-tox) | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | ✅ | ✅ | no | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | [➖](#pr-guard-trusted-users) | no | [➖](#blacken-docs) | [➖](#sphinx-lint) |

### ruff

ruff-check and ruff-format are used, instead of tools that ruff replaces.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no .pre-commit-config.yaml
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: ruff-check, ruff-format
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, isort, pyupgrade
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: ruff-check, ruff-format; pre-commit still runs black, flake8, isort, pyupgrade
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### ruff-rules

ruff enables rules beyond its defaults, with select or extend-select.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): only the default rules are enabled
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): only the default rules are enabled
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): only the default rules are enabled
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): only the default rules are enabled
- ➖ Does not use ruff. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon)
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pylint

A tox environment runs pylint.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)

### pre-commit-in-ci

pre-commit runs in CI workflows, directly or through tox, or in pre-commit.ci.

- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): not run in CI workflows or tox
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): tox environments that run pre-commit are not run in CI: pre-commit
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): not run in CI workflows or tox
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): not run in CI workflows or tox
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-tox

A tox environment runs pre-commit on all files.

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): no tox environment runs pre-commit run --all-files
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no tox environment runs pre-commit run --all-files
- ❌ [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): no tox environment runs pre-commit run --all-files
- ❌ [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard): no tox environment runs pre-commit run --all-files
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-hooks

The hooks of https://github.com/pre-commit/pre-commit-hooks are used.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy/frostwork](https://github.com/scrapy/frostwork): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): https://github.com/pre-commit/pre-commit-hooks is not used
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): https://github.com/pre-commit/pre-commit-hooks is not used
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)

### pre-commit-updates

The ruff and zizmor pre-commit hooks are updated within 180 days of a new release.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): outdated: ruff v0.11.2 (0.15.11 or later expected)
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): outdated: ruff v0.12.5 (0.15.11 or later expected)
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): outdated: ruff v0.8.4 (0.15.11 or later expected)
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): outdated: ruff v0.9.3 (0.15.11 or later expected)
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): outdated: ruff v0.15.6 (0.15.11 or later expected)
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): outdated: ruff v0.9.4 (0.15.11 or later expected)
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): outdated: ruff v0.11.12 (0.15.11 or later expected)
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): outdated: ruff v0.13.2 (0.15.11 or later expected)
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): outdated: ruff v0.11.13 (0.15.11 or later expected)
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): outdated: ruff v0.11.13 (0.15.11 or later expected)
- ➖ No .pre-commit-config.yaml. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ No checked hooks. [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite)

### actionlint

GitHub Actions workflows are linted with actionlint.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: actionlint
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: actionlint
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): missing pre-commit hooks: actionlint
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: actionlint
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): missing pre-commit hooks: actionlint
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: actionlint
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### zizmor

GitHub Actions workflows are audited with zizmor.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): no .pre-commit-config.yaml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: zizmor
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): missing pre-commit hooks: zizmor
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): missing pre-commit hooks: zizmor
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): no .pre-commit-config.yaml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no .pre-commit-config.yaml
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no .pre-commit-config.yaml
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): missing pre-commit hooks: zizmor
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: zizmor
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): missing pre-commit hooks: zizmor
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no .pre-commit-config.yaml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no .pre-commit-config.yaml
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### dependabot

Dependabot updates GitHub Actions, which zizmor requires pinning.

- ❌ [scrapy/xtractmime](https://github.com/scrapy/xtractmime): no .github/dependabot.yml
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): no .github/dependabot.yml
- ➖ Does not use zizmor. [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ No GitHub Actions workflows. [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)

### pr-guard-trusted-users

The trusted-users of scrapy/unattended-pr-guard include no public members of its trusted-orgs, which it trusts already.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): public members of trusted orgs: kishan3
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): public members of trusted orgs: kishan3
- ➖ Does not use scrapy/unattended-pr-guard. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint), [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet), [zytedata/url-matcher](https://github.com/zytedata/url-matcher), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api), [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items), [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub), [scrapinghub/shub](https://github.com/scrapinghub/shub), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/agent-exam](https://github.com/zytedata/agent-exam), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### has-sphinx-docs

The project has Sphinx docs (docs/conf.py).

Nothing to report.

### blacken-docs

Code examples in the docs are formatted with blacken-docs.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: blacken-docs
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: blacken-docs
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-lint

The docs are linted with sphinx-lint.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): missing pre-commit hooks: sphinx-lint
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): missing pre-commit hooks: sphinx-lint
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .pre-commit-config.yaml
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Documentation

| Check | Statement | Results |
| --- | --- | --- |
| [`docs-requirements-in`](#docs-requirements-in) | Sphinx docs requirements are defined in docs/requirements.in. | 10/25 passing |
| [`sphinx-scrapy`](#sphinx-scrapy) | Sphinx docs use sphinx-scrapy. | 13/25 passing |
| [`sphinx-scrapy-pins`](#sphinx-scrapy-pins) | sphinx-scrapy is pinned to the same version in the tox requires, the docs requirements and the pre-commit hook rev. | 10/13 passing |
| [`sphinx-scrapy-latest`](#sphinx-scrapy-latest) | sphinx-scrapy is pinned to its latest release. | 0/13 passing |
| [`readthedocs`](#readthedocs) | Sphinx docs are built on Read the Docs (.readthedocs.yml), and the README links to them. | 22/25 passing |
| [`docs-stable-links`](#docs-stable-links) | Links to the docs in the README and in [project.urls] that name a version use stable, which is built from the latest release. | 12/24 passing |
| [`changelog`](#changelog) | There is a changelog, e.g. CHANGES.rst, CHANGELOG.md, NEWS or docs/news.rst. | 53/61 passing |
| [`changelog-date`](#changelog-date) | bump-my-version replaces (unreleased) in the changelog with the release date. | 43/46 passing |

| Project | [docs-requirements-in](#docs-requirements-in) | [sphinx-scrapy](#sphinx-scrapy) | [sphinx-scrapy-pins](#sphinx-scrapy-pins) | [sphinx-scrapy-latest](#sphinx-scrapy-latest) | [readthedocs](#readthedocs) | [docs-stable-links](#docs-stable-links) | [changelog](#changelog) | [changelog-date](#changelog-date) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Scrapy plugins** | | | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | [❌](#changelog-date) |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| **Scrapy tools** | | | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| **Feed exporters** | | | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **scrapy-poet and its deps** | | | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | [❌](#changelog-date) |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Zyte API** | | | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | [❌](#docs-requirements-in) | ✅ | [❌](#sphinx-scrapy-pins) | [❌](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Data extraction** | | | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| **Forms** | | | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | ✅ | ✅ | [❌](#changelog-date) |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | [❌](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [❌](#readthedocs) | ✅ | ✅ | ✅ |
| **Monitoring** | | | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | [❌](#docs-requirements-in) | [❌](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | ✅ | [❌](#docs-stable-links) | ✅ | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [❌](#changelog) | [➖](#changelog-date) |
| **AI agents** | | | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | ✅ | ✅ | ✅ | [❌](#sphinx-scrapy-latest) | ✅ | ✅ | ✅ | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | [➖](#changelog-date) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| **Maintenance** | | | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | ✅ | ✅ |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#docs-requirements-in) | [➖](#sphinx-scrapy) | [➖](#sphinx-scrapy-pins) | [➖](#sphinx-scrapy-latest) | [➖](#readthedocs) | [➖](#docs-stable-links) | [➖](#changelog) | [➖](#changelog-date) |

### docs-requirements-in

Sphinx docs requirements are defined in docs/requirements.in.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): no docs/requirements.in
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): no docs/requirements.in
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): no docs/requirements.in
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no docs/requirements.in
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): no docs/requirements.in
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): no docs/requirements.in
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): no docs/requirements.in
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): no docs/requirements.in
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): no docs/requirements.in
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): no docs/requirements.in
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): no docs/requirements.in
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no docs/requirements.in
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no docs/requirements.in
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no docs/requirements.in
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): no docs/requirements.in
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy

Sphinx docs use sphinx-scrapy.

- ❌ [scrapy/cssselect](https://github.com/scrapy/cssselect): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): sphinx_scrapy not in docs/conf.py or docs/requirements.in
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy-pins

sphinx-scrapy is pinned to the same version in the tox requires, the docs requirements and the pre-commit hook rev.

- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned in tox, docs/requirements.in, .pre-commit-config.yaml
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### sphinx-scrapy-latest

sphinx-scrapy is pinned to its latest release.

- ❌ [scrapy/scrapy](https://github.com/scrapy/scrapy): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): not pinned
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): not pinned
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): pinned to 0.8.4, latest is 0.14.0
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): pinned to 0.8.12, latest is 0.14.0
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): pinned to 0.13.0, latest is 0.14.0
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): pinned to 0.8.12, latest is 0.14.0
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): pinned to 0.13.0, latest is 0.14.0
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): not pinned
- ❌ [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub): pinned to 0.7.1, latest is 0.14.0
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): pinned to 0.8.4, latest is 0.14.0
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): pinned to 0.8.10, latest is 0.14.0
- ➖ Does not use sphinx-scrapy. [scrapy/cssselect](https://github.com/scrapy/cssselect), [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/itemloaders](https://github.com/scrapy/itemloaders), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/w3lib](https://github.com/scrapy/w3lib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy/form2request](https://github.com/scrapy/form2request), [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite), [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### readthedocs

Sphinx docs are built on Read the Docs (.readthedocs.yml), and the README links to them.

- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): the README does not link to Formasaurus.readthedocs.io or Formasaurus.readthedocs.org
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): no .readthedocs.yml
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): no .readthedocs.yml; the README does not link to python-crfsuite.readthedocs.io or python-crfsuite.readthedocs.org
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### docs-stable-links

Links to the docs in the README and in [project.urls] that name a version use stable, which is built from the latest release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy/parsel](https://github.com/scrapy/parsel): links to latest in pyproject.toml
- ❌ [scrapy/w3lib](https://github.com/scrapy/w3lib): links to latest in pyproject.toml
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): links to latest in README.rst
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): links to latest in README.rst; latest in pyproject.toml
- ❌ [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items): links to latest in README.rst
- ❌ [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapy/form2request](https://github.com/scrapy/form2request): links to latest in README.rst; latest in pyproject.toml
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): links to latest in README.rst
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): links to latest in README.rst; latest in pyproject.toml
- ➖ On docs.scrapy.org, latest is the latest release and master the default branch. [scrapy/scrapy](https://github.com/scrapy/scrapy)
- ➖ No Sphinx docs. [scrapy/formerly](https://github.com/scrapy/formerly), [scrapy/itemadapter](https://github.com/scrapy/itemadapter), [scrapy/protego](https://github.com/scrapy/protego), [scrapy/queuelib](https://github.com/scrapy/queuelib), [scrapy/xtractmime](https://github.com/scrapy/xtractmime), [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator), [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright), [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp), [scrapinghub/andi](https://github.com/scrapinghub/andi), [scrapy/frostwork](https://github.com/scrapy/frostwork), [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend), [zytedata/clear-html](https://github.com/zytedata/clear-html), [zytedata/html-text](https://github.com/zytedata/html-text), [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official), [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage), [zytedata/harness-run](https://github.com/zytedata/harness-run), [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly), [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### changelog

There is a changelog, e.g. CHANGES.rst, CHANGELOG.md, NEWS or docs/news.rst.

- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no changelog file
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no changelog file
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no changelog file
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no changelog file
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### changelog-date

bump-my-version replaces (unreleased) in the changelog with the release date.

- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ❌ [zytedata/url-matcher](https://github.com/zytedata/url-matcher): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): no file replacement of (unreleased) with {now:%Y-%m-%d}
- ➖ Does not use bump-my-version. [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder), [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules), [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow), [scrapinghub/frontera](https://github.com/scrapinghub/frontera), [scrapinghub/extruct](https://github.com/scrapinghub/extruct), [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser), [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [zytedata/harness-run](https://github.com/zytedata/harness-run)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

## Releases

| Check | Statement | Results |
| --- | --- | --- |
| [`latest-release`](#latest-release) | The latest release on PyPI, with its date. | 52/59 yes |
| [`unreleased-changes`](#unreleased-changes) | The default branch has commits since the latest release on PyPI. | 43/52 yes |
| [`trusted-publishing`](#trusted-publishing) | Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment. | 35/59 passing |
| [`publish-on-tag`](#publish-on-tag) | Publishing is triggered by pushing a tag, not by creating a GitHub release. | 46/59 passing |
| [`separate-build-job`](#separate-build-job) | The publish workflow builds distributions in a separate job from the one that publishes them. | 22/59 passing |
| [`bump-my-version`](#bump-my-version) | bump-my-version is configured, in pyproject.toml or .bumpversion.toml. | 46/61 passing |

| Project | [latest-release](#latest-release) | [unreleased-changes](#unreleased-changes) | [trusted-publishing](#trusted-publishing) | [publish-on-tag](#publish-on-tag) | [separate-build-job](#separate-build-job) | [bump-my-version](#bump-my-version) |
| --- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Scrapy and its deps** | | | | | | |
| [scrapy/scrapy](https://github.com/scrapy/scrapy) | 2.19.0 (2026-09-10) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/cssselect](https://github.com/scrapy/cssselect) | 1.6.0 (2026-10-09) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/formerly](https://github.com/scrapy/formerly) | 0.1.0 (2026-08-05) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/itemadapter](https://github.com/scrapy/itemadapter) | 0.13.1 (2026-01-08) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/itemloaders](https://github.com/scrapy/itemloaders) | 1.5.0 (2026-09-29) | yes | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy/parsel](https://github.com/scrapy/parsel) | 1.12.1 (2026-09-28) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/protego](https://github.com/scrapy/protego) | 0.7.0 (2026-09-21) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/queuelib](https://github.com/scrapy/queuelib) | 1.10.0 (2026-08-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/w3lib](https://github.com/scrapy/w3lib) | 2.5.0 (2026-09-30) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/xtractmime](https://github.com/scrapy/xtractmime) | 0.2.1 (2024-01-16) | yes | ✅ | ✅ | ✅ | ✅ |
| **Scrapy plugins** | | | | | | |
| [scrapy-plugins/scrapy-download-handlers-incubator](https://github.com/scrapy-plugins/scrapy-download-handlers-incubator) | 0.5.1 (2026-09-11) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright) | 0.0.48 (2026-07-10) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata) | 0.2.0 (2024-09-26) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder) | 0.3.0 (2024-12-30) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules) | 2024.11.5 (2024-11-05) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **Scrapy tools** | | | | | | |
| [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint) | 0.1.1 (2026-01-27) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt) | 0.18.1 (2026-06-29) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Feed exporters** | | | | | | |
| [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc) | no | [➖](#unreleased-changes) | ✅ | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp) | 1.1.0 (2025-02-12) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **scrapy-poet and its deps** | | | | | | |
| [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet) | 0.27.2 (2026-04-28) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/andi](https://github.com/scrapinghub/andi) | 0.9.0 (2026-09-17) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet) | 0.24.1 (2026-04-28) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/url-matcher](https://github.com/zytedata/url-matcher) | 0.6.0 (2025-02-14) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapy/frostwork](https://github.com/scrapy/frostwork) | 0.1.6 (2026-09-23) | yes | ✅ | ✅ | ✅ | ✅ |
| **Zyte API** | | | | | | |
| [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api) | 0.36.0 (2026-08-20) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api) | 0.11.0 (2026-07-23) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) | 2.4.1 (2025-03-24) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/zyte-common-items](https://github.com/zytedata/zyte-common-items) | 0.30.0 (2026-10-14) | no | ✅ | ✅ | ✅ | ✅ |
| **Scrapy Cloud** | | | | | | |
| [scrapinghub/python-scrapinghub](https://github.com/scrapinghub/python-scrapinghub) | 2.9.0 (2026-08-12) | no | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/shub](https://github.com/scrapinghub/shub) | 2.18.1 (2026-07-08) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy) | 0.18.1 (2026-01-28) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow) | 1.14.43 (2026-10-13) | no | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera) | 0.3.0 (2025-06-06) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/frontera](https://github.com/scrapinghub/frontera) | 0.8.1 (2019-04-05) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend) | 0.6.1 (2025-10-31) | no | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| **Data extraction** | | | | | | |
| [zytedata/zyte-parsers](https://github.com/zytedata/zyte-parsers) | 0.6.0 (2025-10-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/clear-html](https://github.com/zytedata/clear-html) | 0.5.0 (2025-10-24) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/html-text](https://github.com/zytedata/html-text) | 0.7.1 (2025-10-06) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser) | 0.5.1 (2026-03-19) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser) | 1.4.3 (2026-09-03) | yes | ✅ | [❌](#publish-on-tag) | ✅ | ✅ |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | 0.18.0 (2024-11-08) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser) | 0.3.2 (2023-03-28) | yes | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **Forms** | | | | | | |
| [scrapy/form2request](https://github.com/scrapy/form2request) | 0.2.0 (2024-07-15) | yes | ✅ | ✅ | ✅ | ✅ |
| [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus) | 0.10.0 (2024-11-07) | yes | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite) | 0.5.0 (2024-06-18) | no | [❌](#trusted-publishing) | ✅ | [❌](#separate-build-job) | [❌](#bump-my-version) |
| [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite) | 0.9.12 (2025-12-23) | no | [❌](#trusted-publishing) | [❌](#publish-on-tag) | ✅ | ✅ |
| **Monitoring** | | | | | | |
| [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon) | 1.27.0 (2026-08-10) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon) | no | [➖](#unreleased-changes) | [❌](#trusted-publishing) | [❌](#publish-on-tag) | [❌](#separate-build-job) | [❌](#bump-my-version) |
| **AI agents** | | | | | | |
| [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [scrapy/scrapy-mcp-official](https://github.com/scrapy/scrapy-mcp-official) | 0.1.2 (2026-09-07) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/agent-exam](https://github.com/zytedata/agent-exam) | 0.2.0 (2026-08-17) | yes | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [zytedata/claude-measure-usage](https://github.com/zytedata/claude-measure-usage) | 0.1.1 (2026-09-14) | yes | ✅ | ✅ | ✅ | ✅ |
| [zytedata/harness-run](https://github.com/zytedata/harness-run) | 0.4.0 (2026-09-23) | yes | ✅ | ✅ | ✅ | [❌](#bump-my-version) |
| [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly) | 0.7.0 (2026-10-03) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| **Maintenance** | | | | | | |
| [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy) | 0.14.0 (2026-10-14) | no | ✅ | ✅ | [❌](#separate-build-job) | ✅ |
| [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | ✅ |
| [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance) | [➖](#latest-release) | [➖](#unreleased-changes) | [➖](#trusted-publishing) | [➖](#publish-on-tag) | [➖](#separate-build-job) | [➖](#bump-my-version) |

### latest-release

The latest release on PyPI, with its date.

- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### unreleased-changes

The default branch has commits since the latest release on PyPI.

- ➖ Not on PyPI. [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc), [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage), [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox), [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive), [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets), [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive), [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon), [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin), [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard), [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### trusted-publishing

Releases are published to PyPI from GitHub Actions through trusted publishing, in a job with a GitHub environment.

- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml uses an API token
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no workflow publishes to PyPI
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): .github/workflows/publish.yml uses an API token
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml uses an API token
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' has no environment; .github/workflows/python-publish.yml publishes with twine upload
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml publishes with twine upload
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): .github/workflows/publish.yml: job 'deploy' has no environment; .github/workflows/publish.yml uses an API token; .github/workflows/publish.yml lacks the id-token: write permission
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): .github/workflows/build_and_upload.yml: job 'upload_to_pypi' has no environment; .github/workflows/build_and_upload.yml uses an API token; .github/workflows/build_and_upload.yml lacks the id-token: write permission
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### publish-on-tag

Publishing is triggered by pushing a tag, not by creating a GitHub release.

- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): .github/workflows/release.yml is not triggered by tag pushes
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no workflow publishes to PyPI
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/dateparser](https://github.com/scrapinghub/dateparser): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml is triggered by GitHub releases
- ❌ [scrapinghub/python-crfsuite](https://github.com/scrapinghub/python-crfsuite): .github/workflows/build_and_upload.yml is triggered by GitHub releases
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### separate-build-job

The publish workflow builds distributions in a separate job from the one that publishes them.

- ❌ [scrapy/itemadapter](https://github.com/scrapy/itemadapter): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/itemloaders](https://github.com/scrapy/itemloaders): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-playwright](https://github.com/scrapy-plugins/scrapy-playwright): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-spider-metadata](https://github.com/scrapy-plugins/scrapy-spider-metadata): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy/scrapy-lint](https://github.com/scrapy/scrapy-lint): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapyrt](https://github.com/scrapinghub/scrapyrt): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): .github/workflows/release.yml: job 'release' builds and publishes
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no workflow publishes to PyPI
- ❌ [scrapy-plugins/scrapy-feedexporter-sftp](https://github.com/scrapy-plugins/scrapy-feedexporter-sftp): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapy-poet](https://github.com/scrapinghub/scrapy-poet): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/web-poet](https://github.com/scrapinghub/web-poet): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-api](https://github.com/scrapy-plugins/scrapy-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/python-zyte-api](https://github.com/zytedata/python-zyte-api): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/scrapy-zyte-smartproxy](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub](https://github.com/scrapinghub/shub): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/scrapinghub-entrypoint-scrapy](https://github.com/scrapinghub/scrapinghub-entrypoint-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no workflow publishes to PyPI
- ❌ [scrapinghub/scrapy-frontera](https://github.com/scrapinghub/scrapy-frontera): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/hcf-backend](https://github.com/scrapinghub/hcf-backend): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [zytedata/html-text](https://github.com/zytedata/html-text): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/price-parser](https://github.com/scrapinghub/price-parser): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): .github/workflows/python-publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/Formasaurus](https://github.com/scrapinghub/Formasaurus): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): .github/workflows/publish.yml: job 'deploy' builds and publishes
- ❌ [scrapinghub/spidermon](https://github.com/scrapinghub/spidermon): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no workflow publishes to PyPI
- ❌ [zytedata/agent-exam](https://github.com/zytedata/agent-exam): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-llm-friendly](https://github.com/scrapy/sphinx-llm-friendly): .github/workflows/publish.yml: job 'publish' builds and publishes
- ❌ [scrapy/sphinx-scrapy](https://github.com/scrapy/sphinx-scrapy): .github/workflows/publish.yml: job 'publish' builds and publishes
- ➖ Agent plugin. [scrapy/scrapy-agent-plugin](https://github.com/scrapy/scrapy-agent-plugin)
- ➖ GitHub Action. [scrapy/unattended-pr-guard](https://github.com/scrapy/unattended-pr-guard)
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)

### bump-my-version

bump-my-version is configured, in pyproject.toml or .bumpversion.toml.

- ❌ [zytedata/duplicate-url-discarder](https://github.com/zytedata/duplicate-url-discarder): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [zytedata/duplicate-url-discarder-rules](https://github.com/zytedata/duplicate-url-discarder-rules): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexport-warc](https://github.com/scrapy-plugins/scrapy-feedexport-warc): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-azure-storage](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-dropbox](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-drive](https://github.com/scrapy-plugins/scrapy-feedexporter-google-drive): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-google-sheets](https://github.com/scrapy-plugins/scrapy-feedexporter-google-sheets): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapy-plugins/scrapy-feedexporter-onedrive](https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/shub-workflow](https://github.com/scrapinghub/shub-workflow): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/frontera](https://github.com/scrapinghub/frontera): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [scrapinghub/extruct](https://github.com/scrapinghub/extruct): only legacy (bump2version) configuration, in setup.cfg
- ❌ [scrapinghub/number-parser](https://github.com/scrapinghub/number-parser): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [scrapinghub/sklearn-crfsuite](https://github.com/scrapinghub/sklearn-crfsuite): only legacy (bump2version) configuration, in .bumpversion.cfg
- ❌ [scrapy-plugins/zyte-spidermon](https://github.com/scrapy-plugins/zyte-spidermon): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ❌ [zytedata/harness-run](https://github.com/zytedata/harness-run): no [tool.bumpversion] in pyproject.toml or .bumpversion.toml
- ➖ Internal tool. [zytedata/zyte-oss-maintenance](https://github.com/zytedata/zyte-oss-maintenance)
