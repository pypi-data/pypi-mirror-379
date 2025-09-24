from abc import abstractmethod
from contextlib import contextmanager
from typing import Any
from typing import Dict
from typing import Generator
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

import h5py
import numpy
from ewoksdata.data.hdf5.dataset_writer import DatasetWriter
from numpy.typing import ArrayLike
from silx.io import h5py_utils
from silx.io.url import DataUrl


class OutputStacks:
    def __enter__(self) -> "OutputStacks":
        return self

    def __exit__(self, *args) -> None:
        pass

    @abstractmethod
    def add_point(self, name: str, data: ArrayLike) -> None:
        pass

    @abstractmethod
    def add_points(self, name: str, data: ArrayLike) -> None:
        pass

    @abstractmethod
    def data_for_input(self) -> Any:
        """Argument to be provided to `InputStacks`"""
        pass


class OutputStacksNumpy(OutputStacks):
    def __init__(self, data: Optional[Dict[str, List[numpy.ndarray]]] = None) -> None:
        if data is None:
            data = dict()
        self._data: Dict[str, List[numpy.ndarray]] = data
        super().__init__()

    @property
    def data(self) -> Dict[str, List[numpy.ndarray]]:
        return self._data

    def _parent(self, name: str) -> List[numpy.ndarray]:
        parent = self._data.get(name)
        if parent is None:
            parent = self._data[name] = list()
        return parent

    def add_point(self, name: str, data: ArrayLike) -> None:
        self._parent(name).append(numpy.asarray(data))

    def add_points(self, name: str, data: ArrayLike) -> None:
        self._parent(name).extend(numpy.asarray(data))

    def data_for_input(self) -> Dict[str, List[numpy.ndarray]]:
        return dict(self._data)


class OutputStacksHdf5(OutputStacks):
    def __init__(self, base_uri: Union[str, DataUrl]) -> None:
        self._file_obj: Optional[h5py.File] = None
        if not isinstance(base_uri, DataUrl):
            base_uri = DataUrl(base_uri)
        self._base_uri = base_uri
        self._base_group: Optional[h5py.Group] = None
        self._writers: Dict[str, DatasetWriter] = dict()
        self._uris: List[str] = list()
        self._keys: List[str] = list()
        super().__init__()

    def __enter__(self) -> "OutputStacksHdf5":
        ctx = h5py_utils.File(self._base_uri.file_path(), mode="a")
        self._file_obj = ctx.__enter__()
        self._base_group = self._file_obj.require_group(self._base_uri.data_path())
        return super().__enter__()

    def __exit__(self, *args) -> None:
        try:
            for writer in self._writers.values():
                writer.__exit__(*args)
            self._file_obj.__exit__(*args)
            return super().__exit__(*args)
        finally:
            self._base_group = None
            self._writers.clear()
            self._uris.clear()
            self._file_obj = None

    def _parent(self, name: str) -> DatasetWriter:
        if self._base_group is None:
            raise RuntimeError("enter the context first")
        writer = self._writers.get(name)
        if writer is None:
            uri, writer = self._create_writer(name)
            self._writers[name] = writer
            self._uris.append(uri)
            self._keys.append(name)
        return writer

    def _create_writer(self, name: str) -> Tuple[str, DatasetWriter]:
        parts = [s for s in name.split("/") if s]
        if not parts:
            raise ValueError(f"'{name}' is not a valid HDF5 dataset name")
        dset_name = parts[-1]
        if len(parts) > 1:
            rel_parent_name = "/".join(parts[:-1])
            parent = self._base_group.require_group(rel_parent_name)
        else:
            parent = self._base_group
        ctx = DatasetWriter(parent, dset_name)
        if parent.name == "/":
            uri = f"{parent.file.filename}::{dset_name}"
        else:
            uri = f"{parent.file.filename}::{parent.name}/{dset_name}"
        return uri, ctx.__enter__()

    def add_point(self, name: str, data: ArrayLike) -> None:
        self._parent(name).add_point(data)

    def add_points(self, name: str, data: ArrayLike) -> None:
        self._parent(name).add_points(data)

    def data_for_input(self) -> Dict[str, str]:
        return dict(zip(self._keys, self._uris))


OutputDataType = Union[Dict[str, List[numpy.ndarray]], str, DataUrl, None]


@contextmanager
def output_context(data: OutputDataType = None) -> Generator[OutputStacks, None, None]:
    """Data stacks as a dictionary of numpy arrays or list of HDF5 dataset URI's under one base URI."""
    if isinstance(data, (str, DataUrl)):
        with OutputStacksHdf5(data) as stack:
            yield stack
    else:
        with OutputStacksNumpy(data) as stack:
            yield stack
