Demo
====

Template project with all configured linters.

Development
-----------

Install dependencies.

```shell
pip install -U pip poetry
poetry install
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
- `flake8`
- `pycodestyle`
- `mypy`

Testing
-------

Run all tests:

```shell
pytest --cov .
```

CI
--

- [GitHub Actions](.github/workflows/ci.yml)
- [GitLab CI/CD](.gitlab-ci.yml)
