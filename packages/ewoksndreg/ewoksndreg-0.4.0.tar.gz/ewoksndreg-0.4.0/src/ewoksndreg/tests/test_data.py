import numpy
import pytest

from ..io import data_for_registration
from ..transformation.scikitimage_backend import SciKitImageHomography


@pytest.mark.parametrize(
    "transfo_type", ["translation", "rigid", "similarity", "affine"]
)
def test_images(transfo_type):
    image = data_for_registration.generate_image()
    images, active, passive = data_for_registration.generate_image_stack(
        image, transfo_type, nimages=5, plot=0
    )
    assert len(images) == 5
    assert len(active) == 5
    assert len(passive) == 5


@pytest.mark.parametrize("transfo_type", ["rigid", "similarity", "affine"])
def test_transformations(transfo_type):
    image = data_for_registration.generate_image(name="gravel")
    images, _, passive = data_for_registration.generate_image_stack(
        image, transfo_type, nimages=5, plot=0
    )
    back = [
        SciKitImageHomography(passive_matrix=mat, warp_options={"order": 3})
        for mat in passive
    ]
    results = [hom.apply_data(images[i]) for i, hom in enumerate(back)]

    diffs = [(images[0] - res) for res in results]

    numpy.testing.assert_allclose(numpy.nanmax(diffs, axis=(1, 2)), 0, atol=0.2)
