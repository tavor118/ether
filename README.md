# ut

[![PyPI - Version](https://img.shields.io/pypi/v/ut.svg)](https://pypi.org/project/ut)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ut.svg)](https://pypi.org/project/ut)

Helpful Python Utilities for Improved Development.

-----

# Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Development](#development)

## Installation

```console
pip install ut
```

## Usage

This package offers a range of utilities across multiple categories, including data manipulation, services, and datetime.

### Services


### Data manipulation

> **nget** - nested get

Retrieves a nested item from a dictionary, safely handling exceptions
and returning `None` if any step fails.
Useful for accessing data from a JSON.

Args:

- obj: The dictionary to traverse.
- items: A sequence of keys or indices to follow in the dictionary.
- default: The default value to return if any key/index is not found.

Returns: The value found at the end of the item chain, or None/default
    if any key/index is not found.

```python
>>> data = {'result': {'users': [{'address': {'street': 'Main St'}}]}}
>>> nget(data, 'result', 'users', 0, 'address', 'street')
'Main St'
>>> nget(data, 'result.users.0.address.street')
'Main St'
>>> nget(data, 'result', 'users', 0, 'address', 'zipcode')
None
>>> nget(data, 'result', 'users', 0, 'address', 'zipcode', default='NY')
'NY'
```


### Datetime


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

- Run tests

```bash
pytest tests
```

- Linting / formatting

```bash
# run ruff
uv run ruff check .

# run ruff and fix
uv run ruff check --fix .

# format code using ruff
uv run ruff format .
```
