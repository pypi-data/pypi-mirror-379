import numpy
from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksndreg.example2d_stacks import OWExample2DStacks

from ...io import data_for_registration


def test_example2d_stack_task():
    _test_example2d_stack(OWExample2DStacks.ewokstaskclass)


def test_example2d_stack_widget(qtapp):
    _test_example2d_stack(OWExample2DStacks.ewokstaskclass)


def _test_example2d_stack(task_cls):
    image = data_for_registration.generate_image(name="astronaut")
    image_stack, active, passive = data_for_registration.generate_image_stack(
        image, "translation", plot=0
    )
    image_stacks = data_for_registration.generate_image_stacks(image_stack, nstacks=1)

    result = execute_task(
        task_cls,
        inputs={
            "name": "astronaut",
            "transformation_type": "translation",
            "nstacks": 1,
        },
    )

    assert set(image_stacks) == set(result["image_stacks"])
    for name in image_stacks:
        istack = image_stacks[name]
        ostack = result["image_stacks"][name]
        numpy.testing.assert_allclose(istack, ostack)
        for tr, a, p in zip(result["transformations"][name], active, passive):
            numpy.testing.assert_allclose(tr.active_matrix, a)
            numpy.testing.assert_allclose(tr.passive_matrix, p)
