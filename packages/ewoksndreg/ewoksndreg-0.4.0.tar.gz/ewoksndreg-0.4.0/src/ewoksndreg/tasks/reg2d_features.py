from typing import Optional
from typing import Union

import numpy
from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from pydantic import Field

from ..features import registration
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
    detector: RegistryIdType = Field(
        ...,
        description="Method to detect and describe feature points in an image.",
        examples=["Sift-Silx", "Sift-SciKitImage", "Orb-SciKitImage"],
    )
    matcher: RegistryIdType = Field(
        ...,
        description="Method to build correspondence between the feature points in two images.",
        examples=["Descriptor-Silx", "Descriptor-SciKitImage"],
    )
    mapper: RegistryIdType = Field(
        ...,
        description="Method to find parameters of the transformation between the matches.",
        examples=["LstSq-Numpy", "LstSq-SciPy", "Ransac-SciKitImage"],
    )
    transformation_type: TransformationType = Field(
        ...,
        description="Type of transformation between the matches.",
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
    mask: Optional[numpy.ndarray] = Field(
        None,
        description="Boolean image mask applied to the image before calculating the transformation (False means masked-off).",
        examples=[[[True, True, True], [True, True, True], [False, True, True]]],
    )
    output_configuration: Optional[dict] = Field(
        None,
        description="Registration configuration parameters to be saved.",
        examples=[{"param1": 0, "param2": 1}],
    )


class Reg2DFeatures(
    Task,
    input_model=Inputs,
    output_names=[
        "image_stacks",
        "transformations",
        "reference_stack",
        "features",
        "matches",
        "output_configuration",
    ],
):
    """Use a feature-based registration method to calculate transformations between the images in one or more stacks."""

    def run(self):
        detector = registration.FeatureDetector.get_subclass(self.inputs.detector)(
            mask=self.inputs.mask
        )
        matcher = registration.FeatureMatching.get_subclass(self.inputs.matcher)()
        mapper = registration.FeatureMapping.get_subclass(self.inputs.mapper)(
            self.inputs.transformation_type
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
            features = registration.detect_features(stacks, detector)
            matches = registration.match_features(
                stacks,
                features,
                matcher,
                reference_image=self.inputs.reference_image,
            )
            transformations = registration.transformations_from_features(
                matches, mapper
            )

        if reference_stack:
            names = list(self.inputs.image_stacks)
            transformations = {name: transformations[reference_stack] for name in names}
            features = {name: features[reference_stack] for name in names}
            matches = {name: matches[reference_stack] for name in names}

        self.outputs.transformations = transformations
        self.outputs.reference_stack = reference_stack
        self.outputs.features = features
        self.outputs.matches = matches
        self.outputs.image_stacks = self.inputs.image_stacks

        output_configuration = self.get_input_value("output_configuration") or dict()
        output_configuration["detector"] = str(detector.get_subclass_id())
        output_configuration["matcher"] = str(matcher.get_subclass_id())
        output_configuration["mapper"] = str(mapper.get_subclass_id())
        output_configuration["transformation_type"] = mapper.transformation_type.value
        output_configuration["reference_image"] = self.inputs.reference_image
        output_configuration["reference_stack"] = reference_stack
        self.outputs.output_configuration = output_configuration
