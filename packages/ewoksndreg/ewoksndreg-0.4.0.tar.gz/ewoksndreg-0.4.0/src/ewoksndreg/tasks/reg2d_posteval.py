import logging
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from ewokscore.variable import Variable
from pydantic import Field
from pydantic import field_validator
from silx.io.url import DataUrl

from ..evaluation.evaluation import post_evaluation
from ..io.input_stack import InputDataType
from ..io.input_stack import input_context
from ..io.output_stack import output_context
from ..transformation import Transformation
from ..transformation import apply_transformations

_logger = logging.getLogger(__name__)

_EvalResult = Tuple[
    Optional[str], Optional[List[str]], Dict[str, List[Transformation]]
]  # type alias


class Inputs(BaseInputModel):
    image_stacks: InputDataType = Field(
        ...,
        description="Image stacks as a dictionary of numpy arrays or list of HDF5 dataset URI's.",
        examples=[
            {
                "stack1": "/path/to/file1.h5::/entry/process/results/parameters/Ca-K",
                "stack2": "/path/to/file1.h5::/entry/process/results/parameters/Fe-K",
            },
            {"stack1": [[0, 0, 0], [1, 1, 1], [2, 2, 2]]},
        ],
    )
    transformations: Dict[str, List[Transformation]] = Field(
        ..., description="Transformations for each image in each stack."
    )
    reference_stack: Optional[str] = Field(
        None,
        description="Force select stack.",
        examples=["stack1", "stack2"],
    )
    output_root_uri: Optional[DataUrl] = Field(
        None,
        description="URL to save all stacks transformed with its own transformations.",
        examples=["/path/to/file2.h5::/entry/process/results/parameters/"],
    )
    output_configuration: Optional[dict] = Field(
        None,
        description="Registration configuration parameters to be saved.",
        examples=[{"param1": 0, "param2": 1}],
    )
    skip: bool = Field(
        False,
        description="Do not rank the stacks.",
    )

    @field_validator("output_root_uri", mode="before")
    def coerce_uri(cls, var):
        if isinstance(var, str):
            return DataUrl(var)
        if isinstance(var, Variable) and isinstance(var.value, str):
            var.value = DataUrl(var.value)
        return var


class Reg2DPostEvaluation(
    Task,
    input_model=Inputs,
    output_names=[
        "image_stacks",
        "transformations",
        "reference_stack",
        "ranked_stack_names",
        "output_configuration",
    ],
):
    """Given several stacks of images and their image transformations,
    determine the stack and list of transformations that results in the best registration.
    """

    def run(self):
        if self.inputs.skip:
            reference_stack, post_eval_rank, transformations = self._skip_eval()
        elif self.inputs.reference_stack:
            reference_stack, post_eval_rank, transformations = (
                self._eval_with_reference_stack()
            )
        else:
            reference_stack, post_eval_rank, transformations = (
                self._eval_without_reference_stack()
            )

        self.outputs.reference_stack = reference_stack
        self.outputs.ranked_stack_names = post_eval_rank
        self.outputs.transformations = transformations

        self.outputs.image_stacks = self.inputs.image_stacks
        output_configuration = self.get_input_value("output_configuration") or dict()
        output_configuration["reference_stack"] = reference_stack
        self.outputs.output_configuration = output_configuration

    def _skip_eval(self) -> _EvalResult:
        """Post evaluation is explicitly disabled."""
        transformations = self.inputs.transformations
        _count_unique_lists = _count_unique_transformation_lists(transformations)
        reference_stack = self.inputs.reference_stack

        if _count_unique_lists > 1:
            _logger.warning(
                "Reg2DPostEvaluation: expected 1 transformation but got %d. The images stacks will not be aligned in the same way.",
                _count_unique_lists,
            )

        return reference_stack, None, transformations

    def _eval_with_reference_stack(self) -> _EvalResult:
        """Post evaluation is not necessary because a reference stack is already defined."""
        transformations = self.inputs.transformations
        reference_stack = self.inputs.reference_stack

        if reference_stack not in transformations:
            raise ValueError(f"{reference_stack=} must be in {list(transformations)}")

        transformations = {
            name: transformations[reference_stack] for name in transformations
        }

        return reference_stack, None, transformations

    def _eval_without_reference_stack(self) -> _EvalResult:
        """Determine the reference stack by aligning all stacks a selecting
        the one with the best results.
        """
        transformations = self.inputs.transformations
        _count_unique_lists = _count_unique_transformation_lists(transformations)

        if _count_unique_lists <= 1:
            _logger.warning(
                "Reg2DPostEvaluation: skipped because the transformation list of each stack is identical."
            )
            return None, None, transformations

        with output_context() as ostacks:
            with input_context(self.inputs.image_stacks) as istacks:
                _ = apply_transformations(istacks, ostacks, transformations)
            ostacks = ostacks.data_for_input()

        output_root_uri = self.inputs.output_root_uri
        if output_root_uri:
            with output_context(output_root_uri) as ostacks_file:
                for name, data in ostacks.items():
                    ostacks_file.add_points(name, data)

        with input_context(ostacks) as ostacks:
            post_eval_rank = post_evaluation(ostacks, transformations)
            reference_stack = post_eval_rank[0]

        transformations = {
            name: transformations[reference_stack] for name in transformations
        }

        return reference_stack, post_eval_rank, transformations


def _count_unique_transformation_lists(
    transformations: Dict[str, List[Transformation]],
) -> int:
    if len(transformations) < 2:
        return len(transformations)
    all_lists = list(transformations.values())
    first_list = all_lists[0]
    count = 1
    count += sum(next_list != first_list for next_list in all_lists[1:])
    return count
