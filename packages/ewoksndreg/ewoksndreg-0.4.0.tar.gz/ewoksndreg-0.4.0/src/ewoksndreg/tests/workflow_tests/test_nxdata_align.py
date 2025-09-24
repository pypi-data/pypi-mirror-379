try:
    from importlib.resources import files as resource_files
except ImportError:
    from importlib_resources import files as resource_files

from typing import List
from typing import Tuple

import h5py
from ewokscore import execute_graph
from ewoksorange.bindings import ows_to_ewoks
from silx.io.url import DataUrl


def test_nxdata_align_without_qt(multi_nxdata_search_url):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "nxdata_align.ows"
    _assert_nxdata_align_without_qt(filename, multi_nxdata_search_url)


def test_nxdata_align_with_qt(ewoks_orange_canvas, multi_nxdata_search_url):
    from ewoksndreg.tests.workflow_tests import workflows

    filename = resource_files(workflows) / "nxdata_align.ows"
    _assert_nxdata_align_with_qt(ewoks_orange_canvas, filename, multi_nxdata_search_url)


def _assert_nxdata_align_without_qt(filename: str, multi_nxdata_search_url: DataUrl):
    """Execute workflow after converting it to an ewoks workflow"""
    graph = ows_to_ewoks(filename)
    outputs = execute_graph(
        graph,
        inputs=get_inputs(multi_nxdata_search_url),
        outputs=[{"all": True}],
        merge_outputs=False,
    )
    id_to_label = {
        node_id: attrs["label"] for node_id, attrs in graph.graph.nodes.items()
    }
    outputs = {id_to_label[k]: v for k, v in outputs.items()}
    _assert_outputs(outputs, multi_nxdata_search_url)


def _assert_nxdata_align_with_qt(
    ewoks_orange_canvas, filename: str, multi_nxdata_search_url: DataUrl
):
    """Execute workflow using the Qt widgets and signals"""
    ewoks_orange_canvas.load_graph(
        str(filename), inputs=get_inputs(multi_nxdata_search_url)
    )
    ewoks_orange_canvas.start_workflow()
    ewoks_orange_canvas.wait_widgets(timeout=60)
    outputs = dict(ewoks_orange_canvas.iter_output_values())
    _assert_outputs(outputs, multi_nxdata_search_url)


def get_inputs(multi_nxdata_search_url: DataUrl) -> List[dict]:
    return [
        {
            "label": "NXdata stacks",
            "name": "input_root_uri",
            "value": multi_nxdata_search_url.path(),
        }
    ]


def _assert_outputs(outputs, multi_nxdata_search_url: DataUrl):
    output_configuration = outputs["2D Transformation"]["output_configuration"]
    expected = {
        "mapper": "CrossCorrelation-Numpy",
        "mapper_options": {},
        "transformation_type": "translation",
        "reference_image": 0,
        "reference_stack": "parameters1/stack_0",
        "preprocessing_options": None,
        "block_size": 1,
        "crop": True,
        "interpolation_order": 1,
    }
    assert output_configuration == expected

    filename = multi_nxdata_search_url.file_path()
    with h5py.File(filename, "r") as fh:
        for nxdata_name in ["parameters1", "parameters2", "parameters3"]:
            nxdata = fh[f"/entry/process/results/{nxdata_name}"]
            original_shape = (4, 200, 220)
            _assert_nxdata_shapes(nxdata, original_shape)

            nxdata = fh[f"/entry/align/results/{nxdata_name}"]
            cropped_shape = (4, 191, 214)
            _assert_nxdata_shapes(nxdata, cropped_shape)


def _assert_nxdata_shapes(nxdata: h5py.Group, shape: Tuple[int, int, int]):
    axes = nxdata.attrs["axes"]
    axes_shape = tuple(nxdata[name].size for name in axes)
    assert axes_shape == shape

    signals = [nxdata.attrs["signal"]] + nxdata.attrs["auxiliary_signals"].tolist()
    for name in signals:
        assert nxdata[name].shape == shape
