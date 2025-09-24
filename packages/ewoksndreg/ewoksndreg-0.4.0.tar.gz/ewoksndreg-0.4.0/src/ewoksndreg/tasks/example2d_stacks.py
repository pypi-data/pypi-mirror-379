from typing import Optional
from typing import Sequence

from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from pydantic import Field

from ..io import data_for_registration
from ..transformation.numpy_backend import NumpyHomography
from ..transformation.types import TransformationType

try:
    from ..transformation.simpleitk_backend import SimpleITKTransformation
except ImportError:
    SimpleITKTransformation = None


class Inputs(BaseInputModel):
    name: str = Field(..., description="Name of the image", examples=["astronaut"])
    transformation_type: TransformationType = Field(
        ..., description="Transformation type", examples=["translation", "rigid"]
    )
    shape: Optional[Sequence[int]] = Field(
        None,
        description="Image shape",
        examples=[(200, 220)],
        min_length=2,
        max_length=2,
    )
    nimages: Optional[int] = Field(None, description="Number of images per stack")
    nstacks: Optional[int] = Field(None, description="Number of image stacks")
    noise: Optional[int] = Field(
        None, description="Number of image stacks", examples=["s&p", "uniform"]
    )


class Example2DStacks(
    Task,
    input_model=Inputs,
    output_names=["image_stacks", "transformations"],
):
    """Generate one or more stacks of transformed images to test registration methods."""

    def run(self):
        image = data_for_registration.generate_image(name=self.inputs.name)
        image_stacks, _, passive_matrices = data_for_registration.generate_image_stack(
            image,
            self.inputs.transformation_type,
            shape=self.inputs.shape,
            nimages=self.inputs.nimages,
        )
        image_stacks = data_for_registration.generate_image_stacks(
            image_stacks, self.inputs.nstacks, noise=self.inputs.noise
        )

        if self.inputs.transformation_type in ["displacement_field", "bspline"]:
            if SimpleITKTransformation is None:
                raise ValueError(
                    "displacement field transforms cannot be generated without SimpleITK"
                )
            transformations = [
                SimpleITKTransformation(displacement_field=d) for d in passive_matrices
            ]
        else:
            transformations = [NumpyHomography(M) for M in passive_matrices]

        self.outputs.image_stacks = image_stacks
        self.outputs.transformations = {name: transformations for name in image_stacks}
