from typing import Optional
from typing import Union

from ewokscore.model import BaseInputModel
from ewokscore.task import Task
from ewokscore.variable import Variable
from pydantic import Field
from pydantic import field_validator
from silx.io.url import DataUrl

from ..io import nexus


class Inputs(BaseInputModel):
    input_root_uri: Union[str, DataUrl] = Field(
        ...,
        description="Root HDF5 URL in which to search for NXdata groups.",
        examples=["/path/to/file.h5::/entry/process/"],
    )
    output_root_uri: Optional[DataUrl] = Field(
        None,
        description="Root HDF5 URL under which to save the aligned results.",
        examples=["/path/to/file.h5::/entry"],
    )

    @field_validator("input_root_uri", "output_root_uri", mode="before")
    def coerce_uri(cls, var):
        if isinstance(var, str):
            return DataUrl(var)
        if isinstance(var, Variable) and isinstance(var.value, str):
            var.value = DataUrl(var.value)
        return var


class SelectNXdataImageStacks(
    Task,
    input_model=Inputs,
    output_names=["image_stacks", "output_root_uri", "image_stacks_nxmetadata"],
):
    """Find image stacks by searching recursively for 3D NXdata signals under a root HDF5 URL."""

    def run(self):
        common_parent_url, image_stacks = nexus.find_nxdata_image_stacks(
            self.inputs.input_root_uri
        )
        output_root_url, metadata = nexus.nxdata_image_stacks_metadata(
            common_parent_url, image_stacks, output_root_url=self.inputs.output_root_uri
        )
        self.outputs.image_stacks = {
            name: url.path() for name, url in image_stacks.items()
        }
        self.outputs.output_root_uri = output_root_url.path()
        self.outputs.image_stacks_nxmetadata = metadata
