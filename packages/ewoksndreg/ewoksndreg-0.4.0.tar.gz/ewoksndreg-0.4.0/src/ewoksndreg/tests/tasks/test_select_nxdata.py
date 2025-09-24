import numpy
from ewoksorange.tests.utils import execute_task
from silx.io.url import DataUrl

from orangecontrib.ewoksndreg.select_nxdata import OWSelectNXdataImageStacks


def test_select_nxdata_task_multiple(multi_nxdata_search_url: DataUrl):
    _test_select_multiple_nxdatas(
        multi_nxdata_search_url, OWSelectNXdataImageStacks.ewokstaskclass
    )


def test_select_nxdata_widget_multiple(multi_nxdata_search_url: DataUrl, qtapp):
    _test_select_multiple_nxdatas(multi_nxdata_search_url, OWSelectNXdataImageStacks)


def test_select_nxdata_task_single(single_nxdata_search_url: DataUrl):
    _test_single_nxdata(
        single_nxdata_search_url, OWSelectNXdataImageStacks.ewokstaskclass
    )


def test_select_nxdata_widget_single(single_nxdata_search_url: DataUrl, qtapp):
    _test_single_nxdata(single_nxdata_search_url, OWSelectNXdataImageStacks)


def _test_select_multiple_nxdatas(multi_nxdata_search_url: DataUrl, task_cls):
    result = execute_task(
        task_cls,
        inputs={
            "input_root_uri": multi_nxdata_search_url,
            "output_root_uri": "test.h5::/2.1",
        },
    )

    expected = {
        "image_stacks": {},
        "image_stacks_nxmetadata": {
            "2.1": {
                "@NX_class": "NXentry",
                "@default": "align",
                "align": {
                    "@NX_class": "NXprocess",
                    "@default": "results",
                    "results": {
                        "@NX_class": "NXcollection",
                        "@default": "parameters1",
                        "parameters1": {
                            "@NX_class": "NXdata",
                            "@signal": "stack_0",
                            "@auxiliary_signals": ["stack_1", "stack_2"],
                            "@axes": ["z", "y", "x"],
                            "z": list(range(4)),
                            "y": list(range(200)),
                            "x": list(range(220)),
                        },
                        "parameters2": {
                            "@NX_class": "NXdata",
                            "@signal": "stack_0",
                            "@auxiliary_signals": ["stack_1", "stack_2"],
                            "@axes": ["z", "y", "x"],
                            "z": list(range(4)),
                            "y": list(range(200)),
                            "x": list(range(220)),
                        },
                        "parameters3": {
                            "@NX_class": "NXdata",
                            "@signal": "stack_0",
                            "@auxiliary_signals": ["stack_1", "stack_2"],
                            "@axes": ["z", "y", "x"],
                            "z": list(range(4)),
                            "y": list(range(200)),
                            "x": list(range(220)),
                        },
                    },
                },
            },
            "@NX_class": "NXroot",
            "@default": "entry",
        },
        "output_root_uri": "test.h5::/2.1/align/results",
    }

    for nxdata_name in ["parameters1", "parameters2", "parameters3"]:
        for stack_name in ["stack_0", "stack_1", "stack_2"]:
            uri = f"{multi_nxdata_search_url.file_path()}::/entry/process/results/{nxdata_name}/{stack_name}"
            expected["image_stacks"][f"{nxdata_name}/{stack_name}"] = uri

    _numpy_array_to_list(result)
    assert result == expected


def _test_single_nxdata(single_nxdata_search_url, task_cls):
    result = execute_task(
        task_cls,
        inputs={
            "input_root_uri": single_nxdata_search_url,
            "output_root_uri": "test.h5::/2.1",
        },
    )

    expected = {
        "image_stacks": {},
        "image_stacks_nxmetadata": {
            "2.1": {
                "@NX_class": "NXentry",
                "@default": "align",
                "align": {
                    "@NX_class": "NXprocess",
                    "@default": "results",
                    "results": {
                        "@NX_class": "NXcollection",
                        "@default": "parameters1",
                        "parameters1": {
                            "@NX_class": "NXdata",
                            "@signal": "stack_0",
                            "@auxiliary_signals": ["stack_1", "stack_2"],
                            "@axes": ["z", "y", "x"],
                            "z": list(range(4)),
                            "y": list(range(200)),
                            "x": list(range(220)),
                        },
                    },
                },
            },
            "@NX_class": "NXroot",
            "@default": "entry",
        },
        "output_root_uri": "test.h5::/2.1/align/results/parameters1",
    }

    for nxdata_name in ["parameters1"]:
        for stack_name in ["stack_0", "stack_1", "stack_2"]:
            uri = f"{single_nxdata_search_url.file_path()}::/entry/process/results/{nxdata_name}/{stack_name}"
            expected["image_stacks"][stack_name] = uri

    _numpy_array_to_list(result)
    assert result == expected


def _numpy_array_to_list(adict: dict):
    for key in adict:
        value = adict[key]
        if isinstance(value, dict):
            _numpy_array_to_list(value)
        elif isinstance(value, numpy.ndarray):
            adict[key] = value.tolist()
