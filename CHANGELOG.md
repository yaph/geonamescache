# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [3.0.0](https://github.com/yaph/geonamescache/releases/tag/3.0.0) - 2025-09-26

<small>[Compare with 2.0.0](https://github.com/yaph/geonamescache/compare/2.0.0...3.0.0)</small>

### Added

- Add test.yml GitHub workflow. ([633071d](https://github.com/yaph/geonamescache/commit/633071dcf8e7da4f5e5b4335e5e6a2d77dc9693d) by Ramiro Gómez).
- Add pyproject.toml. ([9a11a11](https://github.com/yaph/geonamescache/commit/9a11a119e9e5421197b97a85543dadfca3a6adab) by Ramiro Gómez).
- Add mypy check to test task. ([804ad02](https://github.com/yaph/geonamescache/commit/804ad020bbf6722451010dc7bd834daa24b89c2c) by Ramiro Gómez).
- add typing overloads for geonamescache.mappers.country ([d0cc123](https://github.com/yaph/geonamescache/commit/d0cc123232c7a09dcc31c72c7f37432fc9d28396) by jicruz96).
- add type hints ([854a4d6](https://github.com/yaph/geonamescache/commit/854a4d6b85be81df14315e2aa780426f8d11e415) by jicruz96).
- Adding brackets for readability ([0b51b61](https://github.com/yaph/geonamescache/commit/0b51b61c9f4b28fbb41efd343b2b47cd06da1299) by Chris Pigden).
- Add JSON data to git ([2ebb5b9](https://github.com/yaph/geonamescache/commit/2ebb5b9f9cf0ac07ced8a0bc3c4796de4fcbd85a) by Ramiro Gómez).
- Add markdown PyPI support ([fbdc8af](https://github.com/yaph/geonamescache/commit/fbdc8af007d8d07702d38f2908bc7419876f0d8d) by Ramiro Gómez).
- Add base and dev requirements Upgrade dependencies Replace assertEquals with assertEqual ([38ef8f8](https://github.com/yaph/geonamescache/commit/38ef8f8e197d668547367891385b3350b44bb540) by Ramiro Gómez).
- Adding the functionality to do case insensitive search in the search_cities function. If using python3 the function used during comparison will be casefold. In python2 the function used during comparison will be lower. ([27370a5](https://github.com/yaph/geonamescache/commit/27370a51e79b80a1bf354c1b79ac82d1f0c9022b) by Chris Pigden).
- Add github funding info ([4c434c6](https://github.com/yaph/geonamescache/commit/4c434c6d88ba7896449fe28fb94f6e0dab7a5a72) by Ramiro Gómez).
- Adds admin1code to cities.json ([9061cbb](https://github.com/yaph/geonamescache/commit/9061cbbce80e34269c59cc1993d00f403c87c752) by Matt Webb).
- Add funding ([0aea364](https://github.com/yaph/geonamescache/commit/0aea3640fff124b43577e6701e89091066c57ea6) by Ramiro Gómez).
- Add entry to country name mapping ([67c20bf](https://github.com/yaph/geonamescache/commit/67c20bf360eafefbcbdae7bba0c51b592f4c1c86) by Ramiro Gómez).
- Add documentation for country mapper ([65e041b](https://github.com/yaph/geonamescache/commit/65e041bd03863563b52496c1cec81a0c9425f4ee) by Ramiro Gómez).
- Add records to mappings, add mapper tests ([fc054db](https://github.com/yaph/geonamescache/commit/fc054dbf9651dc54bd9785ea1662ad50577175ea) by Ramiro Gómez).
- added python 3.5 to travis ([d7b1eb9](https://github.com/yaph/geonamescache/commit/d7b1eb9c8da7adf1865bb6e23eaad33dfeb15f58) by Ramiro Gómez).
- added python 3.5 to supported versions ([62471d4](https://github.com/yaph/geonamescache/commit/62471d45de4a8f72394d02616cd69993edc5af98) by Ramiro Gómez).
- added makefile tasks and version bump ([b515713](https://github.com/yaph/geonamescache/commit/b51571377a707e4c0a72fb74e58693c4bed97ba9) by Ramiro Gómez).
- Adds travis file to the develop branch so that Travis CI doesn't flip out and do crazy things. ([55f15b0](https://github.com/yaph/geonamescache/commit/55f15b0d86bc2ba509a5c5c237d6ba32ef6e3253) by Michael Lissner).
- Adds a new dependency that wasn't listed before. ([c4ee9f7](https://github.com/yaph/geonamescache/commit/c4ee9f7a1523445672979c6d419045af3d1a530e) by Michael Lissner).
- added country name mappings ([02a695a](https://github.com/yaph/geonamescache/commit/02a695a7d065f37e9572357fff7a5251522cbaac) by Ramiro Gómez).
- added 2 country name mappings ([f858f96](https://github.com/yaph/geonamescache/commit/f858f96b691cc32ade05516d5043761e66fdcafd) by Ramiro Gómez).
- added new method to readme ([c84bed1](https://github.com/yaph/geonamescache/commit/c84bed13c103109003f608f5b7175329864c192e) by Ramiro Gómez).
- added mappings and tests for mappings ([bc14b0e](https://github.com/yaph/geonamescache/commit/bc14b0e82e8d9a83a94daf89786f0a1d7a1c1ecc) by Ramiro Gómez).
- added landscape config: ignore docs dir ([b0deb19](https://github.com/yaph/geonamescache/commit/b0deb19ac7024a4f36dc96e341be416b0a1e44f8) by Ramiro Gómez).
- added pandas as dev req ([6168781](https://github.com/yaph/geonamescache/commit/616878189a11a99cbc53f14c8d52bcadff1939a3) by Ramiro Gómez).
- added countries as CSV ([7d97e5a](https://github.com/yaph/geonamescache/commit/7d97e5aa7004fd87f660186ce6bd6d763339437d) by Ramiro Gómez).
- added fips to us states data ([9b2c87a](https://github.com/yaph/geonamescache/commit/9b2c87a0b4809e843d7892c0cde23678c8f05922) by Ramiro Gómez).
- added travis and pypi badges ([8d945c0](https://github.com/yaph/geonamescache/commit/8d945c04bf13bbaa02fcd6577027fd5c6b50144f) by Ramiro Gómez).
- added travis config ([594f09d](https://github.com/yaph/geonamescache/commit/594f09dfc1a3c246d0aac25171fc0129f780e925) by Ramiro Gómez).
- added pypi command to fab ([0583b3c](https://github.com/yaph/geonamescache/commit/0583b3c3caeb5f675b02c1b2f2ac7b8f87c0b44c) by Ramiro Gómez).
- added fips code to countries ([2880d63](https://github.com/yaph/geonamescache/commit/2880d6353c5d21f3583b8da909c4b101fbd504be) by Ramiro Gomez).
- added more country data and moved it to json file, load country data from json file in module ([1cbbf5d](https://github.com/yaph/geonamescache/commit/1cbbf5d9b1271ec68951bfc65cd0c3844d0b623d) by Ramiro Gomez).
- added doc ([c6e4a60](https://github.com/yaph/geonamescache/commit/c6e4a60e0cd22e7137c5129e6f763df86c95fd55) by Ramiro Gomez).
- added get_us_states_by_names method ([8cd8ca4](https://github.com/yaph/geonamescache/commit/8cd8ca40e941ec3bb93410c0ea8938aca9eb17cd) by Ramiro Gomez).
- Added cities greater than 15k ([56aa267](https://github.com/yaph/geonamescache/commit/56aa267285a9ab529a118df8bc2a13194d8e67a4) by Ramiro Gomez).
- added get_countries_by_names and TODOs ([e498269](https://github.com/yaph/geonamescache/commit/e49826999ad599263f4f6039246c18770e6693aa) by Ramiro Gomez).
- added MANIFEST ([eb00373](https://github.com/yaph/geonamescache/commit/eb00373e49622d1e11f536d2d12c6d95ba19fc6d) by Ramiro Gomez).
- add scripts ([03f271d](https://github.com/yaph/geonamescache/commit/03f271d83415fa2085fb356dd587b8a54d919442) by Ramiro Gomez).

### Fixed

- Fix paths and linting errors ([1f5a93e](https://github.com/yaph/geonamescache/commit/1f5a93eb30c01b9a0ad2da4238c437d614fb3126) by Ramiro Gómez).
- Fix #43: Remove JSON data from git. Add hatch_build.py to temprarily remove "geonamescache/data" from .gitignore so data is included when package is installed using pip. ([2a3da25](https://github.com/yaph/geonamescache/commit/2a3da2579755266757ae00fa68c36da67c055c3e) by Ramiro Gómez).
- Fix issue #1: Download US states data with Python and save as JSON. ([277439c](https://github.com/yaph/geonamescache/commit/277439ca50975d520f26c2362712b66b7b7ebc05) by Ramiro Gómez).
- Fix linting issues: use absolute imports, sys.exit and dict comprehensions. ([b30e161](https://github.com/yaph/geonamescache/commit/b30e1611ed4638b2db667c5ad491366e44f687e4) by Ramiro Gómez).
- fix mypy errors by loosening type restrictions of helper functions ([01e8341](https://github.com/yaph/geonamescache/commit/01e8341b85547aba3f6c771f579795ced9f35220) by jicruz96).
- Fix event name ([3a17926](https://github.com/yaph/geonamescache/commit/3a17926828991d31793850a5b79b98445632cbdc) by Ramiro Gómez).
- fix test_data.py function name ([f763f96](https://github.com/yaph/geonamescache/commit/f763f96549b60384af4a64acf69cb0866d2b54be) by Mikhael Gaster).
- Fix importib files is only support 3.9 so revert ([81b9aab](https://github.com/yaph/geonamescache/commit/81b9aab1a0aada54dc051a5c4f1765dbf214b4d0) by Benny Elgazar).
- Fix #32: Document min_city_population ([39525e7](https://github.com/yaph/geonamescache/commit/39525e76f76455588823d4b27b1a034864cb41b3) by Ramiro Gómez).
- Fix issue #23: Convert README from restructured text to markdown ([5b4a49f](https://github.com/yaph/geonamescache/commit/5b4a49ff305299b4027e03eb9831f5047b501376) by Ramiro Gómez).
- Fix issue #28: Remove check for casefold ([0bfe583](https://github.com/yaph/geonamescache/commit/0bfe5831994a04e24444f4223b08f1559d7c858e) by Ramiro Gómez).
- Fix typo ([00e9edc](https://github.com/yaph/geonamescache/commit/00e9edcaae1ec00b1050cc3d6b5bb171b9991a9c) by Ramiro Gómez).
- Fix issue #12: use io.open in setup.py to set encoding explicitly. ([c65fc89](https://github.com/yaph/geonamescache/commit/c65fc89c6dda1c174e8a22f360c69d0ac53538cd) by Ramiro Gómez).
- Fix issue 12: use io.open in setup.py to set encoding explicitly. ([122a780](https://github.com/yaph/geonamescache/commit/122a780a3e26f5f231a269cb4758745c1eaba79c) by Ramiro Gómez).
- fix travis ([d914c1e](https://github.com/yaph/geonamescache/commit/d914c1e280147f16c02ee5b6b79740390b143579) by Ramiro Gómez).
- Fixes #8 by adding type conversions to the cities script. Regenerates cities.json with the new data. ([0638b0e](https://github.com/yaph/geonamescache/commit/0638b0e8f97a1568e3660db3957c52dba62bde09) by Michael Lissner).
- Fixes #9 by nuking the requirements.txt file in the dev branch and replacing it with the dev_requirements.txt file. ([8aff055](https://github.com/yaph/geonamescache/commit/8aff055c05965830ea0b49b31aa031b46c54f2be) by Michael Lissner).
- fixed rst ([f93e126](https://github.com/yaph/geonamescache/commit/f93e1268a267b591c42cd9b12f5ddcbf86a059d9) by Ramiro Gómez).
- fix rst ([d41e75e](https://github.com/yaph/geonamescache/commit/d41e75e7499f9601c842d913f3c1910d7bc90dec) by Ramiro Gómez).
- fix #2: added mappings module with country name mappings ([fcc662a](https://github.com/yaph/geonamescache/commit/fcc662ad287a789f51a44bf7be13069ac27a4af2) by Ramiro Gómez).
- fixed classifiers ([841e50f](https://github.com/yaph/geonamescache/commit/841e50fa73773f7c866f5af2ccb5ec14f11a2590) by Ramiro Gomez).

### Changed

- Change OS order ([6fcf154](https://github.com/yaph/geonamescache/commit/6fcf154e350a5e7489a331001e6558a66676cf16) by Ramiro Gómez).
- Changes countries to pretty print and use a context manager, making it consistent with the other scripts. ([7630a4b](https://github.com/yaph/geonamescache/commit/7630a4bd0b912de12fed01ad1fb52559ab2dd56c) by Michael Lissner).

### Removed

- Remove version hint ([6d7827c](https://github.com/yaph/geonamescache/commit/6d7827cf27f44eee0ca4c8a4fb6fd373ba686888) by Ramiro Gómez).
- Remove unicode characters because it breaks on windows ([b283410](https://github.com/yaph/geonamescache/commit/b2834107c101e58f7ffbf204a728458d83a99f6c) by Ramiro Gómez).
- Remove data_dir argument. ([170a804](https://github.com/yaph/geonamescache/commit/170a8042c7a8e5bf2a770aba1f9d645c25c071d0) by Ramiro Gómez).
- Remove gitattributes ([ddf9d8c](https://github.com/yaph/geonamescache/commit/ddf9d8c95769bf2aaddb63117e6b546815907881) by Ramiro Gómez).
- Remove support for Python 3.8 and 3.9 Use built-in types instead of typing imports Apply ruff formatting ([0eb056d](https://github.com/yaph/geonamescache/commit/0eb056dc6870a2e8ceb5996bd85292fe047bd316) by Ramiro Gómez).
- Remove landscape config. ([f6f257f](https://github.com/yaph/geonamescache/commit/f6f257fb7f063c05dfd01074a834a28afdccae2a) by Ramiro Gómez).
- Remove obsolete workflow and Python setup files. Add changelog. ([e82e708](https://github.com/yaph/geonamescache/commit/e82e7081328e6a034859c1e75a501cc7d485996a) by Ramiro Gómez).
- Remove obsolete make tasks. ([d6f4d48](https://github.com/yaph/geonamescache/commit/d6f4d48552ab355a96ec9858b3e4f6bf2443b0ae) by Ramiro Gómez).
- Remove install requirements from workflow ([1bcd1c9](https://github.com/yaph/geonamescache/commit/1bcd1c9e014f2a43937e4880a231702dd2012ed4) by Ramiro Gómez).
- Remove install task ([3a676fb](https://github.com/yaph/geonamescache/commit/3a676fb5775c8f2d138d6c71ec8c0fb11859fa0c) by Ramiro Gómez).
- Remove JSON files from geonamescache ([c8b708d](https://github.com/yaph/geonamescache/commit/c8b708d29792262aeea853fd0e4696d22fd65116) by Ramiro Gómez).
- Remove Python 2.7 support ([089fb1d](https://github.com/yaph/geonamescache/commit/089fb1dfbb9165118751d7ca3193baa4f0b24767) by Ramiro Gómez).
- Remove tox Bump package version Use coverage with pytest Change supported Python versions Add test_data.py with data tests ([f9b0845](https://github.com/yaph/geonamescache/commit/f9b08458351e764bc7d557ad5e60f8c9691b343f) by Ramiro Gómez).
- Remove docs directory and tasks because they were not used Update geo data ([b8b85c3](https://github.com/yaph/geonamescache/commit/b8b85c38036cbecbf8dbbc6bd3db6c80845e5101) by Ramiro Gómez).
- Remove Python versions not supported by Travis ([5b3e6e7](https://github.com/yaph/geonamescache/commit/5b3e6e7f8faafecae93d26a59155f3caed188fc8) by Ramiro Gómez).
- Remove useless file ([3e7ace4](https://github.com/yaph/geonamescache/commit/3e7ace485c2894d777f4c90ece98ffc9679c74c2) by Ramiro Gómez).
- Remove outdated info from readme ([d059333](https://github.com/yaph/geonamescache/commit/d0593332b842ab8f24b8cc74fde70c413d42a1be) by Ramiro Gómez).
- Remove Python 2.6 from Travis config ([a9ec8ec](https://github.com/yaph/geonamescache/commit/a9ec8ecd772ab9ad4cfcda98b6ffe4a96b0f0e61) by Ramiro Gómez).
- removed undefined task ([76346d4](https://github.com/yaph/geonamescache/commit/76346d4dfd168a7182ef5a13bec73ec3f33a2d57) by Ramiro Gómez).
- removed pypi from travis since pandas installation fails ([50c7e9d](https://github.com/yaph/geonamescache/commit/50c7e9d7e761c75799bfd0f77224365dccc0cf66) by Ramiro Gómez).
- removed pickle and added json file ([a49ded4](https://github.com/yaph/geonamescache/commit/a49ded4f809d6860bb272a67b1bfa64f9d57d3cc) by Ramiro Gomez).
- remove dev from version ([804e7c5](https://github.com/yaph/geonamescache/commit/804e7c5b210e265af95c261931c0c3dbfad2affb) by Ramiro Gomez).
- removed docs dir, documentation in README, DRY ([53f108e](https://github.com/yaph/geonamescache/commit/53f108e2445d0bb73b44c524525309ac2afd655d) by Ramiro Gomez).
- removed README.md ([a0980cb](https://github.com/yaph/geonamescache/commit/a0980cbfa9ec30b18d47a9a1b15329df085f6e1d) by Ramiro Gomez).

## [2.0.0](https://github.com/yaph/geonamescache/releases/tag/2.0.0) - 2023-07-03

<small>[Compare with 1.6.0](https://github.com/yaph/geonamescache/compare/1.6.0...2.0.0)</small>

### Added

- Adding brackets for readability ([538e8db](https://github.com/yaph/geonamescache/commit/538e8dbe6695e5f237c7b51e8c07fa722efc6532) by Chris Pigden).

## [1.6.0](https://github.com/yaph/geonamescache/releases/tag/1.6.0) - 2023-04-19

<small>[Compare with 1.5.0](https://github.com/yaph/geonamescache/compare/1.5.0...1.6.0)</small>

### Fixed

- fix test_data.py function name ([00ab232](https://github.com/yaph/geonamescache/commit/00ab2326e3311224bb8bd6f3bf2228aa27f0f46f) by Mikhael Gaster).

## [1.5.0](https://github.com/yaph/geonamescache/releases/tag/1.5.0) - 2022-08-03

<small>[Compare with 1.4.0](https://github.com/yaph/geonamescache/compare/1.4.0...1.5.0)</small>

### Fixed

- Fix importib files is only support 3.9 so revert ([3fb70ea](https://github.com/yaph/geonamescache/commit/3fb70ea8561f899662f3e374b9d3d481d4879bb9) by Benny Elgazar).

## [1.4.0](https://github.com/yaph/geonamescache/releases/tag/1.4.0) - 2022-07-13

<small>[Compare with 1.3.0](https://github.com/yaph/geonamescache/compare/1.3.0...1.4.0)</small>

### Added

- Add JSON data to git ([2b2200d](https://github.com/yaph/geonamescache/commit/2b2200d2b08586d40c5867c1928d7eedd564b8b8) by Ramiro Gómez).
- Add markdown PyPI support ([90d5a78](https://github.com/yaph/geonamescache/commit/90d5a78d57d5e5b730037d4b23c92ad4b2bd7f78) by Ramiro Gómez).

### Fixed

- Fix #32: Document min_city_population ([57aca2f](https://github.com/yaph/geonamescache/commit/57aca2fbea1f01d12897f76c09bccea406d0fbc9) by Ramiro Gómez).
- Fix issue #23: Convert README from restructured text to markdown ([6d331e1](https://github.com/yaph/geonamescache/commit/6d331e134f9ec6491f2d05164f479f7260d7e62c) by Ramiro Gómez).
- Fix issue #28: Remove check for casefold ([17726bd](https://github.com/yaph/geonamescache/commit/17726bd1a71dbea24a36eea45ae88d469d4a4c78) by Ramiro Gómez).
- Fix typo ([e697aed](https://github.com/yaph/geonamescache/commit/e697aedcf4c6bddb00b8eb4a4644809bf2fdfa8e) by Ramiro Gómez).

### Removed

- Remove install requirements from workflow ([5793396](https://github.com/yaph/geonamescache/commit/57933961ca05a9541aec24ffe66a7916719da052) by Ramiro Gómez).
- Remove install task ([0968d6e](https://github.com/yaph/geonamescache/commit/0968d6eb1f64d68d8d1941ac72a2ea0065765f95) by Ramiro Gómez).
- Remove JSON files from geonamescache ([60e875f](https://github.com/yaph/geonamescache/commit/60e875fe1d678d0e4f61c1162475adf8bfefbf2d) by Ramiro Gómez).

## [1.3.0](https://github.com/yaph/geonamescache/releases/tag/1.3.0) - 2021-11-02

<small>[Compare with 1.2.0](https://github.com/yaph/geonamescache/compare/1.2.0...1.3.0)</small>

### Added

- Add base and dev requirements Upgrade dependencies Replace assertEquals with assertEqual ([5f671ce](https://github.com/yaph/geonamescache/commit/5f671ce164937000b8de3c94648cf40d3183955f) by Ramiro Gómez).
- Adding the functionality to do case insensitive search in the search_cities function. If using python3 the function used during comparison will be casefold. In python2 the function used during comparison will be lower. ([c35458c](https://github.com/yaph/geonamescache/commit/c35458c749e0b6e3e2ab4e530a4905fad8617054) by Chris Pigden).
- Add github funding info ([310ff92](https://github.com/yaph/geonamescache/commit/310ff9214d5758b6d136b65c196f7a86583e5089) by Ramiro Gómez).

### Removed

- Remove Python 2.7 support ([69662ef](https://github.com/yaph/geonamescache/commit/69662ef6670a77291359f0f7c29d27502f407403) by Ramiro Gómez).
- Remove tox Bump package version Use coverage with pytest Change supported Python versions Add test_data.py with data tests ([c49b50d](https://github.com/yaph/geonamescache/commit/c49b50db4308a43173bd846e922f6ea4949bb27a) by Ramiro Gómez).
- Remove docs directory and tasks because they were not used Update geo data ([814846a](https://github.com/yaph/geonamescache/commit/814846af7b3eb52acd8f295ac1c1e70ec65582f9) by Ramiro Gómez).

## [1.2.0](https://github.com/yaph/geonamescache/releases/tag/1.2.0) - 2020-05-20

<small>[Compare with 1.1.0](https://github.com/yaph/geonamescache/compare/1.1.0...1.2.0)</small>

## [1.1.0](https://github.com/yaph/geonamescache/releases/tag/1.1.0) - 2019-09-11

<small>[Compare with 1.0.3](https://github.com/yaph/geonamescache/compare/1.0.3...1.1.0)</small>

### Added

- Adds admin1code to cities.json ([8d45202](https://github.com/yaph/geonamescache/commit/8d45202bc996818a0f76720b5fa6d07790c95aba) by Matt Webb).
- Add funding ([9b3c361](https://github.com/yaph/geonamescache/commit/9b3c3613b507444d88cc01ef5241a90d81c9e3ca) by Ramiro Gómez).

### Removed

- Remove Python versions not supported by Travis ([46bc5f4](https://github.com/yaph/geonamescache/commit/46bc5f4918ee94ebb2693a01379d3e0e8b33d246) by Ramiro Gómez).

## [1.0.3](https://github.com/yaph/geonamescache/releases/tag/1.0.3) - 2019-08-27

<small>[Compare with 1.0.2](https://github.com/yaph/geonamescache/compare/1.0.2...1.0.3)</small>

## [1.0.2](https://github.com/yaph/geonamescache/releases/tag/1.0.2) - 2019-04-16

<small>[Compare with 1.0.1](https://github.com/yaph/geonamescache/compare/1.0.1...1.0.2)</small>

### Added

- Add entry to country name mapping ([297fe31](https://github.com/yaph/geonamescache/commit/297fe3154fe60b3399b8deaedc8138a45a614b50) by Ramiro Gómez).
- Add documentation for country mapper ([aa1366d](https://github.com/yaph/geonamescache/commit/aa1366d85c52d2829e1b68acf9ce9bbe8aac2b3e) by Ramiro Gómez).
- Add records to mappings, add mapper tests ([a10449a](https://github.com/yaph/geonamescache/commit/a10449af351691adc84128115e985e12bd8122e8) by Ramiro Gómez).

### Removed

- Remove useless file ([0f0875d](https://github.com/yaph/geonamescache/commit/0f0875d7f3e7cb38620944ebbde635c9fb36e87c) by Ramiro Gómez).
- Remove outdated info from readme ([ac8b91e](https://github.com/yaph/geonamescache/commit/ac8b91e266c6cd61ed9d4b344322c48dfb4d423a) by Ramiro Gómez).
- Remove Python 2.6 from Travis config ([4be4591](https://github.com/yaph/geonamescache/commit/4be45910429b8d90ba695d52185806fcdd11bfbe) by Ramiro Gómez).

## [1.0.1](https://github.com/yaph/geonamescache/releases/tag/1.0.1) - 2018-05-18

<small>[Compare with first commit](https://github.com/yaph/geonamescache/compare/09898314c21464a7e315f81fbbc0ff01442d673c...1.0.1)</small>

### Added

- added python 3.5 to travis ([1fc98d4](https://github.com/yaph/geonamescache/commit/1fc98d4f656de75bf3e578695c27746f1ac8f473) by Ramiro Gómez).
- added python 3.5 to supported versions ([6e8112f](https://github.com/yaph/geonamescache/commit/6e8112fe538d8c75282db2b2625afe2e630f3007) by Ramiro Gómez).
- added makefile tasks and version bump ([3b8e7d1](https://github.com/yaph/geonamescache/commit/3b8e7d1e7a4acac387bc7a92d9560d596d40ca32) by Ramiro Gómez).
- Adds travis file to the develop branch so that Travis CI doesn't flip out and do crazy things. ([ce8584b](https://github.com/yaph/geonamescache/commit/ce8584bf167b1434749e979e0d4a7e1c35611647) by Michael Lissner).
- Adds a new dependency that wasn't listed before. ([f49cb72](https://github.com/yaph/geonamescache/commit/f49cb7296ddf816123001dc401787a6afed7dcc8) by Michael Lissner).
- added country name mappings ([7cef64e](https://github.com/yaph/geonamescache/commit/7cef64ef423de1a90a91fec0926192e351ec9487) by Ramiro Gómez).
- added 2 country name mappings ([9e388a3](https://github.com/yaph/geonamescache/commit/9e388a3f6544c478b14941a873d9b6ecd73372c3) by Ramiro Gómez).
- added new method to readme ([a1b762f](https://github.com/yaph/geonamescache/commit/a1b762fc90a970d939912b26de82eae468845eef) by Ramiro Gómez).
- added mappings and tests for mappings ([8bec9a4](https://github.com/yaph/geonamescache/commit/8bec9a465b169648e9af2509835517a2f660f56e) by Ramiro Gómez).
- added landscape config: ignore docs dir ([a318631](https://github.com/yaph/geonamescache/commit/a31863130c80c3fd891a51aacadcfbf27083ed66) by Ramiro Gómez).
- added pandas as dev req ([626a91e](https://github.com/yaph/geonamescache/commit/626a91e7f9c2aae3538cb2382a83705c5898bc88) by Ramiro Gómez).
- added countries as CSV ([379ef7f](https://github.com/yaph/geonamescache/commit/379ef7f038166b58b874a0136b2eac5baa260d04) by Ramiro Gómez).
- added fips to us states data ([3261910](https://github.com/yaph/geonamescache/commit/3261910c42f1bb2f3d4e6897a2a76c6c0d6008ce) by Ramiro Gómez).
- added travis and pypi badges ([deee36b](https://github.com/yaph/geonamescache/commit/deee36b40108b65825e48bee14dc5a639836e79e) by Ramiro Gómez).
- added travis config ([93f3952](https://github.com/yaph/geonamescache/commit/93f3952c22bb6ae7bf21b68f39808d33cb68d9ca) by Ramiro Gómez).
- added pypi command to fab ([a80b40d](https://github.com/yaph/geonamescache/commit/a80b40df6f32e471002df854a2c79ed66400df92) by Ramiro Gómez).
- added fips code to countries ([e02aac3](https://github.com/yaph/geonamescache/commit/e02aac30a6a48632dfb07df24f6bba15a954c4dd) by Ramiro Gomez).
- added more country data and moved it to json file, load country data from json file in module ([74d9428](https://github.com/yaph/geonamescache/commit/74d9428507d26499b3fd2d9e5d949cc5fd4e8783) by Ramiro Gomez).
- added doc ([99f74c2](https://github.com/yaph/geonamescache/commit/99f74c2b5a66ae84339cef735359f4ac52342c5a) by Ramiro Gomez).
- added get_us_states_by_names method ([18c0bf9](https://github.com/yaph/geonamescache/commit/18c0bf98b0814bf6229243695875fbe6a0544678) by Ramiro Gomez).
- Added cities greater than 15k ([08a35b0](https://github.com/yaph/geonamescache/commit/08a35b028a8227777faf6f5ed9fc61ba583e31fc) by Ramiro Gomez).
- added get_countries_by_names and TODOs ([1a2a725](https://github.com/yaph/geonamescache/commit/1a2a7256bb41deb04fcc921f9f78d75ccab44b56) by Ramiro Gomez).
- added MANIFEST ([eb6b2fe](https://github.com/yaph/geonamescache/commit/eb6b2fe907f37e2f03a69dc82792f8036c77136f) by Ramiro Gomez).
- add scripts ([3d2aba5](https://github.com/yaph/geonamescache/commit/3d2aba51ee6f9e21e8238f2aa03ae223fea0dbaa) by Ramiro Gomez).

### Fixed

- Fix issue #12: use io.open in setup.py to set encoding explicitly. ([5affbd3](https://github.com/yaph/geonamescache/commit/5affbd30061aad4be1a569006949a5afedba8fff) by Ramiro Gómez).
- Fix issue 12: use io.open in setup.py to set encoding explicitly. ([c3a981c](https://github.com/yaph/geonamescache/commit/c3a981c7a2999862ce06ee071c822b009ace1c7b) by Ramiro Gómez).
- fix travis ([e75f29b](https://github.com/yaph/geonamescache/commit/e75f29bbcd9fb83f447af7950e0c6401a6f64505) by Ramiro Gómez).
- Fixes #8 by adding type conversions to the cities script. Regenerates cities.json with the new data. ([20be7b4](https://github.com/yaph/geonamescache/commit/20be7b41120f189311e77738628774ecb5f3357b) by Michael Lissner).
- Fixes #9 by nuking the requirements.txt file in the dev branch and replacing it with the dev_requirements.txt file. ([491e6a8](https://github.com/yaph/geonamescache/commit/491e6a8f7dcbdfda1e5c0af487dab042973badb5) by Michael Lissner).
- fixed rst ([252791b](https://github.com/yaph/geonamescache/commit/252791b46c1ff5548f84639bc5878776584fe6fb) by Ramiro Gómez).
- fix rst ([3ee7d63](https://github.com/yaph/geonamescache/commit/3ee7d63e000bf315c6220481a89ef540d2b38480) by Ramiro Gómez).
- fix #2: added mappings module with country name mappings ([0da8845](https://github.com/yaph/geonamescache/commit/0da88459fafff2d8e8208a01443e39bb7a643dc5) by Ramiro Gómez).
- fixed classifiers ([f39039c](https://github.com/yaph/geonamescache/commit/f39039cad2595737c5d74c11db21361f09a16121) by Ramiro Gomez).

### Changed

- Changes countries to pretty print and use a context manager, making it consistent with the other scripts. ([a3d1e98](https://github.com/yaph/geonamescache/commit/a3d1e9844a2edc87343c5779e2275923a99a8401) by Michael Lissner).

### Removed

- removed undefined task ([ed6d906](https://github.com/yaph/geonamescache/commit/ed6d906c3ba5e92045c24a8b84560d4d4048dd2f) by Ramiro Gómez).
- removed pypi from travis since pandas installation fails ([36aeaa9](https://github.com/yaph/geonamescache/commit/36aeaa9a955f960fbda08c735c6277bd4446f455) by Ramiro Gómez).
- removed pickle and added json file ([5d624f4](https://github.com/yaph/geonamescache/commit/5d624f41aa27f00538f82c1377a47d8be9b34a04) by Ramiro Gomez).
- remove dev from version ([b2efc3b](https://github.com/yaph/geonamescache/commit/b2efc3bf862f3b235c5ab09e4fdd74b2be04f4e2) by Ramiro Gomez).
- removed docs dir, documentation in README, DRY ([e2d4b08](https://github.com/yaph/geonamescache/commit/e2d4b08618add3559f13cacf4444dfc267dbda4f) by Ramiro Gomez).
- removed README.md ([25420f5](https://github.com/yaph/geonamescache/commit/25420f5d1fd5d0995d5931e78ac39ac12a0a86d8) by Ramiro Gomez).

