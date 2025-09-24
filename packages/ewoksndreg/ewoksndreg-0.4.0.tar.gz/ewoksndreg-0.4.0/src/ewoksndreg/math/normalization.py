from typing import List
from typing import Union

import numpy


def range_normalization(image: Union[numpy.ndarray, List]):
    """
    Scale image intensities between [0,1]
    """
    image = numpy.asarray(image)
    mi = numpy.nanmin(image)
    ma = numpy.nanmax(image)
    if mi == ma:
        return image
    return (image - mi) / (ma - mi)


def stack_range_normalization(image_stacks: numpy.ndarray):
    """
    Scale intensities of each image in a stack of images between [0,1].
    """
    return numpy.stack([range_normalization(image) for image in image_stacks])
