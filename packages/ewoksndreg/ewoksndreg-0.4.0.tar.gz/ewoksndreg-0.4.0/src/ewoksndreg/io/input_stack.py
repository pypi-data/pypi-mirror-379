import sys
from collections.abc import Mapping as AbcMapping
from contextlib import contextmanager
from typing import Dict
from typing import Generator
from typing import Iterator
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

import numpy
from numpy.typing import ArrayLike
from silx.io import h5py_utils
from silx.io.url import DataUrl

from .nexus import common_h5_parent


class InputStacks(AbcMapping):
    def __init__(
        self, data: Dict[str, Union[Sequence[ArrayLike], numpy.ndarray]]
    ) -> None:
        self._data = data

    def __enter__(self) -> "InputStacks":
        return self

    def __exit__(self, *args) -> None:
        pass

    def __getitem__(self, idx) -> ArrayLike:
        return self._data[idx]

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    @property
    def _first_stack(self) -> Optional[Sequence[ArrayLike]]:
        if self._data:
            return next(iter(self._data.values()))

    @property
    def stack_len(self) -> int:
        if self._data:
            return len(self._first_stack)
        return 0

    @property
    def data_shape(self) -> Tuple[int]:
        if self._data:
            return self._first_stack[0].shape
        return tuple()


class InputStacksNumpy(InputStacks):
    def __init__(
        self, data: Dict[str, Union[Sequence[numpy.ndarray], numpy.ndarray]], **_
    ) -> None:
        super().__init__(data)


class InputStacksHdf5(InputStacks):
    def __init__(
        self,
        data: Union[Sequence[Union[str, DataUrl]], Dict[str, Union[str, DataUrl]]],
        output_filenames: Optional[Sequence[str]] = None,
        **_,
    ) -> None:
        if isinstance(data, AbcMapping):
            self._uris = [
                uri if isinstance(uri, DataUrl) else DataUrl(uri)
                for uri in data.values()
            ]
            self._keys = list(data.keys())
        else:
            self._uris = [
                uri if isinstance(uri, DataUrl) else DataUrl(uri) for uri in data
            ]
            _, self._keys = common_h5_parent([uri.data_path() for uri in self._uris])
        self._file_objs = list()
        if output_filenames:
            output_filenames = set(output_filenames)
            self._modes = [
                "a" if uri.file_path() in output_filenames else "r"
                for uri in self._uris
            ]
        else:
            self._modes = ["r"] * len(self._uris)
        super().__init__(dict())

    def __enter__(self) -> "InputStacksHdf5":
        dset_objs = []
        try:
            for uri, mode in zip(self._uris, self._modes):
                ctx = h5py_utils.File(uri.file_path(), mode=mode)
                file_obj = ctx.__enter__()
                dset_obj = file_obj[uri.data_path()]
                self._shape = (len(self._uris),) + dset_obj.shape
                self._dtype = dset_obj.dtype
                self._file_objs.append(file_obj)
                dset_objs.append(dset_obj)
        except Exception:
            for ctx in self._file_objs:
                ctx.__exit__(*sys.exc_info())
            self._file_objs.clear()
            raise

        if len(dset_objs) == 0:
            pass
        else:
            self._data.update(zip(self._keys, dset_objs))

        return super().__enter__()

    def __exit__(self, *args) -> None:
        try:
            for ctx in self._file_objs:
                ctx.__exit__(*args)
            return super().__exit__(*args)
        finally:
            self._data.clear()
            self._file_objs.clear()


InputDataType = Union[
    InputStacks,
    Dict[str, Sequence[numpy.ndarray]],
    Dict[str, numpy.ndarray],
    Sequence[Union[str, DataUrl]],
    Dict[str, Union[str, DataUrl]],
]


@contextmanager
def input_context(
    data: InputDataType,
    output_filenames: Optional[Sequence[str]] = None,
) -> Generator[InputStacks, None, None]:
    """Data stacks as a dictionary of numpy arrays or list of HDF5 dataset URI's."""
    if isinstance(data, InputStacks):
        yield data
    else:
        if isinstance(data, AbcMapping):
            if data and isinstance(next(iter(data.values())), (str, DataUrl)):
                with InputStacksHdf5(data, output_filenames=output_filenames) as stack:
                    yield stack
            else:
                with InputStacksNumpy(data) as stack:
                    yield stack
        elif isinstance(data, Sequence):
            with InputStacksHdf5(data, output_filenames=output_filenames) as stack:
                yield stack
        else:
            raise TypeError(str(type(data)))
