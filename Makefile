PACKAGE := $$(sed -n 's/^name = "\(.*\)"/\1/p' pyproject.toml)
VERSION := $$(scripts/update_version_from_git.sh >/dev/null || true; sed -n 's/__version__ = "\(.*\)"/\1/p' src/$(PACKAGE)/_version.py)
PATH_COV_BADGE := docs/figs/coverage.svg
RUFF_VERSION := 0.5.7
PYRIGHT_VERSION := 1.1.403

.PHONY: setup clean env-clean format lint typecheck test version pre-commit

setup:
	@uv venv --seed
	@uv pip install pytest pytest-cov pytest-sugar coverage-badge mkdocs-material mkdocstrings-python

clean:
	@rm -rf build dist .eggs *.egg-info
	@rm -rf .benchmarks .coverage coverage.xml htmlcov report.xml .tox
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '*pytest_cache*' -exec rm -rf {} +
	@find . -type f -name "*.py[co]" -exec rm -rf {} +

env-clean: clean
	@rm -rf .venv .uv .tox

format: version
	@bash -lc "command -v ruff >/dev/null 2>&1 && ruff format . || { if [ -e /etc/os-release ] && grep -qi '^ID=nixos' /etc/os-release && command -v nix >/dev/null 2>&1; then nix develop -c ruff format .; else uvx ruff==$(RUFF_VERSION) format .; fi; }"

lint:
	@bash -lc "command -v ruff >/dev/null 2>&1 && ruff check . || { if [ -e /etc/os-release ] && grep -qi '^ID=nixos' /etc/os-release && command -v nix >/dev/null 2>&1; then nix develop -c ruff check .; else uvx ruff==$(RUFF_VERSION) check .; fi; }"
	@bash -lc "command -v pyright >/dev/null 2>&1 && pyright || { if [ -e /etc/os-release ] && grep -qi '^ID=nixos' /etc/os-release && command -v nix >/dev/null 2>&1; then nix develop -c pyright; else uvx pyright@$(PYRIGHT_VERSION); fi; }"

typecheck:
	@bash -lc "command -v pyright >/dev/null 2>&1 && pyright || { if [ -e /etc/os-release ] && grep -qi '^ID=nixos' /etc/os-release && command -v nix >/dev/null 2>&1; then nix develop -c pyright; else uvx pyright@$(PYRIGHT_VERSION); fi; }"

test:
	@.venv/bin/python -m coverage run -m pytest
	@.venv/bin/python -m coverage report -m
	@.venv/bin/python -m coverage xml -o coverage.xml
	@.venv/bin/python -m coverage_badge -fo $(PATH_COV_BADGE)

version:
	@bash scripts/update_version_from_git.sh

pre-commit: setup version format lint typecheck test
