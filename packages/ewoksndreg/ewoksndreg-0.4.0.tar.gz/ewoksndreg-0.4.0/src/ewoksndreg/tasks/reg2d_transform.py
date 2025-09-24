import datetime
import json
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple

from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from ewokscore.variable import Variable
from pydantic import Field
from pydantic import field_validator
from silx.io import h5py_utils
from silx.io.url import DataUrl

from ..io.input_stack import InputDataType
from ..io.input_stack import input_context
from ..io.nexus import nx_annotate
from ..io.output_stack import output_context
from ..transformation import Transformation
from ..transformation import apply_transformations


class Inputs(BaseInputModel):
    image_stacks: InputDataType = Field(
        ...,
        description="Image stacks as a dictionary of numpy arrays or list of HDF5 dataset URI's.",
        examples=[
            {
                "stack1": "/path/to/file.h5::/entry/process1/results/parameters/Ca-K",
                "stack2": "/path/to/file.h5::/entry/process1/results/parameters/Fe-K",
            },
            {"stack1": [[0, 0, 0], [1, 1, 1], [2, 2, 2]]},
        ],
    )
    transformations: Dict[str, List[Transformation]] = Field(
        ..., description="Transformations for each image in each stack."
    )
    output_root_uri: Optional[DataUrl] = Field(
        None,
        description="URL to save all transformed stacks.",
        examples=["/path/to/file.h5::/entry/process2/results/parameters/"],
    )
    image_stacks_nxmetadata: Optional[dict] = Field(
        None,
        description="HDF5/NeXus metadata relative to the file root following the Silx dictdump schema.",
        examples=[{"@NX_class": "NXroot", "entry": {"@NX_class": "NXentry"}}],
    )
    output_configuration: Optional[dict] = Field(
        None,
        description="Registration configuration parameters to be saved.",
        examples=[{"param1": 0, "param2": 1}],
    )
    crop: bool = Field(
        False, description="Crop Nan's at the image edges after alignment."
    )
    interpolation_order: int = Field(
        1, description="Interpolation order when transforming an image."
    )

    @field_validator("output_root_uri", mode="before")
    def coerce_uri(cls, var):
        if isinstance(var, str):
            return DataUrl(var)
        if isinstance(var, Variable) and isinstance(var.value, str):
            var.value = DataUrl(var.value)
        return var


class Reg2DTransform(
    Task, input_model=Inputs, output_names=["image_stacks", "output_configuration"]
):
    """Apply transformations calculated from image registration to the images of one or more stacks."""

    def run(self):
        image_stacks = self.inputs.image_stacks
        output_root_uri = self.get_input_value("output_root_uri", None)
        image_stacks_nxmetadata = self.get_input_value("image_stacks_nxmetadata", None)
        if output_root_uri:
            output_filenames = [output_root_uri.file_path()]
        else:
            output_filenames = None
            image_stacks_nxmetadata = None

        with output_context(output_root_uri) as ostacks:
            with input_context(
                image_stacks, output_filenames=output_filenames
            ) as istacks:
                image_crop_idx = apply_transformations(
                    istacks,
                    ostacks,
                    self.inputs.transformations,
                    crop=self.inputs.crop,
                    interpolation_order=self.inputs.interpolation_order,
                )
            aligned_stacks = ostacks.data_for_input()

        if image_stacks_nxmetadata:
            if image_crop_idx is not None:
                _crop_nxdata_axes(
                    output_root_uri,
                    list(aligned_stacks),
                    image_stacks_nxmetadata,
                    image_crop_idx,
                )
            nx_annotate(image_stacks_nxmetadata, output_root_uri.file_path())

        output_configuration = self.get_input_value("output_configuration") or dict()
        output_configuration["crop"] = self.inputs.crop
        output_configuration["interpolation_order"] = self.inputs.interpolation_order
        self.outputs.output_configuration = output_configuration
        if output_root_uri:
            _save_output_configuration(
                output_root_uri, list(aligned_stacks), output_configuration
            )

        self.outputs.image_stacks = aligned_stacks


def _crop_nxdata_axes(
    output_root_uri: DataUrl,
    stack_names: List[str],
    image_stacks_nxmetadata: dict,
    image_crop_idx: Tuple[slice, ...],
):
    root_parts = output_root_uri.data_path().split("/")
    modified = set()
    expected_stack_ndim = len(image_crop_idx) + 1
    for stack_name in stack_names:
        nxdata_parts = root_parts + stack_name.split("/")[:-1]
        nxdata_id = tuple(nxdata_parts)
        if nxdata_id in modified:
            continue
        modified.add(nxdata_id)
        nxdata = image_stacks_nxmetadata
        for name in nxdata_parts:
            if name:
                nxdata = nxdata.get(name, dict())
        axes = nxdata.get("@axes")
        if axes is None:
            continue
        if len(axes) != expected_stack_ndim:
            raise ValueError(
                f"NXdata axes attribute must contain {expected_stack_ndim} names."
            )
        for axis, axis_idx in zip(axes[1:], image_crop_idx):
            nxdata[axis] = nxdata[axis][axis_idx]


def _save_output_configuration(
    output_root_uri: DataUrl, stack_names: List[str], output_configuration: dict
) -> None:
    root_parts = output_root_uri.data_path().split("/")
    nxdata_parts = root_parts + stack_names[0].split("/")[:-1]

    with h5py_utils.File(output_root_uri.file_path(), mode="a") as fh:
        nxprocess = fh
        for name in nxdata_parts:
            if name:
                nxprocess = nxprocess[name]
            if nxprocess.attrs.get("NX_class") == "NXprocess":
                break
        else:
            return

        nxnote = nxprocess.require_group("configuration")
        nxnote.attrs["NX_class"] = "NXnote"
        nxnote["type"] = "application/json"
        nxnote["data"] = json.dumps(output_configuration, indent=2)
        nxnote["date"] = datetime.datetime.now().astimezone().isoformat()
