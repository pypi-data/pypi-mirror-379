from pathlib import Path
from typing import List

import h5py
import numpy
import pytest
from ewoksorange.canvas.handler import OrangeCanvasHandler
from ewoksorange.tests.conftest import qtapp  # noqa F401
from silx.io.url import DataUrl

from ..io import data_for_registration
from ..io import output_stack


@pytest.fixture(scope="session")
def ewoks_orange_canvas(qtapp):  # noqa F811
    with OrangeCanvasHandler() as handler:
        yield handler


@pytest.fixture
def single_nxdata_search_url(tmp_path: Path):
    parameter_groups = ["parameters1"]
    return _create_nxdata_groups(tmp_path, parameter_groups)


@pytest.fixture
def multi_nxdata_search_url(tmp_path: Path):
    parameter_groups = ["parameters1", "parameters2", "parameters3"]
    return _create_nxdata_groups(tmp_path, parameter_groups)


def _create_nxdata_groups(tmp_path: Path, parameter_groups: List[str]) -> DataUrl:
    file_path = str(tmp_path / "data.h5")

    for name in parameter_groups:
        data_path = f"/entry/process/results/{name}"
        output_root_uri = f"silx://{file_path}::{data_path}"
        image = data_for_registration.generate_image()
        image_stack, _, _ = data_for_registration.generate_image_stack(
            image, "translation", plot=0
        )
        image_stacks = data_for_registration.generate_image_stacks(
            image_stack, nstacks=3
        )

        with output_stack.output_context(output_root_uri) as stacks:
            for name, image_stacks in image_stacks.items():
                stacks.add_points(name, image_stacks)

    with h5py.File(file_path, "a") as fh:
        fh.attrs["NX_class"] = "NXroot"
        fh["/entry"].attrs["NX_class"] = "NXentry"
        fh["/entry/process"].attrs["NX_class"] = "NXprocess"
        fh["/entry/process/results"].attrs["NX_class"] = "NXcollection"

        fh["/"].attrs["default"] = "entry"
        fh["/entry"].attrs["default"] = "process"
        fh["/entry/process"].attrs["default"] = "results"
        fh["/entry/process/results"].attrs["default"] = parameter_groups[0]

        for nxdata_name in parameter_groups:
            nxdata = fh[f"/entry/process/results/{nxdata_name}"]
            nxdata.attrs["NX_class"] = "NXdata"
            nxdata.attrs["signal"] = "stack_0"
            nxdata.attrs["auxiliary_signals"] = ["stack_1", "stack_2"]
            nxdata.attrs["axes"] = ["z", "y", "x"]
            shape = nxdata["stack_0"].shape
            for name, length in zip(["z", "y", "x"], shape):
                nxdata[name] = numpy.arange(length)

    return DataUrl(f"{file_path}::/entry")
