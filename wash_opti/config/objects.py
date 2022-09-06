"""Hold all objects present in the package."""

from dataclasses import dataclass


@dataclass
class Task:
    """A task handed to the laundry service."""

    ID: str
    DURATION: int
    PREFERRED_DELIVERY: int
