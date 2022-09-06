"""Hold methods for processing inputs before they are handed to the optimizer."""

import logging
import typing as T

import pandas as pd

from wash_opti.config.directories import directories
from wash_opti.config.objects import Task
from wash_opti.config.schema_columns import Task_table
from wash_opti.config.utils import load_yaml

LOGGER = logging.getLogger(__name__)


class InputProcessor:
    """Process inputs."""

    def __init__(self):
        """Initiate class."""
        self.__CONFIG = load_yaml(directories.CONFIG)
        self.__PATH_TO_TASK_TABLE = self.__CONFIG["path_to_input_file"]

    def import_task_table(self) -> pd.DataFrame:
        """Read task table."""
        df = pd.read_csv(self.__PATH_TO_TASK_TABLE)
        self.check_input_table(df)
        return df

    def check_input_table(self, df: pd.DataFrame) -> None:
        """Check if input table has desired characteristics."""
        assert len(df) > 0, "Provided task table is empty"
        assert all([col in df.columns for col in ["task_id", "length", "preferred"]])

    def convert_row_to_task(self, row: pd.Series) -> Task:
        """Read a row in table and convert it to task object."""
        return Task(
            ID=row[Task_table.ID],
            DURATION=row[Task_table.DURATION],
            PREFERRED_DELIVERY=row[Task_table.PREFERRED_DELIVERY],
        )

    def generate_task_list(self, task_table: pd.DataFrame) -> T.List[Task]:
        """Parse rows in task table into list of tasks."""
        task_list = [self.convert_row_to_task(row) for __, row in task_table.iterrows()]
        LOGGER.info("Task list imported")
        LOGGER.info("%s tasks found", str(len(task_list)))
        return task_list

    def execute_pipeline(self) -> T.List[Task]:
        """Execute input processing pipeline.

        Read task table and convert it to list of tasks.
        """
        task_table = self.import_task_table()
        return self.generate_task_list(task_table)
