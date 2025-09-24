from typing import Tuple
from typing import Union

import numpy


def resize(
    image: numpy.ndarray, out_shape: Tuple[int], order: int = 0
) -> numpy.ndarray:
    if image.ndim != len(out_shape):
        raise ValueError("New shape must have same dimensionality as image")

    in_shape = image.shape

    ranges = [
        numpy.arange(0, shp, shp / out_shape[i]) for i, shp in enumerate(in_shape)
    ]
    X = numpy.meshgrid(*ranges[::-1])
    X = numpy.array(X).astype(int)
    X = X[::-1]
    if order == 0:
        result = image[X[0], X[1]]
        result = numpy.reshape(result, out_shape)
        return result


def rescale(
    image: numpy.ndarray, factor: Union[float, int, Tuple], order: int = 0
) -> numpy.ndarray:
    shp = image.shape

    factor = float(factor) if isinstance(factor, int) else factor

    if isinstance(factor, float):
        factor = (factor,) * image.ndim

    if len(factor) != image.ndim:
        raise ValueError(
            f"{len(factor)} scaling factors must match image dimension {image.ndim}"
        )

    new_shape = tuple([int(x * factor[i]) for i, x in enumerate(shp)])

    return resize(image, new_shape, order=order)
