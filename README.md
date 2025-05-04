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

- `service` decorator
- `nget` function - nested get
- `destruct` function - to extract values from a dictionary, matching variable names from the caller's scope or from provided list
- `utc_now` function

### `@service`


### `nget()`

Retrieves a nested item from a dictionary, safely handling exceptions
and returning `None` if any step fails.
Useful for accessing data from a JSON.

Args:

    dct: The dictionary to traverse.
    items: A sequence of keys or indices to follow in the dictionary.
    default: The default value to return if any key/index is not found.

Returns:

    The value found at the end of the item chain, or None/default if any key/index is not found.

Example:

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


### `destruct()`

Mimics JavaScript's object destructuring.
Extract values from a dictionary, matching variable names from the caller's scope.

This function inspects the calling frame and tries to match variable names
that exist in the caller's code context with keys in the provided dictionary.
It then returns a tuple of values from the dictionary based on those variable names.

Args:

    dct: The dictionary to extract values from.
    keys: Optional sequence of keys to extract. If None, keys are inferred from the assignment statement.
    default: Default value to use when a key is not found in the dictionary. If not provided, KeyError will be raised for missing keys.

Returns:

    Single value or a tuple of values from the dictionary corresponding
    to the caller's variable names.

Raises:

    KeyError: If any variable name from the caller is not found in the dictionary
        and default value is provided.
    DestructError: If the function cannot complete successfully.

WARNING:

    `destruct` relies on inspecting the caller's frame, which may not work properly
    in interactive environments like the Python shell or Jupyter notebooks.
    Use `keys` argument if you need to work in the shell.

Example:

```python
person_dict = {"name": "John", "age": 30, "city": "New York"}

# Basic usage
name, age, city = destruct(person_dict)

# With default value for missing keys
name, age, country = destruct(person_dict, default="N/A")

# With explicit keys and default
name, country = destruct(person_dict, keys=["name", "country"], default="N/A")
```


### `utc_now()`



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
