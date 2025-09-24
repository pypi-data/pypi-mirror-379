import numpy
from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksndreg.reg2d_transform import OWReg2DTransform

from ...io import data_for_registration
from ...transformation.numpy_backend import NumpyHomography


def test_owreg2d_transform_task():
    _test_owreg2d_transform(OWReg2DTransform.ewokstaskclass)


def test_owreg2d_transform_widget(qtapp):
    _test_owreg2d_transform(OWReg2DTransform)


def _test_owreg2d_transform(task_cls):
    image = data_for_registration.generate_image()
    image_stacks, active, passive = data_for_registration.generate_image_stack(
        image, "translation", plot=0
    )
    image_stacks = data_for_registration.generate_image_stacks(
        image_stacks, noise="none"
    )

    forward = [NumpyHomography(M) for M in passive]
    backward = [NumpyHomography(M) for M in active]
    forward = {name: forward for name in image_stacks}
    backward = {name: backward for name in image_stacks}

    result = execute_task(
        task_cls,
        inputs={"image_stacks": image_stacks, "transformations": forward},
    )
    result = execute_task(
        task_cls,
        inputs={"image_stacks": result["image_stacks"], "transformations": backward},
    )

    for name, istack in image_stacks.items():
        istack = numpy.asarray(istack)
        ostack = numpy.asarray(result["image_stacks"][name])
        idx = numpy.isnan(ostack)
        ostack[idx] = istack[idx]
        numpy.testing.assert_allclose(istack, ostack)
