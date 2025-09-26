# threecx

Python client for 3CX HTTP APIs with configuration handled via Alkivi's config manager.

## Installation

```bash
pip install threecx
```

## Configuration

Configuration is provided by `python-alkivi-config-manager`. See its repository for details: [alkivi-sas/python-alkivi-config-manager](https://github.com/alkivi-sas/python-alkivi-config-manager).

Create a configuration file named `3cx.conf` in one of the supported locations (`./3cx.conf`, `~/.3cx.conf`, `/etc/3cx.conf`):

```ini
[default]
endpoint=prod

[prod]
fqdn=pbx.example.com
username=john
password=secret
```

## Usage

```python
from threecx import get_3cx_api

client = get_3cx_api("prod")
print(client.version())
```

Or list configured endpoints:

```python
from threecx import get_3cx_endpoints

print(get_3cx_endpoints())
```

## Development

- Build: `python -m build` (requires `pip install build`)
- Test: `pytest`

## License

MIT


