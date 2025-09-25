# Data Contract Specification (Python)

The pip module `datacontract-specification` to read and write YAML files using the [Data Contract Specification](https://datacontract.com). The pip module was extracted from the [Data Contract CLI](https://github.com/datacontract/datacontract-cli), which is its primary user.

The version number of the pip module corresponds to the version of the Data Contract Specification it supports.

## Version Mapping

| Data Contract Specification Version | Pip Module Version |
|-------------------------------------|--------------------|
| 1.2.0                               | >=1.2.0            |
| 1.1.0                               | >=1.1.0            |

**Note**: We mirror major and minor version from the Data Contract Specification to the pip module, but not the patch version!

## Installation

```bash
pip install datacontract-specification
```

## Usage

```python
from datacontract_specification.model import DataContractSpecification

# Load a data contract specification from a file
data_contract = DataContractSpecification.from_file('path/to/your/data_contract.yaml')
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```

```python
from datacontract_specification.model import DataContractSpecification

# Load a data contract specification from a string
data_contract_str = """
dataContractSpecification: 1.2.0
id: urn:datacontract:checkout:orders-latest
info:
  title: Orders Latest
  version: 2.0.0
  description: |
    Successful customer orders in the webshop.
    All orders since 2020-01-01.
    Orders with their line items are in their current state (no history included).
  owner: Checkout Team
  status: active
  contact:
    name: John Doe (Data Product Owner)
    url: https://teams.microsoft.com/l/channel/example/checkout
"""
data_contract = DataContractSpecification.from_string(data_contract_str)
# Print the data contract specification as a YAML string
print(data_contract.to_yaml())
```

## Development

```
uv sync --all-extras
```

## Release

- Change version number in `pyproject.toml`
- Run `./release` in your command line
- Wait for the releases on [GitHub](https://github.com/datacontract/datacontract-specification-python/releases), [PyPi](https://test.pypi.org/project/datacontract-specification/) and [PyPi (test)](https://test.pypi.org/project/datacontract-specification/)
