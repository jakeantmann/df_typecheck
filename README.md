# df_typecheck

Typechecks for pandas dataframe columns using a single, central type dictionary

![Tests](https://github.com/jakeantmann/df_typecheck/actions/workflows/tests.yml/badge.svg)

## ToDo

![cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) is inspiration. Might fork when making my cookiecutter

### ~~Initial setup:~~

- ~~Add base code and tests in src layout~~
- ~~Git~~
  - ~~Install git fork~~
  - ~~Create git repo (simple readme, license)~~
  - ~~Make generic .gitignore~~
  - ~~Put on github~~

### ~~Packaging~~

- ~~Turn into package using pyproject.toml and setup.cfg~~

### ~~Code quality part 1: Tox~~

- ~~Tox~~
  - ~~pytest~~
  - ~~wemake (linting)~~
  - ~~docstr-coverage (docstring coverage)~~
  - ~~pyroma (package metadata completeness)~~
  - ~~mypy (optional typehint correctness)~~
  - ~~Add py.typed file~~
  - ~~Fix nitpick issues~~
  - ~~Move metadata to pyproject.toml~~ (only done in commented out version, waiting for pyroma updates)

### Code quality part 2: CI, pre-commit hooks, changelogs

- ~~Simple Github Actions (CI)~~
- Pre-commit hooks
  - ~~Initial pre-commit setup~~
  - Find relevant pre-commit hooks not covered well using tox
  - Implement these
- Code coverage (need to research - coveragepy?)
- Commit standards ([Conventional commits](https://www.conventionalcommits.org/en/v1.0.0/))
- Changelog ([Conventional changelogs](https://github.com/conventional-changelog/conventional-changelog))

### README

For custom badges, use this ![github action](https://github.com/marketplace/actions/dynamic-badges)

- Add some relevant badges to README
  - license [![PyPI - License](https://github.com//jakeantmann/df_typecheck/blob/main/LICENSE)](https://img.shields.io/pypi/l/df_typecheck)
  - pypi [![pypi](https://pypi.org/project/df_typecheck.svg)](https://img.shields.io/pypi/v/df_typecheck)
  - PyPi python versions [![PyPI - Python Version](https://pypi.org/project/df_typecheck)](https://img.shields.io/pypi/pyversions/df_typecheck)
  - codestyle: wemake
    [![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
  - Code coverage [![https://codecov.io/gh//jakeantmann/df_typecheck/branch/main/graph/badge.svg](https://codecov.io/gh//jakeantmann/df_typecheck/branch/main)](Codecov status)
  - Split tox_gh_actions tests into several kinds of tests
    - Tests
    - Docs
  - Cookiecutter template example badge [![Cookiecutter template from @cthoyt](https://github.com/cthoyt/cookiecutter-python-package)](https://img.shields.io/badge/Cookiecutter-snekpack-blue), make my own
- Organise badges
- What else goes in a standard readme? Research this

### Cookiecutter template

- ~~Personal package template~~ (keep updating)

### General tools to include

- bumpversion (Version management)
- Documentation
  - sphinx
  - mkdocs
  - readTheDocs
  - Add to tox
  - Add documentation status badge [![https://readthedocs.org/projects/df_typecheck/badge/?version=latest](https://df_typecheck.readthedocs.io/en/latest/?badge=latest)](Documentation Status - readthedocs)
- click (cmd line tool builder) (including badge?)
- PyPi (automatically push latest code to PyPi, a standard Python public code library)
- BitBucket Pipeline integration
- More tools for testing
  - pytest-cov
  - pytest-randomly
  - pytest-sugar
  - pytest-xdist
- ![Dependency pinning](https://hynek.me/articles/python-app-deps-2018/), requires more research

### Explanatory files to consider -  either make or copy

- Contributing.md (See contributor covenant badge)
- Code of conduct
- Readme for cookiecutter

### Updates to pyproject.toml

- project.dynamic, as seen ![here](https://github.com/pawamoy/git-changelog/blob/master/pyproject.toml)

### More linting tools

- ![import-linter](https://import-linter.readthedocs.io/en/stable/) checks your intra-package imports
- ![dlint](https://github.com/dlint-py/dlint) checks security and coding best practises - complements bandit
- ![Flakehell](https://wemake-python-stylegui.de/en/0.16.0/pages/usage/integrations/flakehell.html) Legacy-first linting

### Other tools to consider using

- ![Cohesion](https://github.com/mschwager/cohesion) Checks class cohesion. Use as a reporting tool
- ![bellybutton](https://github.com/hchasestevens/bellybutton) custom, project-specific linting using regex or ast
- ![vulture](https://github.com/jendrikseipp/vulture) finds unused code
