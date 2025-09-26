from typing import Dict, List

from .client import ThreeCXClient
from .config import load_config

_THREECX_API_CLIENTS: Dict[str, ThreeCXClient] = {}


def get_3cx_endpoints(app_name: str = "3cx") -> List[str]:
    """Return available endpoint section names from configuration.

    It reads the configuration using Alkivi's ConfigManager and returns all
    section names except the special 'default' section.
    """
    cfg = load_config(app_name)
    parser = cfg._config  # use underlying configparser
    return [s for s in parser.sections() if s.lower() != "default"]


def get_3cx_api(endpoint: str, app_name: str = "3cx") -> ThreeCXClient:
    """Return a cached ThreeCXClient for the given endpoint.

    The configuration is expected to provide 'username' and 'password' in the
    endpoint section. For example in 3cx.conf:

        [default]
        endpoint=prod

        [prod]
        username=john
        password=secret
        fqdn=pbx.example.com
    """
    if endpoint in _THREECX_API_CLIENTS:
        return _THREECX_API_CLIENTS[endpoint]

    cfg = load_config(app_name)
    parser = cfg._config

    section = endpoint
    fqdn = parser.get(section, "fqdn", fallback=endpoint)
    username = parser.get(section, "username")
    password = parser.get(section, "password")

    client = ThreeCXClient(fqdn=fqdn, username=username, password=password)
    _THREECX_API_CLIENTS[endpoint] = client
    return client


