import numpy

from ..transformation.numpy_backend import homography_transform_bounding_box
from ..transformation.numpy_backend import homography_transform_coordinates
from ..transformation.numpy_backend import homography_transform_data


def test_homography_transform_coordinates():
    from_coordinates = numpy.random.uniform(-10, 10, (2, 10))

    active_expected = numpy.array(
        [[0, 1, 3], [1, 0, -2], [0, 0, 1]]
    )  # transpose + translate
    expected1 = from_coordinates.copy()
    expected1 = expected1[::-1, ...]  # transpose
    expected1 += numpy.array([[3], [-2]])  # translate

    active_actual = numpy.array(
        [[-1, 0, -1], [0, -1, 3], [0, 0, 1]]
    )  # inverse + translate
    expected2 = from_coordinates.copy()
    expected2 = -expected2  # inverse
    expected2 += numpy.array([[-1], [3]])  # translate

    active = numpy.stack([active_expected, active_actual], axis=0)
    expected = numpy.stack([expected1, expected2], axis=0)

    to_coordinates = homography_transform_coordinates(active_expected, from_coordinates)
    numpy.testing.assert_allclose(to_coordinates, expected1)

    to_coordinates = homography_transform_coordinates(active_actual, from_coordinates)
    numpy.testing.assert_allclose(to_coordinates, expected2)

    to_coordinates = homography_transform_coordinates(active, from_coordinates)
    numpy.testing.assert_allclose(to_coordinates, expected)


def test_homography_transform_bounding_box():
    shape = (10, 20)
    active_expected = numpy.array(
        [[0, 1, 3], [1, 0, -2], [0, 0, 1]]
    )  # transpose + translate
    expected_xmin1 = numpy.array([3, -2])
    expected_xmax1 = numpy.array([20 + 3, 10 - 2])

    active_actual = numpy.array(
        [[-1, 0, -1], [0, -1, 3], [0, 0, 1]]
    )  # inverse + translate
    expected_xmin2 = numpy.array([-10 - 1, -20 + 3])
    expected_xmax2 = expected_xmin2 + numpy.array([10, 20])

    active = numpy.stack([active_expected, active_actual], axis=0)
    expected_xmin = numpy.stack([expected_xmin1, expected_xmin2], axis=0)
    expected_xmax = numpy.stack([expected_xmax1, expected_xmax2], axis=0)

    to_xmin, to_xmax = homography_transform_bounding_box(active_expected, shape)
    numpy.testing.assert_allclose(to_xmin, expected_xmin1)
    numpy.testing.assert_allclose(to_xmax, expected_xmax1)

    to_xmin, to_xmax = homography_transform_bounding_box(active_actual, shape)
    numpy.testing.assert_allclose(to_xmin, expected_xmin2)
    numpy.testing.assert_allclose(to_xmax, expected_xmax2)

    to_xmin, to_xmax = homography_transform_bounding_box(active, shape)
    numpy.testing.assert_allclose(to_xmin, expected_xmin)
    numpy.testing.assert_allclose(to_xmax, expected_xmax)


def test_homography_transform_data():
    from_img = numpy.zeros((10, 20))
    from_img[5, 3] = 1

    active_expected = numpy.array(
        [[0, 1, 5], [1, 0, 8], [0, 0, 1]]
    )  # transpose + translate
    expected1 = numpy.zeros((10, 20))
    expected1[3 + 5, 5 + 8] = 1

    active_actual = numpy.array(
        [[-1, 0, 8], [0, -1, 10], [0, 0, 1]]
    )  # inverse + translate
    expected2 = numpy.zeros((10, 20))
    expected2[-5 + 8, -3 + 10] = 1

    passive_expected = numpy.linalg.inv(active_expected)
    passive_actual = numpy.linalg.inv(active_actual)

    to_img = homography_transform_data(passive_expected, from_img, cval=0)
    numpy.testing.assert_allclose(to_img, expected1)

    to_img = homography_transform_data(passive_actual, from_img, cval=0)
    numpy.testing.assert_allclose(to_img, expected2)
