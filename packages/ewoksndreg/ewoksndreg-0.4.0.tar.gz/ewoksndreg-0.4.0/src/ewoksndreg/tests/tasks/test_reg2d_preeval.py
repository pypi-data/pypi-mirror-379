from ewoksorange.tests.utils import execute_task

from orangecontrib.ewoksndreg.reg2d_preeval import OWReg2DPreEvaluation

from ...io import data_for_registration
from ...io import output_stack


def test_reg2d_preeval_task(tmp_path):
    _test_reg2d_preeval(tmp_path, OWReg2DPreEvaluation.ewokstaskclass)


def test_reg2d_preeval_widget(tmp_path):
    _test_reg2d_preeval(tmp_path, OWReg2DPreEvaluation)


def _test_reg2d_preeval(tmp_path, task_cls):
    file_path = str(tmp_path / "data.h5")
    data_path = "/entry/process/results/parameters"
    output_root_uri = f"silx://{file_path}::{data_path}"
    image = data_for_registration.generate_image()
    image_stack, _, _ = data_for_registration.generate_image_stack(image, "rigid")
    image_stacks = data_for_registration.generate_image_stacks(
        image_stack, noise="uniform"
    )

    with output_stack.output_context(output_root_uri) as stacks:
        for name, image_stacks in image_stacks.items():
            stacks.add_points(name, image_stacks)
        urls = stacks.data_for_input()

    result = execute_task(task_cls, inputs={"image_stacks": urls})
    assert result == {
        "reference_stack": "stack_0",
        "image_stacks": urls,
        "ranked_stack_names": ["stack_0", "stack_1", "stack_2"],
        "output_configuration": {"reference_stack": None},
    }
