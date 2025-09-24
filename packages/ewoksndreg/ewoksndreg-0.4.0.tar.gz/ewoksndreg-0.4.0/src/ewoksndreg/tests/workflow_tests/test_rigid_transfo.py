try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

import pytest
from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks

try:
    from ...dependencies.sitk import sitk
except ImportError:
    sitk = None

from ..assert_transformations import assert_allclose_transformations_dicts


@pytest.mark.skipif(sitk is None, reason="requires SimpleITK")
def test_rigid_transfo_without_qt():
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "rigid_transfo.ows"
    assert_workflow_without_qt(filename)


@pytest.mark.skipif(sitk is None, reason="requires SimpleITK")
def test_rigid_transfo_with_qt(ewoks_orange_canvas):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "rigid_transfo.ows"
    assert_workflow_with_qt(ewoks_orange_canvas, filename)


def assert_workflow_without_qt(filename):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph, inputs=[], outputs=[{"all": True}], merge_outputs=False
    )
    id_to_label = {
        node_id: attrs["label"] for node_id, attrs in graph.graph.nodes.items()
    }
    outputs = {id_to_label[k]: v for k, v in outputs.items()}
    _assert_outputs(outputs)


def assert_workflow_with_qt(ewoks_orange_canvas, filename):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=[])
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    _assert_outputs(outputs)


def _assert_outputs(outputs):
    all_expected_transformations = outputs["2D Example Stacks"]["transformations"]
    all_actual_transformations = outputs["2D Intensity-Based Registration"][
        "transformations"
    ]
    assert_allclose_transformations_dicts(
        all_actual_transformations,
        all_expected_transformations,
        rtol=0.01,
        atol=0,
        rtol_pixels=0.0,
        atol_pixels=0.1,
    )
