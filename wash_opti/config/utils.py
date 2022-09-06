"""Hold all utils used throughout the package."""

from pathlib import Path

import yaml


def load_yaml(input_path: Path):
    """Load yaml file."""
    with open(input_path) as file:
        out = yaml.safe_load(file)
    return out
