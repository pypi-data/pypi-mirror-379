from alkivi.config import ConfigManager


def load_config(app_name: str) -> ConfigManager:
    """Load configuration using Alkivi's config manager.

    Search order (handled by ConfigManager):
      1. ./{app_name}.conf
      2. ~/.{app_name}.conf
      3. /etc/{app_name}.conf
    """
    return ConfigManager(app_name)


