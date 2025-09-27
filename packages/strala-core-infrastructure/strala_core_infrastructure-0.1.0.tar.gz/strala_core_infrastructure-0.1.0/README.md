# Strala Core Infrastructure

A shared Python package containing common utilities, schemas, and services used across Strala's claims platform applications.

## Installation

### From PyPI (when published)
```bash
pip install strala-core-infrastructure
```

### From source
```bash
git clone https://github.com/strala/core-infrastructure.git
cd core-infrastructure
pip install -e .
```

## Usage

```python
from strala_core import schemas, utils, services

# Use the base model
from strala_core.schemas import BaseModel

class MyModel(BaseModel):
    name: str
    value: int
```

## Development

### Building the package
```bash
./scripts/build.sh
```

### Publishing to PyPI
```bash
./scripts/publish.sh
```

## Package Structure

- `strala_core.schemas` - Common data models and schemas (api, pubsub)
- `strala_core.utils` - Utility functions and helpers
- `strala_core.services` - Service interfaces and base classes

## License

MIT License - see LICENSE file for details.
