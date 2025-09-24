import numpy
import pytest

from ..intensities import registration
from ..io import data_for_registration
from ..io.input_stack import InputStacksNumpy
from .assert_transformations import assert_allclose_transformations

_MAPPERS = {
    f"mapper{'_'.join(k)}": v
    for k, v in registration.IntensityMapping.get_subclass_items()
}


@pytest.mark.parametrize("mapper", _MAPPERS)
@pytest.mark.parametrize(
    "transfo_type",
    ["translation", "rigid", "affine", "similarity"],
)
def test_intensity_registration(transfo_type, mapper):
    if transfo_type not in _MAPPERS[mapper].SUPPORTED_TRANSFORMATIONS:
        pytest.skip(f"transformation type {transfo_type} not supported by {mapper}")

    image = data_for_registration.generate_image()
    image_stack, active_expected, passive_expected = (
        data_for_registration.generate_image_stack(image, transfo_type, plot=0)
    )
    image_stacks = data_for_registration.generate_image_stacks(image_stack, nstacks=1)

    mapper = _MAPPERS[mapper](transfo_type=transfo_type)

    with InputStacksNumpy(image_stacks) as stacks:
        transformations = registration.calculate_transformations(stacks, mapper)

    assert_allclose_transformations(
        transformations,
        active_expected,
        passive_expected,
        rtol=0.1,
        atol=0.1,
        rtol_pixels=0.1,
        atol_pixels=0.4,
    )


@pytest.mark.parametrize("mapper", _MAPPERS)
@pytest.mark.parametrize("transfo_type", ["translation", "affine"])
def test_intensity_registration_block(transfo_type, mapper):
    if transfo_type not in _MAPPERS[mapper].SUPPORTED_TRANSFORMATIONS:
        pytest.skip(f"transformation type {transfo_type} not supported by {mapper}")

    image = data_for_registration.generate_image()
    image_stack, active_expected, passive_expected = (
        data_for_registration.generate_image_stack(
            image, transfo_type, nimages=7, plot=0
        )
    )
    image_stacks = data_for_registration.generate_image_stacks(image_stack, nstacks=1)

    mapper = _MAPPERS[mapper](transfo_type=transfo_type)

    with InputStacksNumpy(image_stacks) as stacks:
        transformations = registration.calculate_transformations(
            stacks, mapper, include=[0, 1, 2, 4, 5, 6], reference_image=0, block_size=3
        )

    for transformations_ in transformations.values():
        assert len(transformations_) == 6
    active_expected.pop(3)
    passive_expected.pop(3)

    assert_allclose_transformations(
        transformations,
        active_expected,
        passive_expected,
        rtol=0.01,
        atol=0.1,
        rtol_pixels=0.1,
        atol_pixels=0.4,
    )


@pytest.mark.parametrize("mapper", _MAPPERS)
def test_intensity_registration_mask(mapper):
    if mapper in ("mapperCrossCorrelation_Numpy", "mapperOptimization_Kornia"):
        pytest.skip("mask not supported")

    transfo_type = "translation"

    image = data_for_registration.generate_image()
    image_stack, _, _ = data_for_registration.generate_image_stack(
        image, transfo_type, nimages=2
    )

    select_identical = numpy.zeros(image_stack[0].shape)
    idx_identical = (slice(100, None), slice(None))
    select_identical[idx_identical] = 1
    select_not_identical = 1 - select_identical

    image_stack[1][idx_identical] = image_stack[0][idx_identical]

    image_stacks = data_for_registration.generate_image_stacks(image_stack, nstacks=1)

    mapper_identical = _MAPPERS[mapper](
        transfo_type=transfo_type, mask=select_identical
    )
    mapper_not_identical = _MAPPERS[mapper](
        transfo_type=transfo_type, mask=select_not_identical
    )

    with InputStacksNumpy(image_stacks) as stacks:
        transformations_identical = registration.calculate_transformations(
            stacks, mapper_identical
        )
        transformations_not_identical = registration.calculate_transformations(
            stacks, mapper_not_identical
        )

    active_matrix = transformations_identical["stack_0"][1].active_matrix
    expected = numpy.identity(3)
    numpy.testing.assert_allclose(active_matrix, expected)

    active_matrix = transformations_not_identical["stack_0"][1].active_matrix
    expected = numpy.identity(3)
    expected[:2, 2] = [3, 2]
    numpy.testing.assert_allclose(active_matrix, expected, rtol=0.1)
