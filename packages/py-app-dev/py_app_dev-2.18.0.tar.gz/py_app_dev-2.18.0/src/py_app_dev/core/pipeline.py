import importlib
from collections import OrderedDict
from dataclasses import dataclass
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import (
    Any,
    Generic,
    TypeAlias,
    TypeVar,
)

from mashumaro import DataClassDictMixin

from py_app_dev.core.exceptions import UserNotificationException


@dataclass
class PipelineStepConfig(DataClassDictMixin):
    #: Step name or class name if file is not specified
    step: str
    #: Path to file with step class
    file: str | None = None
    #: Python module with step class
    module: str | None = None
    #: Step class name
    class_name: str | None = None
    #: Step description
    description: str | None = None
    #: Step timeout in seconds
    timeout_sec: int | None = None
    #: Custom step configuration
    config: dict[str, Any] | None = None


PipelineConfig: TypeAlias = list[PipelineStepConfig] | OrderedDict[str, list[PipelineStepConfig]]

TPipelineStep = TypeVar("TPipelineStep")


class PipelineStep:
    """Base class for pipelines with no custom user steps."""

    pass


@dataclass
class PipelineStepReference(Generic[TPipelineStep]):
    """Once a Step is found, keep the Step class reference to be able to instantiate it later."""

    group_name: str | None
    _class: type[TPipelineStep]
    config: dict[str, Any] | None = None


class PipelineLoader(Generic[TPipelineStep]):
    def __init__(self, pipeline_config: PipelineConfig, project_root_dir: Path) -> None:
        self.pipeline_config = pipeline_config
        self.project_root_dir = project_root_dir

    def load_steps(self) -> list[PipelineStepReference[TPipelineStep]]:
        result = []
        if isinstance(self.pipeline_config, list):
            # Handle List[PipelineStepConfig]
            result.extend(self._load_steps(None, self.pipeline_config, self.project_root_dir))
        elif isinstance(self.pipeline_config, OrderedDict):
            # Handle OrderedDict[str, List[PipelineStepConfig]]
            for group_name, steps_config in self.pipeline_config.items():
                result.extend(self._load_steps(group_name, steps_config, self.project_root_dir))
        else:
            raise UserNotificationException("Invalid pipeline configuration. Expected a list or an ordered dictionary.")
        return result

    @staticmethod
    def _load_steps(
        group_name: str | None,
        steps_config: list[PipelineStepConfig],
        project_root_dir: Path,
    ) -> list[PipelineStepReference[TPipelineStep]]:
        result = []
        for step_config in steps_config:
            step_class_name = step_config.class_name or step_config.step
            if step_config.module:
                step_class = PipelineLoader[TPipelineStep]._load_module_step(step_config.module, step_class_name)
            elif step_config.file:
                step_class = PipelineLoader[TPipelineStep]._load_user_step(project_root_dir.joinpath(step_config.file), step_class_name)
            else:
                raise UserNotificationException(f"Step '{step_class_name}' has no 'module' nor 'file' defined. Please check your pipeline configuration.")
            result.append(PipelineStepReference(group_name, step_class, step_config.config))
        return result

    @staticmethod
    def _load_user_step(python_file: Path, step_class_name: str) -> type[TPipelineStep]:
        # Create a module specification from the file path
        spec = spec_from_file_location(f"user__{step_class_name}", python_file)
        if spec and spec.loader:
            step_module = module_from_spec(spec)
            # Import the module
            spec.loader.exec_module(step_module)
            try:
                step_class = getattr(step_module, step_class_name)
            except AttributeError:
                raise UserNotificationException(f"Could not load class '{step_class_name}' from file '{python_file}'. Please check your pipeline configuration.") from None
            return step_class
        raise UserNotificationException(f"Could not load file '{python_file}'. Please check the file for any errors.")

    @staticmethod
    def _load_module_step(module_name: str, step_class_name: str) -> type[TPipelineStep]:
        try:
            module = importlib.import_module(module_name)
            step_class = getattr(module, step_class_name)
        except ImportError:
            raise UserNotificationException(f"Could not load module '{module_name}'. Please check your pipeline configuration.") from None
        except AttributeError:
            raise UserNotificationException(f"Could not load class '{step_class_name}' from module '{module_name}'. Please check your pipeline configuration.") from None
        return step_class
