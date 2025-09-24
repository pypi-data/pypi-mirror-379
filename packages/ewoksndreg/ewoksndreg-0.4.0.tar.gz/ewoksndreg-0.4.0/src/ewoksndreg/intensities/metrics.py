from typing import Optional

import numpy
from scipy.stats import entropy


def normalized_mutual_information_metric(
    image1: numpy.ndarray,
    image2: numpy.ndarray,
    bins: int = 100,
    image1_mask: Optional[numpy.ndarray] = None,
    image2_mask: Optional[numpy.ndarray] = None,
) -> float:
    """
    Given two images, the mutual information between the images is calculated based on an histogramm with 'bins' bins
    Masks can be given to exclude some parts of the images from the histogramm calculation
    Alternatively, two stacks of images can be given, where the mutual information per image pair is calculated and summed.
    """
    if image1.ndim == 2 and image2.ndim == 2:
        if image1_mask is not None:
            if image1.shape() != image1_mask.shape:
                raise ValueError("Masks must have same shape as image")
            image1 = image1[image1_mask]

        if image2_mask is not None:
            if image2.shape() != image2_mask.shape:
                raise ValueError("Masks must have same shape as image")
            image2 = image2[image2_mask]

        img1 = image1[numpy.logical_not(numpy.isnan(image2))]
        img2 = image2[numpy.logical_not(numpy.isnan(image2))]

        joint_bins, edgex, edgey = numpy.histogram2d(
            img1.flatten(), img2.flatten(), bins=bins
        )

        image1_entropy = entropy(numpy.sum(joint_bins, axis=0))
        image2_entropy = entropy(numpy.sum(joint_bins, axis=1))
        joint_entropy = entropy(joint_bins.flatten())

        if joint_entropy != 0:
            return (image1_entropy + image2_entropy) / joint_entropy
        else:
            return 0

    elif image1.ndim == 3 and image2.ndim == 3:
        NME_sum = 0
        for i in range(image1.shape[1]):
            NME_sum += normalized_mutual_information_metric(
                image1[i],
                image2[i],
                bins=bins,
                image1_mask=image1_mask[i],
                image2_mask=image2_mask[i],
            )
        return NME_sum

    else:
        raise ValueError("ndim of both images must be 2 or 3")


def mean_squared_metric(image1: numpy.ndarray, image2: numpy.ndarray) -> numpy.float64:
    mean = numpy.nanmean((image1 - image2) ** 2, dtype=numpy.float64)
    return mean if not numpy.isnan(mean) else numpy.finfo(numpy.float64).max
