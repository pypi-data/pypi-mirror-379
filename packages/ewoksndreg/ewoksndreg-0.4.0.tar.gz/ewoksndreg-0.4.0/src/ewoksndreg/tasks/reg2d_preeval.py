from typing import Optional

from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from pydantic import Field

from ..evaluation.evaluation import pre_evaluation
from ..io.input_stack import InputDataType
from ..io.input_stack import input_context


class Inputs(BaseInputModel):
    image_stacks: InputDataType = Field(
        ...,
        description="Image stacks as a dictionary of numpy arrays or list of HDF5 dataset URI's.",
        examples=[
            {
                "stack1": "/path/to/file.h5::/entry/process/results/parameters/Ca-K",
                "stack2": "/path/to/file.h5::/entry/process/results/parameters/Fe-K",
            },
            {"stack1": [[0, 0, 0], [1, 1, 1], [2, 2, 2]]},
        ],
    )
    reference_stack: Optional[str] = Field(
        None,
        description="Force select stack.",
        examples=["stack1", "stack2"],
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


class Reg2DPreEvaluation(
    Task,
    input_model=Inputs,
    output_names=[
        "image_stacks",
        "reference_stack",
        "ranked_stack_names",
        "output_configuration",
    ],
):
    """Given several stacks of images requiring the same alignment,
    determine the stack which is most suitable to get a correct alignment.
    """

    def run(self):
        reference_stack = self.inputs.reference_stack
        image_stacks = self.inputs.image_stacks

        if self.inputs.skip:
            self.outputs.reference_stack = reference_stack
            self.outputs.ranked_stack_names = None
        elif reference_stack:
            if reference_stack not in image_stacks:
                raise ValueError(f"{reference_stack=} must be in {list(image_stacks)}")
            self.outputs.reference_stack = reference_stack
            self.outputs.ranked_stack_names = None
        else:
            with input_context(image_stacks) as stacks:
                pre_eval_rank = pre_evaluation(stacks)
            self.outputs.reference_stack = pre_eval_rank[0]
            self.outputs.ranked_stack_names = pre_eval_rank
        self.outputs.image_stacks = image_stacks

        output_configuration = self.get_input_value("output_configuration") or dict()
        output_configuration["reference_stack"] = reference_stack
        self.outputs.output_configuration = output_configuration
