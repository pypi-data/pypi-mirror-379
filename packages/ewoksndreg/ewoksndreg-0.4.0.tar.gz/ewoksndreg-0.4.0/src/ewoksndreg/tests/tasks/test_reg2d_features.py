from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksndreg.reg2d_features import OWReg2DFeatures

from ...io import data_for_registration
from ...io import output_stack
from ..assert_transformations import assert_allclose_transformations


def test_owreg2d_features_task(tmp_path):
    _test_owreg2d_features(tmp_path, OWReg2DFeatures.ewokstaskclass)


def test_owreg2d_features_widget(tmp_path, qtapp):
    _test_owreg2d_features(tmp_path, OWReg2DFeatures)


def _test_owreg2d_features(tmp_path, task_cls):
    file_path = str(tmp_path / "data.h5")
    data_path = "/entry/process/results/parameters"
    output_root_uri = f"silx://{file_path}::{data_path}"
    image = data_for_registration.generate_image()
    image_stack, active_expected, passive_expected = (
        data_for_registration.generate_image_stack(image, "translation", plot=0)
    )
    image_stacks = data_for_registration.generate_image_stacks(
        image_stack, noise="none", nstacks=1
    )

    with output_stack.output_context(output_root_uri) as stacks:
        for name, image_stacks in image_stacks.items():
            stacks.add_points(name, image_stacks)
        urls = stacks.data_for_input()

    result = execute_task(
        task_cls,
        inputs={
            "image_stacks": urls,
            "transformation_type": "translation",
            "detector": ("Sift", "SciKitImage"),
            "matcher": ("Descriptor", "SciKitImage"),
            "mapper": ("LstSq", "Numpy"),
        },
        timeout=120,
    )

    assert_allclose_transformations(
        result["transformations"],
        active_expected,
        passive_expected,
        rtol=0.01,
        atol=0,
        rtol_pixels=0.0,
        atol_pixels=0.1,
    )
