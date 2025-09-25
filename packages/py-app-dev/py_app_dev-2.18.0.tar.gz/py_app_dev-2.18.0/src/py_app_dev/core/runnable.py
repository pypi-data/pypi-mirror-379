# create a Runnable protocol and make Executor accept it
import hashlib
import json
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path

from .logging import logger


class Runnable(ABC):
    def __init__(self, needs_dependency_management: bool = True) -> None:
        self.needs_dependency_management = needs_dependency_management

    @abstractmethod
    def run(self) -> int:
        """Run and return exit code."""

    @abstractmethod
    def get_name(self) -> str:
        """Get runnable name."""

    @abstractmethod
    def get_inputs(self) -> list[Path]:
        """Get runnable dependencies."""

    @abstractmethod
    def get_outputs(self) -> list[Path]:
        """Get runnable outputs."""

    def get_config(self) -> dict[str, str] | None:
        """
        Get runnable configuration.

        (!) Do NOT put sensitive information in the configuration. It will be stored in a file.
        """
        return None


class RunInfoStatus(Enum):
    MATCH = (False, "Nothing changed. Previous execution info matches.")
    NO_INFO = (True, "No previous execution info found.")
    FILE_NOT_FOUND = (True, "File not found.")
    FILE_CHANGED = (True, "File has changed.")
    INPUT_FILES_CHANGED = (True, "Current input files have changed (added or removed).")
    NOTHING_TO_CHECK = (True, "Nothing to be checked. Assume it shall always run.")
    FORCED_RUN = (True, "Forced run. Ignore previous execution info.")
    CONFIG_CHANGED = (True, "Configuration has changed.")

    def __init__(self, should_run: bool, message: str) -> None:
        self.should_run = should_run
        self.message = message


class Executor:
    """
    Accepts Runnable objects and executes them.

    It create a file with the same name as the runnable's name and stores the inputs and outputs with their hashes.
    If the file exists, it checks the hashes of the inputs and outputs and if they match, it skips the execution.
    """

    RUN_INFO_FILE_EXTENSION = ".deps.json"

    def __init__(self, cache_dir: Path, force_run: bool = False, dry_run: bool = False) -> None:
        self.cache_dir = cache_dir
        self.force_run = force_run
        self.dry_run = dry_run

    @staticmethod
    def get_file_hash(path: Path) -> str | None:
        if path.is_file():
            with open(path, "rb") as file:
                bytes = file.read()
                readable_hash = hashlib.sha256(bytes).hexdigest()
                return readable_hash
        # Return special string for directories instead of hashing the whole directory
        elif path.is_dir():
            return "IS_DIR"
        # Return None if path does not exist
        else:
            return None

    def store_run_info(self, runnable: Runnable) -> None:
        def file_hash_to_str(file_hash: str | None) -> str:
            if file_hash is None:
                return "NOT_FOUND"
            else:
                return file_hash

        file_info = {
            "inputs": {str(path): file_hash_to_str(self.get_file_hash(path)) for path in runnable.get_inputs()},
            "outputs": {str(path): file_hash_to_str(self.get_file_hash(path)) for path in runnable.get_outputs()},
        }

        # Only store config if the runnable has a config
        config = runnable.get_config()
        if config is not None:
            file_info["config"] = config

        run_info_path = self.get_runnable_run_info_file(runnable)
        run_info_path.parent.mkdir(parents=True, exist_ok=True)
        with run_info_path.open("w") as f:
            # pretty print the json file
            json.dump(file_info, f, indent=4)

    def get_runnable_run_info_file(self, runnable: Runnable) -> Path:
        return self.cache_dir / f"{runnable.get_name()}{self.RUN_INFO_FILE_EXTENSION}"

    def previous_run_info_matches(self, runnable: Runnable) -> RunInfoStatus:
        if self.force_run:
            return RunInfoStatus.FORCED_RUN
        run_info_path = self.get_runnable_run_info_file(runnable)
        if not run_info_path.exists():
            return RunInfoStatus.NO_INFO

        with run_info_path.open() as f:
            previous_info = json.load(f)

        # Check if configuration has changed
        current_config = runnable.get_config()
        if "config" in previous_info:
            if current_config != previous_info["config"]:
                return RunInfoStatus.CONFIG_CHANGED

        # Check if the list of inputs has changed
        current_inputs = {str(path) for path in runnable.get_inputs()}
        previous_inputs = set(previous_info.get("inputs", {}).keys())
        if current_inputs != previous_inputs:
            return RunInfoStatus.INPUT_FILES_CHANGED

        # Check if there is anything to be checked
        if any(len(previous_info[file_type]) for file_type in ["inputs", "outputs"]):
            for file_type in ["inputs", "outputs"]:
                for path_str, previous_hash in previous_info[file_type].items():
                    path = Path(path_str)
                    if not path.exists():
                        return RunInfoStatus.FILE_NOT_FOUND
                    elif self.get_file_hash(path) != previous_hash:
                        return RunInfoStatus.FILE_CHANGED
        # If there is nothing to be checked, assume it shall always run
        else:
            return RunInfoStatus.NOTHING_TO_CHECK
        return RunInfoStatus.MATCH

    def execute(self, runnable: Runnable) -> int:
        if not runnable.needs_dependency_management:
            logger.info(f"Runnable '{runnable.get_name()}' does not need dependency management. Executing directly.")
            if self.dry_run:
                return 0
            return runnable.run()

        run_info_status = self.previous_run_info_matches(runnable)
        if run_info_status.should_run:
            logger.info(f"Runnable '{runnable.get_name()}' must run. {run_info_status.message}")
            if self.dry_run:
                return 0
            exit_code = runnable.run()
            self.store_run_info(runnable)
            return exit_code
        logger.info(f"Runnable '{runnable.get_name()}' execution skipped. {run_info_status.message}")

        return 0
