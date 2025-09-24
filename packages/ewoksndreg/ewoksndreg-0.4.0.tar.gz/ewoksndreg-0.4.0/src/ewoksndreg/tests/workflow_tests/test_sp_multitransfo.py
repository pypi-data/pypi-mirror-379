try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks

from ..assert_transformations import assert_allclose_transformations_dicts


def test_sp_multi_without_qt():
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "sp_multitransfo.ows"
    assert_multi_without_qt(filename)


def test_sp_multi_with_qt(ewoks_orange_canvas):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "sp_multitransfo.ows"
    assert_multi_with_qt(ewoks_orange_canvas, filename)


def assert_multi_without_qt(filename):
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


def assert_multi_with_qt(ewoks_orange_canvas, filename):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=[])
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    _assert_outputs(outputs)


def _assert_outputs(outputs):
    expected_transformations = outputs["2D Example Stacks"]["transformations"]
    actual_transformations = outputs["2D Intensity-Based Registration"][
        "transformations"
    ]
    assert_allclose_transformations_dicts(
        actual_transformations,
        expected_transformations,
        rtol=0.1,
        atol=0.05,
        rtol_pixels=0.1,
        atol_pixels=0.4,
    )

    output_configuration = outputs["Align"]["output_configuration"]
    expected = {
        "mapper": "CrossCorrelation-Numpy",
        "mapper_options": {},
        "transformation_type": "translation",
        "reference_image": 0,
        "reference_stack": None,
        "preprocessing_options": {
            "apply_filter": "median",
            "apply_low_pass": 0.0,
            "apply_high_pass": 0.0,
        },
        "block_size": 1000,
        "crop": False,
        "interpolation_order": 0,
    }
    assert output_configuration == expected
