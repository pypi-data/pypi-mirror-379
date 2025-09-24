import logging
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

import h5py
import numpy

from ..io.input_stack import InputStacks
from ..io.output_stack import OutputStacks
from ..math import crop
from .base import Transformation

logger = logging.getLogger(__name__)


def apply_transformations(
    input_stacks: InputStacks,
    output_stacks: OutputStacks,
    transformations: Dict[str, Transformation],
    cval: int = numpy.nan,
    crop: bool = False,
    interpolation_order: int = 1,
) -> Optional[Tuple[slice, ...]]:
    if set(input_stacks) != set(transformations):
        raise ValueError(
            f"Stack names {set(input_stacks)} are not equal to transformation names {set(transformations)}"
        )
    if crop and not numpy.isnan(cval):
        logger.warning(f"Cropping is skipped for {cval=}")
        crop = False

    transformed_stacks = {}
    for name, input_stack in input_stacks.items():
        transformed_stack = _apply_transformations(
            input_stack,
            transformations[name],
            cval=cval,
            interpolation_order=interpolation_order,
        )
        transformed_stacks[name] = transformed_stack

    if crop:
        transformed_stacks, image_crop_idx = _crop_stacks(transformed_stacks)
    else:
        image_crop_idx = None

    for name, transformed_stack in transformed_stacks.items():
        output_stacks.add_points(name, transformed_stack)
    return image_crop_idx


def _apply_transformations(
    input_stack: Union[Sequence[numpy.ndarray], h5py.Dataset],
    transformations: List[Transformation],
    cval: int = numpy.nan,
    interpolation_order: int = 1,
) -> List[numpy.ndarray]:
    if len(input_stack) != len(transformations):
        raise ValueError("Number of images and number of transformations must be equal")

    img_shape = input_stack[0].shape
    if len(img_shape) != 2:
        raise ValueError("Requires a stack of 2D images")

    transformed_stack = list()
    for image, transformation in zip(input_stack, transformations):
        transformed = transformation.apply_data(
            image,
            offset=None,
            shape=None,
            cval=cval,
            interpolation_order=interpolation_order,
        )
        transformed_stack.append(transformed)

    return transformed_stack


def _crop_stacks(
    transformed_stacks: Dict[str, List[numpy.ndarray]],
) -> Tuple[Dict[str, List[numpy.ndarray]], Tuple[slice, ...]]:
    all_intersection_limits = []
    for transformed_stack in transformed_stacks.values():
        # Find the intersection between a stack of transformed images.
        image_limits = [crop.array_crop_limits(image) for image in transformed_stack]
        intersection_limits = crop.merge_crop_limits(image_limits, intersection=True)
        if intersection_limits is None:
            # Transformed images don't have an intersection.
            continue
        all_intersection_limits.append(intersection_limits)

    # Find the envelop of the intersection regions of all image stacks.
    cropped_limits = crop.merge_crop_limits(all_intersection_limits, intersection=False)
    if cropped_limits is None:
        logger.warning("Cropping is skipped because nothing would be left")
        return transformed_stacks, None

    # Envelop might cover the entire original range.
    any_stack = next(iter(transformed_stacks.values()))
    original_limits = [(0, n - 1) for n in any_stack[0].shape]
    if original_limits == cropped_limits:
        logger.warning(
            "Cropping is skipped because nothing can be trimmed at the edges"
        )
        return transformed_stacks, None

    # Apply crop limits.
    logger.info("Images are cropped from %s to %s", original_limits, cropped_limits)
    image_crop_idx = tuple(slice(lo, hi + 1) for lo, hi in cropped_limits)
    transformed_stacks = {
        name: [transformed[image_crop_idx] for transformed in transformed_stack]
        for name, transformed_stack in transformed_stacks.items()
    }
    return transformed_stacks, image_crop_idx
