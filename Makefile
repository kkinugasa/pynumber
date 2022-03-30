PACKAGE := $$(sed -n 's/name = "\(.*\)"/\1/p' pyproject.toml)
VERSION := $$(sed -n 's/__version__ = "\(.*\)"/\1/p' $(PACKAGE)/_version.py )
PATH_COV_BADGE := docs/figs/coverage.svg

setup:
	@poetry install

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '.mypy_cache' -exec rm -rf {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

env-clean: clean
	@rm -rf .venv
	@rm -rf .tox

format:
	@poetry run isort .
	@poetry run black .

lint:
	@poetry run pylint -d C $(PACKAGE)
	@poetry run mypy .

test:
	@poetry run pytest
	@poetry run coverage-badge -fo $(PATH_COV_BADGE)

version:
	@sed -n 's/version = \(.*\)/__version__ = \1/p' pyproject.toml > $(PACKAGE)/_version.py

pre-commit: version format lint test
