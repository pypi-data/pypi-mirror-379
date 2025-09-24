from itertools import takewhile
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

import h5py
from silx.io import h5py_utils
from silx.io.url import DataUrl


def common_h5_parent(h5names: List[str]) -> Tuple[str, List[str]]:
    """
    :param h5names: Absolute HDF5 dataset or group names.
    :returns: Name of the common parent and the relative names with respect to that parent.
    """
    split_h5names = [h5name.split("/") for h5name in h5names]
    common_parent_groups = list(
        takewhile(lambda parts: all(p == parts[0] for p in parts), zip(*split_h5names))
    )
    ncommon = len(common_parent_groups)
    parent_h5name = "/".join(split_h5names[0][:ncommon])
    rel_h5names = ["/".join(parts[ncommon:]) for parts in split_h5names]
    return parent_h5name, rel_h5names


def find_nxdata_image_stacks(
    root_url: Union[str, DataUrl],
) -> Tuple[DataUrl, Dict[str, DataUrl]]:
    """
    :param h5names: Absolute HDF5 dataset or group names.
    :returns: URL of the common parent and dictionary that maps relative name w.r.t. common parent to URL.
    """
    if not isinstance(root_url, DataUrl):
        root_url = DataUrl(root_url)

    filename = root_url.file_path()
    with h5py_utils.File(filename) as fh:
        name = root_url.data_path() or "/"
        root = fh[name]

        h5names = list()

        def func(_, h5item):
            if isinstance(h5item, h5py.Group):
                nx_class = h5item.attrs.get("NX_class")
                if nx_class == "NXdata":
                    signal = h5item.attrs.get("signal")
                    if signal:
                        if h5item[signal].ndim == 3:
                            for h5child in h5item.values():
                                if h5child.ndim == 3:
                                    h5names.append(h5child.name)

        _ = root.visititems(func)

    if not h5names:
        raise RuntimeError(
            f"No NXdata groups found with 3D signals under {root_url.path()!r}"
        )

    parent_h5name, rel_h5names = common_h5_parent(h5names)
    image_stacks = {
        key: DataUrl(f"{filename}::{name}") for key, name in zip(rel_h5names, h5names)
    }
    common_parent_url = DataUrl(f"{filename}::{parent_h5name}")

    return common_parent_url, image_stacks


