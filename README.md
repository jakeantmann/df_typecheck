# df_typecheck

Typechecks for pandas dataframe columns using a single, central type dictionary

## ToDo:

https://github.com/cthoyt/cookiecutter-snekpack is inspiration. Might fork when making my cookiecutter

### ~~Initial setup:~~

- ~~Add base code and tests in src layout~~
- ~~Git~~
  - ~~Install git fork~~
  - ~~Create git repo (simple readme, license)~~
  - ~~Make generic .gitignore~~
  - ~~Put on github~~

### ~~Packaging~~

- ~~Turn into package using pyproject.toml and setup.cfg~~

### Code quality part 1: Tox

- Tox
  - ~~pytest~~
  - wemake (linting)
  - docstr-coverage (docstring coverage)
  - pyroma (package metadata completeness)
  - check-manifest (MANIFEST correctness)
  - mypy (optional typehint correctness)
  - ~~Add py.typed file~~
  - Add py.typed to setup.py/setup.cfg/pyproject.toml
  - documentation format and build? (see reference cookiecutter)

### Code quality part 2: CI and pre-commit hooks

- Github Actions (CI)
- Pre-commit hooks
- Code coverage (need to research - coveragepy?)

### Documentation and publication

- Update README (badges etc - do this after tox setup)
- bumpversion (Version management)
- sphinx (Documentation build)
- PyPi

### Cookiecutter template

- Personal package template

