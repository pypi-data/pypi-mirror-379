from typing import Sequence
from typing import Tuple

import numpy
from skimage.filters import gaussian

from ..math.normalization import range_normalization
from ..transformation.homography import Homography


def noisy_eval(stack: numpy.ndarray) -> float:
    """
    Determines how noisy the images in the given stack are.

    This is determined by denoising the image with a gaussian filter and comparing the variance before and after.
    Return value is big if the denoising decreased the variance a lot.

    :param stack: array of shape [N,H,W]
    """
    total = 0
    for image in stack:
        image = range_normalization(image)
        var = image.var()
        newvar = gaussian(image).var()
        total += var / newvar
    return total / len(stack)


def peak_eval(stack: numpy.ndarray, reference_image: int) -> float:
    """
    Calculate a measure of how reliable a stack of images is to determine the transformations between the images.

    The measure is based on phase cross correlation which generates an image with the peak with coordinates corresponding to the shift.
    This eval calculates how distinguished this peak is by comparing it to the mean of the phase correlation image.

    :param stack: the aligned or unaligned stack
    :param reference_image: reference image for phase cross correlation
    :returns: reliablility measure (smaller value means more reliable)
    """
    total = 0
    ref = range_normalization(stack[reference_image])
    fft_ref = numpy.fft.fft2(ref)
    for image in stack:
        fft = numpy.fft.fft2(range_normalization(image))
        prod = fft_ref * fft.conj()
        denom = numpy.abs(prod)
        with numpy.errstate(invalid="ignore"):
            safe_prod = numpy.where(denom != 0, prod / denom, 0)
        peak = numpy.abs(numpy.fft.ifft2(safe_prod))
        total += peak.mean() - peak.max()
    return total / len(stack)


def mse_eval(stack: numpy.ndarray, reference_image: int) -> float:
    """
    Evaluate success based on the remaining mse error after alignment

    :param stack: Aligned stack of images with pixel values in [0,1]
    """
    total = 0
    for image in stack:
        total += numpy.nanmean((stack[reference_image] - image) ** 2)
    return total / len(stack)


def smoothness_eval(
    transformations: Sequence[Homography], img_size: Tuple[int, ...]
) -> float:
    """
    Evaluates the transformations by smoothness.

    This is done by transforming the coordinates of the corners of the image and looking at how much these change by transformations

    :param transformations: Sequence of Homographies
    :param img_size: Shape of the images that these transformations are meant for
    """
    i, j = img_size
    points = numpy.array([[0, 0, i, i], [0, j, 0, j]])
    corners_after = [transfo.apply_coordinates(points) for transfo in transformations]
    corners_diff = [
        (corners_after[i] - corners_after[i - 1]) for i in range(1, len(corners_after))
    ]
    size = numpy.array([[i], [j]])
    corners_diff = [c / size for c in corners_diff]
    corners_diff = numpy.linalg.norm(corners_diff, axis=1)
    return numpy.mean(corners_diff)