def nxdata_image_stacks_metadata(
    common_parent_url: Union[str, DataUrl],
    image_stacks: Dict[str, Union[str, DataUrl]],
    top_nx_class: str = "NXprocess",
    top_name: str = "align",
    output_root_url: Union[str, DataUrl, None] = None,
) -> Tuple[DataUrl, dict]:
    """
    :param common_parent_url: URL to the common parent of all image stack URLs.
    :param image_stacks: URL to image stacks.
    :param top_nx_class: NX_class of the parent group which needs to be renamed to `top_name`.
    :param top_name: New top HDF5 group name.
    :param output_root_url: output root URL.
    :returns: output root URL and HDF5/NeXus metadata relative to the file root following the Silx dictdump schema.
    """
    if not isinstance(common_parent_url, DataUrl):
        common_parent_url = DataUrl(common_parent_url)
    if output_root_url is not None and not isinstance(output_root_url, DataUrl):
        output_root_url = DataUrl(output_root_url)

    # For example:
    #  common_parent_name = "/entry/process/results"
    #  common_parent_groups = ["", "entry", "process", "results"]
    common_parent_name = common_parent_url.data_path()
    common_parent_groups = common_parent_name.split("/")

    filename = common_parent_url.file_path()
    with h5py_utils.File(filename) as fh:
        common_parent = fh[common_parent_name]

        # Classes of the common parent groups
        # For example
        #  nxclasses = ["NXroot", "NXentry", "NXprocess", "NXcollection"]
        parent = common_parent
        common_parent_group_attrs = [dict(parent.attrs)]
        while parent.name != "/":
            parent = parent.parent
            common_parent_group_attrs.append(dict(parent.attrs))
        common_parent_group_attrs = common_parent_group_attrs[::-1]
        nxclasses = [attrs.get("NX_class") for attrs in common_parent_group_attrs]

        # Find the top level to replace it with a new name
        # For example
        #  common_parent_groups = ["", "entry", "align", "results"]
        if top_nx_class in nxclasses:
            top_level = nxclasses.index(top_nx_class)
        else:
            top_level = len(nxclasses) - 1
        original_top_name = common_parent_groups[top_level]
        common_parent_groups[top_level] = top_name
        nxclasses[top_level] = top_nx_class
        common_parent_group_attrs[top_level]["NX_class"] = top_nx_class
        if top_level > 0:
            top_parent_attrs = common_parent_group_attrs[top_level - 1]
            original_top_parent_default = top_parent_attrs.get("default")
            if original_top_name == original_top_parent_default:
                top_parent_attrs["default"] = top_name

        # Replace the common input groups with the requested common groups
        if output_root_url:
            output_root_file_path = output_root_url.file_path()
            if output_root_url.data_path():
                requested_common_parent_groups = output_root_url.data_path().split("/")
            else:
                requested_common_parent_groups = [""]

            nextra = len(requested_common_parent_groups) - len(common_parent_groups)
            if nextra <= 0:
                nrequested = len(requested_common_parent_groups)
                common_parent_groups[:nrequested] = requested_common_parent_groups
            else:
                common_parent_groups = requested_common_parent_groups
                common_parent_group_attrs += [{"NX_class": "NXcollection"}] * nextra
                nxclasses += ["NXcollection"] * nextra
        else:
            output_root_file_path = filename
        output_root_name = "/".join(common_parent_groups)

        # Metadata of the common parent groups
        output_metadata = {}
        common_output_metadata = output_metadata
        for name, attrs in zip(common_parent_groups, common_parent_group_attrs):
            if name:
                common_output_metadata[name] = dict()
                common_output_metadata = common_output_metadata[name]
            for key, value in attrs.items():
                common_output_metadata[f"@{key}"] = value

        # Metadata of the NXdata group(s)
        top_nxdata_is_annotated = False
        for dset_relname, dset_url in image_stacks.items():
            dset_parts = dset_relname.split("/")
            nxdata_is_common_parent = len(dset_parts) == 1

            if nxdata_is_common_parent:
                if top_nxdata_is_annotated:
                    # NXdata metadata is already read in a previous iteration
                    continue

                # Read NXdata metadata
                nxdata_metadata = _get_nxdata_metadata(fh, dset_url)
                common_output_metadata.update(nxdata_metadata)
                top_nxdata_is_annotated = True
            else:
                # Get the metadata of the parents
                parent_metadata = common_output_metadata
                for s in dset_parts[:-2]:
                    if s not in parent_metadata:
                        parent_metadata[s] = {"@NX_class": "NXcollection"}
                    parent_metadata = parent_metadata[s]

                name_in_nxdata = dset_parts[-2]
                nxdata_is_annotated = name_in_nxdata in parent
                if nxdata_is_annotated:
                    # NXdata metadata is already read in a previous iteration
                    continue

                # Read NXdata metadata
                nxdata_metadata = _get_nxdata_metadata(fh, dset_url)
                nxdata_metadata = _get_nxdata_metadata(fh, dset_url)
                parent_metadata[name_in_nxdata] = nxdata_metadata

    output_root_url = DataUrl(f"{output_root_file_path}::{output_root_name}")
    return output_root_url, output_metadata


def _get_nxdata_metadata(fh: h5py.File, dset_url: Union[str, DataUrl]) -> dict:
    """NXdata metadata includes all HDF5 attributes and axes field values."""
    if not isinstance(dset_url, DataUrl):
        dset_url = DataUrl(dset_url)
    nxdata = fh[dset_url.data_path()].parent
    nxdata_metadata = {f"@{k}": v for k, v in nxdata.attrs.items()}
    for name in nxdata.attrs.get("axes", []):
        nxdata_metadata[name] = nxdata[name][()]
    return nxdata_metadata


def nx_annotate(
    treedict: Dict,
    h5item: Union[h5py.Group, h5py.Dataset, str, DataUrl],
    **open_options,
) -> None:
    """Like dicttonx from Silx but recursive addition of groups and datasets
    and modifying of attributes.
    """
    if isinstance(h5item, str):
        h5item = DataUrl(h5item)
    if isinstance(h5item, DataUrl):
        _ = open_options.setdefault("mode", "a")
        with h5py_utils.File(h5item.file_path(), **open_options) as fh:
            h5item = fh[h5item.data_path() or "/"]
            _dicttonx(treedict, h5item)
    else:
        _dicttonx(treedict, h5item)


def _dicttonx(treedict: Dict, h5item: Union[h5py.Group, h5py.Dataset]) -> None:
    child_attrs = dict()
    for key, value in treedict.items():
        if "@" in key:
            child_name, _, attr_name = key.partition("@")
            if child_name:
                child_attrs[(child_name, attr_name)] = value
            else:
                h5item.attrs[attr_name] = value
        elif isinstance(value, dict):
            h5group = h5item.require_group(key)
            _dicttonx(value, h5group)
        else:
            if key not in h5item:
                h5item[key] = value
    for (child_name, attr_name), value in child_attrs.items():
        h5child = h5item[child_name]
        if attr_name not in h5child.attrs:
            h5child.attrs[attr_name] = value
