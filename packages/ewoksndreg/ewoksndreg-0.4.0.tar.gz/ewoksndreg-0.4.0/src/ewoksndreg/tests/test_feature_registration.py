import numpy
import pytest

from ..features import registration
from ..io import data_for_registration
from ..io.input_stack import InputStacksNumpy

_DETECTORS = {
    f"detector{'_'.join(k)}": v
    for k, v in registration.FeatureDetector.get_subclass_items()
}
_MATCHERS = {
    f"matcher{'_'.join(k)}": v
    for k, v in registration.FeatureMatching.get_subclass_items()
}
_MAPPERS = {
    f"mapper{'_'.join(k)}": v
    for k, v in registration.FeatureMapping.get_subclass_items()
}


@pytest.mark.parametrize("mapper", _MAPPERS)
@pytest.mark.parametrize("detector", _DETECTORS)
@pytest.mark.parametrize("matcher", _MATCHERS)
@pytest.mark.parametrize("transfo_type", ["translation"])
def test_feature_registration(transfo_type, matcher, detector, mapper):
    image = data_for_registration.generate_image()
    image_stack, active_expected, passive_expected = (
        data_for_registration.generate_image_stack(image, transfo_type, plot=0)
    )
    image_stacks = data_for_registration.generate_image_stacks(image_stack, nstacks=1)

    detector = _DETECTORS[detector]()
    matcher = _MATCHERS[matcher]()
    mapper = _MAPPERS[mapper](transfo_type)

    with InputStacksNumpy(image_stacks) as stacks:
        transformations = registration.calculate_transformations(
            stacks, detector, matcher, mapper
        )

    for transformations in transformations.values():
        active_actual = numpy.stack([tr.active_matrix for tr in transformations])
        passive_actual = numpy.stack([tr.passive_matrix for tr in transformations])

        if "Sift" in detector.get_subclass_id():
            rtol = 0.01
        else:
            rtol = 0.05
        numpy.testing.assert_allclose(active_expected, active_actual, rtol=rtol)
        numpy.testing.assert_allclose(passive_expected, passive_actual, rtol=rtol)


@pytest.mark.parametrize("mapper", _MAPPERS)
@pytest.mark.parametrize("detector", _DETECTORS)
@pytest.mark.parametrize("matcher", _MATCHERS)
def test_feature_registration_mask(matcher, detector, mapper):
    transfo_type = "translation"
    matcher = _MATCHERS[matcher]()
    mapper = _MAPPERS[mapper](transfo_type)

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

    detector_identical = _DETECTORS[detector](mask=select_identical)
    detector_not_identical = _DETECTORS[detector](mask=select_not_identical)

    with InputStacksNumpy(image_stacks) as stacks:
        transformations_identical = registration.calculate_transformations(
            stacks, detector_identical, matcher, mapper
        )
        transformations_not_identical = registration.calculate_transformations(
            stacks, detector_not_identical, matcher, mapper
        )

    active_matrix = transformations_identical["stack_0"][1].active_matrix
    expected = numpy.identity(3)
    if detector in ("detectorSift_Silx", "detectorSift_Silx"):
        atol = 0.3
    else:
        atol = 0
    numpy.testing.assert_allclose(active_matrix, expected, atol=atol)

    active_matrix = transformations_not_identical["stack_0"][1].active_matrix
    expected = numpy.identity(3)
    expected[:2, 2] = [3, 2]
    numpy.testing.assert_allclose(active_matrix, expected, rtol=0.1)
