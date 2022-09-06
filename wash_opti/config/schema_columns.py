"""Hold all columns for available data."""

from dataclasses import dataclass


@dataclass
class Task_table:
    """Detail all columns present in the Task table."""

    ID: str = "task_id"
    DURATION: str = "length"
    PREFERRED_DELIVERY: str = "preferred"
