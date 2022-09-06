"""Hold directories used in package."""

from pathlib import Path

MASTER_PATH = "wash_opti"
CONFIG_PATH = "config/config.yaml"


class Directories:
    """Hold all directories."""

    def __init__(self):
        """Initialize class."""
        self.__MASTER = Path(MASTER_PATH)
        self.CONFIG = self.__MASTER / CONFIG_PATH


directories = Directories()
