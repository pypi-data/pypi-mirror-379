from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Union

import numpy

from ..io.input_stack import InputStacks
from ..math.filter import preprocess
from ..math.indices import get_positive_index
from ..transformation.base import Transformation
from .base import IntensityMapping


def calculate_transformations(
    input_stacks: InputStacks,
    mapper: IntensityMapping,
    include: Optional[Sequence[int]] = None,
    reference_image: Union[int, float] = 0,
    block_size: int = 1,
    preprocessing_options: Optional[Dict] = None,
) -> Dict[str, List[Transformation]]:
    """
    Uses the mapper to calculate the transformation between the reference image and all other images in the stack.

    param input_stacks: InputStacks of all the images
    param mapper: An IntensityMapper to calculate transformations between the images
    param include: Indices of images to include for the registration. Default: all.
    param reference_image: The index of the reference image, if 0.5 the reference will be the middle of the stack.
    param block_size: Included images get partitioned into blocks.Every image in one block gets aligned to the first element in the block.
                      The first elements of each block get sequentially aligned to the reference
    """
    stack_len = input_stacks.stack_len
    if include is None:
        include = list(range(stack_len))
    if block_size <= 0:
        block_size = 1
    reference_image = get_positive_index(reference_image, stack_len)
    # ref_index is the index of the reference in include, as include might not contain all indices
    ref_index = include.index(reference_image)
    if preprocessing_options is None:
        preprocessing_options = {}

    transformations = dict()

    for name, input_stack in input_stacks.items():
        ref_image0 = preprocess(input_stack[reference_image], **preprocessing_options)

        # calculate all transformations up to reference
        # counter holds the position in one block, so goes from 0 to block_size-1
        indices = list(reversed(include[:ref_index]))
        transformations_ = [mapper.identity(ref_image0.ndim)]
        transformations_ += _calculate_transformations(
            input_stack, indices, mapper, ref_image0, block_size, preprocessing_options
        )
        transformations_ = list(reversed(transformations_))

        # calculate all transformations after reference
        indices = include[ref_index + 1 :]
        transformations_ += _calculate_transformations(
            input_stack, indices, mapper, ref_image0, block_size, preprocessing_options
        )

        transformations[name] = transformations_
    return transformations


def _calculate_transformations(
    input_stack: numpy.ndarray,
    indices: List[int],
    mapper: IntensityMapping,
    ref_image: numpy.ndarray,
    block_size: int,
    preprocessing_options: dict,
):
    counter = 0
    dim = ref_image.ndim
    current_ref_transfo = mapper.identity(dim)
    transformations = list()
    for i in indices:
        next_img = preprocess(input_stack[i], **preprocessing_options)
        next_transfo = mapper.calculate(next_img, ref_image) @ current_ref_transfo
        transformations.append(next_transfo)
        counter += 1
        if counter % block_size == 0:
            ref_image = next_img
            current_ref_transfo = next_transfo
            counter = 0
    return transformations
