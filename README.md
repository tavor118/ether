# ut
Python utilities for better development.

## Installation

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


## Development

Useful commands
```bash
# run ruff
uv run ruff check .

# run ruff and fix
uv run ruff check --fix .

# format code using ruff
uv run ruff format .
```
