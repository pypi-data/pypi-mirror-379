from typing import Optional
from typing import Union

import numpy
from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from pydantic import Field

from ..intensities import registration
from ..io.input_stack import InputDataType
from ..io.input_stack import input_context
from ..registry import RegistryIdType
from ..transformation.types import TransformationType


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
    mapper: RegistryIdType = Field(
        ...,
        description="Method to find parameters of the transformation between the image intensities.",
        examples=["LstSq-Numpy", "LstSq-SciPy", "Ransac-SciKitImage"],
    )
    transformation_type: TransformationType = Field(
        ...,
        description="Type of transformation between the intensities.",
        examples=["Translation", "Rigid", "Affine"],
    )
    reference_image: Union[int, float] = Field(
        0,
        description="The index of the reference image in the stack (0.5 is the middle of the stack)."
        "The calculated transformations will be relative to this image.",
        examples=[0, -1, 0.5],
    )
    reference_stack: Optional[str] = Field(
        None,
        description="Transformations of all stacks is based on the image registration of this stack.",
        examples=["stack1", "stack2"],
    )
    block_size: int = Field(
        1,
        description="Register images within blocks and then register with respect to the reference. "
        "Pair-wise registration can be done with `block_size=2`."
        "Useful when images drift alot over the entire stack.",
        examples=[2, 5],
    )
    mask: Optional[numpy.ndarray] = Field(
        None,
        description="Boolean image mask applied to the image before calculating the transformation (False means masked-off).",
        examples=[[[True, True, True], [True, True, True], [False, True, True]]],
    )
    preprocessing_options: Optional[dict] = Field(
        None,
        description="Filters, windows and other operations that will be applied to the image before calculating the transformation.",
        examples=[{"apply_filter": "median"}],
    )
    mapper_options: Optional[dict] = Field(
        None,
        description="Method dependent parameters.",
        examples=None,
    )
    output_configuration: Optional[dict] = Field(
        None,
        description="Registration configuration parameters to be saved.",
        examples=[{"param1": 0, "param2": 1}],
    )


class Reg2DIntensities(
    Task,
    input_model=Inputs,
    output_names=[
        "image_stacks",
        "transformations",
        "reference_stack",
        "output_configuration",
    ],
):
    """Use an intensity-based registration method to calculate transformations between the images in one or more stacks."""

    def run(self):
        mapper_options = self.inputs.mapper_options or dict()
        mapper = registration.IntensityMapping.get_subclass(self.inputs.mapper)(
            transfo_type=self.inputs.transformation_type,
            mask=self.inputs.mask,
            **mapper_options,
        )

        stacks_to_align = self.inputs.image_stacks
        reference_stack = self.inputs.reference_stack
        if reference_stack:
            if reference_stack not in stacks_to_align:
                raise ValueError(
                    f"{reference_stack=} must be in {list(stacks_to_align)}"
                )
            stacks_to_align = {reference_stack: stacks_to_align[reference_stack]}

        with input_context(stacks_to_align) as stacks:
            transformations = registration.calculate_transformations(
                stacks,
                mapper,
                reference_image=self.inputs.reference_image,
                block_size=self.inputs.block_size,
                preprocessing_options=self.inputs.preprocessing_options,
            )

        if reference_stack:
            names = list(self.inputs.image_stacks)
            transformations = {name: transformations[reference_stack] for name in names}

        self.outputs.transformations = transformations
        self.outputs.reference_stack = reference_stack
        self.outputs.image_stacks = self.inputs.image_stacks

        output_configuration = self.get_input_value("output_configuration") or dict()
        output_configuration["mapper"] = str(mapper.get_subclass_id())
        output_configuration["mapper_options"] = mapper_options
        output_configuration["transformation_type"] = mapper.transformation_type.name
        output_configuration["reference_image"] = self.inputs.reference_image
        output_configuration["reference_stack"] = reference_stack
        output_configuration["preprocessing_options"] = (
            self.inputs.preprocessing_options
        )
        output_configuration["block_size"] = self.inputs.block_size
        self.outputs.output_configuration = output_configuration
