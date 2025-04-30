# ut

[![PyPI - Version](https://img.shields.io/pypi/v/ut.svg)](https://pypi.org/project/ut)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ut.svg)](https://pypi.org/project/ut)

-----

# Table of Contents

- [Installation](#installation)
- [License](#license)
- [Development](#development)

## Installation

```console
pip install ut
```

## License

`ut` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.


## Development

- Installation

```bash
# Clone the repository
git clone https://github.com/tavor118/ut
cd ut

# Set up a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate

# Install the package
pip install -e .
```

- Useful commands
```bash
# run ruff
uv run ruff check .

# run ruff and fix
uv run ruff check --fix .

# format code using ruff
uv run ruff format .
```
