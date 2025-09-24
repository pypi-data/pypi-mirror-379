from typing import List
from typing import Optional
from typing import Tuple

import numpy

CropLimitsType = Optional[List[Tuple[int, int]]]


def array_crop_limits(
    array: numpy.ndarray,
) -> CropLimitsType:
    """Calculate array index limits for each dimension to strip invalid
    value blocks at the edges.

    :param array:
    :returns: A 2-tuple for each array dimension `[(lo0, hi0), (lo1, hi1), ...]`
              or `None` when the cropped sub-array is empty.
    """
    valid = numpy.isfinite(array)
    if not valid.any():
        return None

    idx_valid = numpy.where(valid)

    for idx in idx_valid:
        if idx.size == 0:
            return None

    return [(int(idx.min()), int(idx.max())) for idx in idx_valid]


def merge_crop_limits(
    all_limits: List[CropLimitsType], intersection: bool
) -> CropLimitsType:
    """Merge several array limits either by taking the intersection or the envelop.

    :param all_limits: several results of `array_crop_limits`
    :returns: A 2-tuple for each array dimension `[(lo0, hi0), (lo1, hi1), ...]`
              or `None` when the merged limits box is empty.
    """
    if None in all_limits:
        if intersection:
            return None
        else:
            all_limits = [limits for limits in all_limits if limits is not None]

    if not all_limits:
        return None

    all_lows = [[limit[0] for limit in limits] for limits in all_limits]
    all_highs = [[limit[1] for limit in limits] for limits in all_limits]

    if intersection:
        overall_low = numpy.max(all_lows, axis=0)
        overall_high = numpy.min(all_highs, axis=0)
    else:
        overall_low = numpy.min(all_lows, axis=0)
        overall_high = numpy.max(all_highs, axis=0)

    if (overall_low >= overall_high).any():
        return None

    return list(zip(overall_low.tolist(), overall_high.tolist()))
