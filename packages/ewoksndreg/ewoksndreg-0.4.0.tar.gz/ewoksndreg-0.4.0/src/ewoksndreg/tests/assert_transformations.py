"""Compare the actual and desired transformations based on the values
of the matrix representation and the pixel coordinates after applying
the transformation. In both cases they are considered close enough when

.. code:: python

    absolute(actual - desired) <= (atol + rtol * absolute(desired))
"""

from typing import Dict
from typing import List

import numpy

from ..transformation.base import Transformation
from ..transformation.numpy_backend import NumpyHomography


def assert_allclose_transformations_dicts(
    all_actual_transformations: Dict[str, List[Transformation]],
    all_expected_transformations: Dict[str, List[Transformation]],
    rtol: float = 0.1,
    atol: float = 0.0,
    rtol_pixels: float = 0.0,
    atol_pixels: float = 0.1,
) -> None:
    assert set(all_expected_transformations) == set(all_actual_transformations)
    for name, actual_transformations in all_actual_transformations.items():
        expected_transformations = all_expected_transformations[name]
        assert len(actual_transformations) == len(expected_transformations)
        for actual_transformation, expected_transformation in zip(
            actual_transformations,
            expected_transformations,
        ):
            _compare_transformations_based_on_values(
                actual_transformation, expected_transformation, rtol=rtol, atol=atol
            )
            _compare_transformations_based_on_coordinates(
                actual_transformation,
                expected_transformation,
                rtol=rtol_pixels,
                atol=atol_pixels,
            )


def assert_allclose_transformations(
    all_actual_transformations: Dict[str, List[Transformation]],
    active_expected: numpy.ndarray,
    passive_expected: numpy.ndarray,
    rtol: float = 0.01,
    atol: float = 0.0,
    rtol_pixels: float = 0.0,
    atol_pixels: float = 0.1,
) -> None:
    for actual_transformations in all_actual_transformations.values():
        assert len(actual_transformations) == len(active_expected)
        for actual_transformation, active, passive in zip(
            actual_transformations, active_expected, passive_expected
        ):
            _assert_transformation_based_on_values(
                actual_transformation, active, passive, rtol=rtol, atol=atol
            )
            _assert_transformation_based_on_coordinates(
                actual_transformation, passive, rtol=rtol_pixels, atol=atol_pixels
            )


def _compare_transformations_based_on_values(
    actual_transformation: Transformation, expected_transformation: Transformation, **kw
) -> None:
    numpy.testing.assert_allclose(
        actual_transformation.passive_matrix,
        expected_transformation.passive_matrix,
        **kw,
    )
    numpy.testing.assert_allclose(
        actual_transformation.active_matrix, expected_transformation.active_matrix, **kw
    )


def _assert_transformation_based_on_values(
    actual_transformation: Transformation,
    active_expected: numpy.ndarray,
    passive_expected: numpy.ndarray,
    **kw,
) -> None:
    if actual_transformation.is_homography():
        numpy.testing.assert_allclose(
            actual_transformation.passive_matrix, passive_expected, **kw
        )
        numpy.testing.assert_allclose(
            actual_transformation.active_matrix, active_expected, **kw
        )


def _compare_transformations_based_on_coordinates(
    actual_transformation: Transformation, expected_transformation: Transformation, **kw
) -> None:
    coord0, coord1 = numpy.mgrid[0:100:10, 0:100:10]
    coord0, coord1 = coord0.astype(numpy.float64), coord1.astype(numpy.float64)
    xy = numpy.asarray([coord0.flatten(), coord1.flatten()])
    actual_xy = actual_transformation.apply_coordinates(xy)
    expected_xy = expected_transformation.apply_coordinates(xy)
    numpy.testing.assert_allclose(actual_xy, expected_xy, **kw)


def _assert_transformation_based_on_coordinates(
    actual_transformation: Transformation, passive_expected: numpy.ndarray, **kw
) -> None:
    coord0, coord1 = numpy.mgrid[0:100:10, 0:100:10]
    coord0, coord1 = coord0.astype(numpy.float64), coord1.astype(numpy.float64)
    coord = numpy.asarray([coord0.flatten(), coord1.flatten()])
    actual_coord = actual_transformation.apply_coordinates(coord)
    expected_coord = NumpyHomography(passive_expected).apply_coordinates(coord)
    numpy.testing.assert_allclose(actual_coord, expected_coord, **kw)
