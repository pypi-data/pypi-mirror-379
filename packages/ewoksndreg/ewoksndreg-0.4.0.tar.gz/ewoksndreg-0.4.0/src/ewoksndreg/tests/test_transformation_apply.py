import numpy
import pytest

from ..io import data_for_registration
from ..io.input_stack import input_context
from ..io.output_stack import output_context
from ..transformation import apply_transformations
from ..transformation.homography import Homography

_HOMOGRAPHIES = {
    f"homography{'_'.join(k)}": v for k, v in Homography.get_subclass_items()
}


@pytest.mark.parametrize("homography", _HOMOGRAPHIES)
def test_apply_transformations(homography):
    image = data_for_registration.generate_image()
    image_stack, active, passive = data_for_registration.generate_image_stack(
        image, "translation", plot=0
    )
    data0 = data_for_registration.generate_image_stacks(image_stack)

    forward = [_HOMOGRAPHIES[homography](passive_matrix=M) for M in passive]
    backward = [_HOMOGRAPHIES[homography](passive_matrix=M) for M in active]
    forward = {name: forward for name in data0}
    backward = {name: backward for name in data0}

    data1 = dict()
    with output_context(data1) as ostacks:
        with input_context(data0) as istacks:
            _ = apply_transformations(istacks, ostacks, forward, interpolation_order=0)

    assert set(data1) == set(data0)

    data2 = dict()
    with output_context(data2) as ostacks:
        with input_context(data1) as istacks:
            _ = apply_transformations(istacks, ostacks, backward, interpolation_order=0)

    assert set(data2) == set(data1)

    for name, stack0 in data0.items():
        stack0 = numpy.asarray(stack0)
        stack2 = numpy.asarray(data2[name])
        idx = numpy.isnan(stack2)
        stack2[idx] = stack0[idx]
        numpy.testing.assert_allclose(stack2, stack0)


@pytest.mark.parametrize("homography", _HOMOGRAPHIES)
def test_apply_translation(homography):
    image = numpy.random.uniform(0.0, 10, (10, 10))

    transform = numpy.array([[1, 0, 6], [0, 1, -2], [0, 0, 1]], dtype=numpy.float64)
    forward = _HOMOGRAPHIES[homography](passive_matrix=transform)
    expected = numpy.zeros((10, 10))
    expected[0:4, 2:10] = image[6:10, 0:8]
    actual = forward.apply_data(image, cval=0)

    numpy.testing.assert_allclose(actual, expected)


@pytest.mark.parametrize("homography", _HOMOGRAPHIES)
def test_apply_coordinate(homography):
    nx, ny = numpy.meshgrid(numpy.arange(4, dtype=numpy.float64), numpy.arange(4))
    nx, ny = nx.flatten(), ny.flatten()
    matrix = numpy.identity(3)
    matrix[0:2, 2] = [-1, -3]

    forward = _HOMOGRAPHIES[homography](passive_matrix=matrix)
    res1 = forward.apply_coordinates(numpy.asarray([nx, ny]))
    numpy.testing.assert_allclose(res1, [nx + 1, ny + 3])

    matrix = numpy.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dtype=numpy.float64)

    forward = _HOMOGRAPHIES[homography](passive_matrix=matrix)
    res1 = forward.apply_coordinates(numpy.asarray([nx, ny]))

    numpy.testing.assert_allclose(res1, [ny, -nx], atol=numpy.finfo(numpy.float64).eps)
