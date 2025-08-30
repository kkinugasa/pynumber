# PyNumber

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![coverage badge](./docs/figs/coverage.svg)

Set-theoretic construction of numbers

See <https://en.wikipedia.org/wiki/Set-theoretic_definition_of_natural_numbers>

## Setup

### Install from this source code

```sh
git clone https://github.com/kkinugasa/pynumber.git
cd pynumber
uv venv --seed
uv pip install -e .[dev]
```

### Install with uv

```sh
uv add --dev git+https://github.com/kkinugasa/pynumber.git
```

### Install with pip

```sh
pip install git+https://github.com/kkinugasa/pynumber.git
```

## Documentation

After pulling this repo and installing dev deps with uv, run the command:

```sh
uv run mkdocs serve
```
