from typing import Dict
from typing import Sequence
from typing import Union

import numpy

from ..io import input_stack
from ..io import output_stack


def test_stack_io_numpy():
    image = numpy.zeros((2, 3))

    data = dict()
    with output_stack.OutputStacksNumpy(data) as stacko:
        stacko.add_point("stack1", image)
        stacko.add_points("stack1", [image + 1, image + 2])
        result = stacko.data_for_input()
    assert data is not result
    expected = {"stack1": [image, image + 1, image + 2]}
    _assert_stacks_equal(expected, data)
    _assert_stacks_equal(expected, result)

    with output_stack.OutputStacksNumpy(data) as stacko:
        stacko.add_point("stack2", image)
        stacko.add_points("stack2", [image + 1, image + 2])
        result = stacko.data_for_input()
    assert data is not result
    expected = {
        "stack1": [image, image + 1, image + 2],
        "stack2": [image, image + 1, image + 2],
    }
    _assert_stacks_equal(expected, data)
    _assert_stacks_equal(expected, result)

    with output_stack.output_context() as stacko:
        assert isinstance(stacko, output_stack.OutputStacksNumpy)
        stacko.add_point("stack", image)
        stacko.add_points("stack", [image + 1, image + 2])
        result = stacko.data_for_input()
    expected = {"stack": [image, image + 1, image + 2]}
    _assert_stacks_equal(expected, result)

    with input_stack.input_context(result) as stacki:
        assert isinstance(stacki, input_stack.InputStacksNumpy)


def test_stack_io_hdf5(tmp_path):
    image = numpy.zeros((2, 3))

    file_path = str(tmp_path / "data1.h5")
    data_path = "/entry/process/results/parameters"
    uri = f"silx://{file_path}::{data_path}"

    with output_stack.OutputStacksHdf5(uri) as stacko:
        stacko.add_point("stack1", image)
        stacko.add_points("stack1", [image + 1, image + 2])
        uris = stacko.data_for_input()
    expected = {"stack1": [image, image + 1, image + 2]}
    _assert_stacks_equal(expected, uris)

    with output_stack.output_context(uri) as stacko:
        assert isinstance(stacko, output_stack.OutputStacksHdf5)
        stacko.add_point("stack2", image)
        stacko.add_points("stack2", [image + 1, image + 2])
        uris.update(stacko.data_for_input())
    expected = {
        "stack1": [image, image + 1, image + 2],
        "stack2": [image, image + 1, image + 2],
    }
    _assert_stacks_equal(expected, uris)

    with input_stack.input_context(uris) as stacki:
        assert isinstance(stacki, input_stack.InputStacksHdf5)

    with input_stack.input_context(list(uris.values())) as stacki:
        assert isinstance(stacki, input_stack.InputStacksHdf5)


def _assert_stacks_equal(
    expected: Dict[str, Sequence[numpy.ndarray]],
    result: Union[Dict[str, Sequence[numpy.ndarray]], Dict[str, str]],
):
    with input_stack.input_context(result) as data:
        assert set(data) == set(expected)
        for name in data:
            numpy.testing.assert_array_equal(data[name], expected[name])
