from typing import Dict
from typing import List

try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks


def test_reg2d_features_without_qt():
    from orangecontrib.ewoksndreg import tutorials

    filename = resource_files(tutorials) / "reg2d_features.ows"
    assert_reg2d_features_without_qt(filename)


def test_reg2d_features_with_qt(ewoks_orange_canvas):
    from orangecontrib.ewoksndreg import tutorials

    filename = resource_files(tutorials) / "reg2d_features.ows"
    assert_reg2d_features_with_qt(ewoks_orange_canvas, filename)


def assert_reg2d_features_without_qt(filename):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph, inputs=get_inputs(), outputs=[{"all": True}], merge_outputs=False
    )
    expected = get_expected_outputs()
    label_to_id = {
        attrs["label"]: node_id for node_id, attrs in graph.graph.nodes.items()
    }
    outputs = {k: set(v) for k, v in outputs.items()}
    expected = {label_to_id[k]: v for k, v in expected.items()}
    assert outputs == expected


def assert_reg2d_features_with_qt(ewoks_orange_canvas, filename):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(str(filename), inputs=get_inputs())
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    outputs = {k: set(v) for k, v in outputs.items()}
    assert outputs == get_expected_outputs()


def get_inputs() -> List[dict]:
    return [
        {
            "label": "2D Feature Registration",
            "name": "detector",
            "value": "Sift-SciKitImage",
        }
    ]


def get_expected_outputs() -> Dict[str, dict]:
    return {
        "Align (theory)": {"image_stacks", "output_configuration"},
        "2D Feature Registration": {
            "image_stacks",
            "features",
            "matches",
            "transformations",
            "reference_stack",
            "output_configuration",
        },
        "Align": {"image_stacks", "output_configuration"},
        "2D Example Stacks": {"image_stacks", "transformations"},
    }
