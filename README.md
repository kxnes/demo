Demo
====

Template project with all configured linters.

Development
-----------

Install dependencies.

```shell
pip install -U pip setuptools poetry
# recommended version: 1.1.12
poetry install --no-root
```

Setup `pre-commit` hook.

```shell
./pre-commit.sh
```

Linters
-------

Use registered linters like:

- `isort`
- `black`
- `flake8` (wemake-python-styleguide)
- `pyright`
- `mypy`

Testing
-------

Run all tests:

```shell
pytest --cov .
```
