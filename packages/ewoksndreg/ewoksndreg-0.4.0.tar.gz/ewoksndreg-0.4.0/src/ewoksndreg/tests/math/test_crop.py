import numpy

from ...math import crop


def test_crop_array_limits():
    # NaN's at the edge of one dimension
    array = numpy.zeros((15, 15))
    array[0:2, :] = numpy.nan
    limits = crop.array_crop_limits(array)
    assert limits == [(2, 14), (0, 14)]

    # NaN's at the edge of one dimension
    # and inside another dimension
    array = numpy.zeros((15, 15))
    array[0:2, :] = numpy.nan
    array[:, 10:12] = numpy.nan
    limits = crop.array_crop_limits(array)
    assert limits == [(2, 14), (0, 14)]

    # NaN's at the edge of two dimension
    array = numpy.zeros((15, 15))
    array[0:2, :] = numpy.nan
    array[:, 10:] = numpy.nan
    limits = crop.array_crop_limits(array)
    assert limits == [(2, 14), (0, 9)]

    # Empty crop limits
    array = numpy.full((15, 15), numpy.nan)
    limits = crop.array_crop_limits(array)
    assert limits is None


def test_merge_crop_limits():
    # Intersection and envelop of two limits
    limits1 = [(5, 11), (0, 9)]
    limits2 = [(2, 10), (1, 13)]
    limits = crop.merge_crop_limits([limits1, limits2], intersection=True)
    assert limits == [(5, 10), (1, 9)]
    limits = crop.merge_crop_limits([limits1, limits2], intersection=False)
    assert limits == [(2, 11), (0, 13)]

    # No intersection alone one dimension
    limits1 = [(2, 5), (0, 9)]
    limits2 = [(7, 10), (1, 13)]
    limits = crop.merge_crop_limits([limits1, limits2], intersection=True)
    assert limits is None
    limits = crop.merge_crop_limits([limits1, limits2], intersection=False)
    assert limits == [(2, 10), (0, 13)]

    # One of the crop limits is empty
    limits1 = [(2, 5), (0, 9)]
    limits2 = [(7, 10), (1, 13)]
    limits3 = None
    limits = crop.merge_crop_limits([limits1, limits2, limits3], intersection=True)
    assert limits is None
    limits = crop.merge_crop_limits([limits1, limits2, limits3], intersection=False)
    assert limits == [(2, 10), (0, 13)]
