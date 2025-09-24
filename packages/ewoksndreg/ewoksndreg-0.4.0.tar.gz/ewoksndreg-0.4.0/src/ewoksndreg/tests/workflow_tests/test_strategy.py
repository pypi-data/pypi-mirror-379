from typing import List

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

import numpy
import pytest
from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks

pytestmark = pytest.mark.parametrize(
    "reference_image, block_size",
    [
        (0, 0),
        (29, 1000),
        (59, 5),
        (13, 3),
        pytest.param(0, 1000, marks=pytest.mark.xfail),
    ],
)


def test_strat_workflow_without_qt(reference_image, block_size):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "strategy.ows"
    assert_workflow_without_qt(filename, reference_image, block_size)


def test_strat_workflow_with_qt(ewoks_orange_canvas, reference_image, block_size):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "strategy.ows"
    assert_workflow_with_qt(ewoks_orange_canvas, filename, reference_image, block_size)


def assert_workflow_without_qt(filename, reference_image, block_size):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph,
        inputs=get_inputs(reference_image, block_size),
        outputs=[{"all": True}],
        merge_outputs=False,
    )
    id_to_label = {
        node_id: attrs["label"] for node_id, attrs in graph.graph.nodes.items()
    }
    outputs = {id_to_label[k]: v for k, v in outputs.items()}
    _assert_strategy(outputs, reference_image, block_size)


def assert_workflow_with_qt(ewoks_orange_canvas, filename, reference_image, block_size):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=[])
    ewoks_orange_canvas.set_input_values(get_inputs(reference_image, block_size))
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    _assert_strategy(outputs, reference_image, block_size)


def _assert_strategy(outputs, reference_image, block_size):
    orignal_stacks = outputs["2D Example Stacks"]["image_stacks"]
    aligned_stacks = outputs["Align"]["image_stacks"]
    assert set(orignal_stacks) == set(aligned_stacks)
    for name, orignal_stack in orignal_stacks.items():
        expected = orignal_stack[reference_image]
        for actual in aligned_stacks[name]:
            idx = numpy.isfinite(actual)
            numpy.testing.assert_allclose(
                actual[idx], expected[idx], rtol=0.1, atol=0.05
            )

    output_configuration = outputs["Align"]["output_configuration"]
    expected = {
        "mapper": "CrossCorrelation-SciKitImage",
        "mapper_options": {},
        "transformation_type": "translation",
        "reference_image": reference_image,
        "reference_stack": None,
        "preprocessing_options": {"apply_high_pass": 1.0},
        "block_size": block_size,
        "crop": False,
        "interpolation_order": 1,
    }
    assert output_configuration == expected


def get_inputs(reference_image, block_size) -> List[dict]:
    return [
        {
            "label": "2D Intensity-Based Registration",
            "name": "reference_image",
            "value": reference_image,
        },
        {
            "label": "2D Intensity-Based Registration",
            "name": "block_size",
            "value": block_size,
        },
    ]
