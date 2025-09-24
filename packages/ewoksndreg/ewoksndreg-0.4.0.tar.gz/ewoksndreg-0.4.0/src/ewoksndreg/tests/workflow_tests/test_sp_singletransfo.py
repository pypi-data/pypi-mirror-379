try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

import numpy
from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks


def test_sp_single_without_qt():
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "sp_singletransfo.ows"
    assert_single_without_qt(filename)


def test_sp_single_with_qt(ewoks_orange_canvas):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "sp_singletransfo.ows"
    assert_single_with_qt(ewoks_orange_canvas, filename)


def assert_single_without_qt(filename):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph, inputs=[], outputs=[{"all": True}], merge_outputs=False
    )
    id_to_label = {
        node_id: attrs["label"] for node_id, attrs in graph.graph.nodes.items()
    }
    outputs = {id_to_label[k]: v for k, v in outputs.items()}
    _assert_single(outputs)


def assert_single_with_qt(ewoks_orange_canvas, filename):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=[])
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    _assert_single(outputs)


def _assert_single(outputs: dict):
    best_stack = outputs["Post-Registration Evaluation"]["reference_stack"]
    best_transformations = outputs["Post-Registration Evaluation"]["transformations"]
    expected_transformations = outputs["2D Example Stacks"]["transformations"]
    for best, expected in zip(
        best_transformations[best_stack], expected_transformations[best_stack]
    ):
        numpy.testing.assert_allclose(
            best.passive_matrix, expected.passive_matrix, rtol=0.1, atol=0.05
        )
        numpy.testing.assert_allclose(
            best.active_matrix, expected.active_matrix, rtol=0.1, atol=0.05
        )

    output_configuration = outputs["Align"]["output_configuration"]
    expected = {
        "mapper": "CrossCorrelation-Numpy",
        "mapper_options": {},
        "transformation_type": "translation",
        "reference_image": 0,
        "reference_stack": "stack_0",
        "preprocessing_options": None,
        "block_size": 1000,
        "crop": False,
        "interpolation_order": 0,
    }
    assert output_configuration == expected
