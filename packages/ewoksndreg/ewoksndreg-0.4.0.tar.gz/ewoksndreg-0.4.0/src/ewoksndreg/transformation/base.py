from typing import Any
from typing import Optional
from typing import Sequence
from typing import Type

import numpy

from ..registry import Registered
from .types import TransformationType

__all__ = ["Transformation"]


class Transformation(Registered, register=False):
    def __init__(self, transfo_type: TransformationType) -> None:
        if isinstance(transfo_type, str):
            transfo_type = TransformationType(transfo_type)
        self._transfo_type = transfo_type
        self._active_matrix: Optional[numpy.ndarray] = None

    @property
    def transformation_type(self) -> TransformationType:
        return self._transfo_type

    def as_type(self, cls: Type["Transformation"]) -> "Transformation":
        if isinstance(self, cls):
            return self
        raise TypeError(f"cannot convert '{type(self).__name__}' to '{cls.__name__}'")

    def is_homography(self):
        return self._transfo_type in [
            "identity",
            "translation",
            "rigid",
            "similarity",
            "affine",
            "projective",
        ]

    def apply_coordinates(self, coord: Sequence[numpy.ndarray]) -> numpy.ndarray:
        """
        :param coord: shape `(N, M)`
        :returns: shape `(N, M)`
        """
        raise NotImplementedError

    def apply_data(
        self,
        data: numpy.ndarray,
        offset: Optional[numpy.ndarray] = None,
        shape: Optional[numpy.ndarray] = None,
        cval=numpy.nan,
        interpolation_order: int = 1,
    ) -> numpy.ndarray:
        """
        :param data: shape `(N1, N2, ..., M1, M2, ...)` with `len((N1, N2, ...)) = N`
        :param offset: shape `(N,)`
        :param shape: shape `(N,) = [N1', N2', ...]`
        :param cval: missing value
        :param interpolation_order: order of interpolation: 0 is nearest neighbor, 1 is bilinear,...
        :returns: shape `(N1', N2', ..., M1, M2, ...)`
        """
        raise NotImplementedError

    def __matmul__(self, other: "Transformation") -> "Transformation":
        """When appyling the transformation, `other` comes after `self`"""
        raise NotImplementedError

    @property
    def passive_matrix(self) -> numpy.ndarray:
        raise AttributeError("Transformation does not have a matrix representation")

    @property
    def active_matrix(self) -> numpy.ndarray:
        if self._active_matrix is None:
            self._active_matrix = numpy.linalg.inv(self.passive_matrix)
        return self._active_matrix

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Transformation):
            return False

        try:
            passive_matrix = self.passive_matrix
            other_passive_matrix = other.passive_matrix
        except AttributeError:
            pass
        else:
            if passive_matrix.shape != other_passive_matrix.shape:
                return False
            return numpy.allclose(passive_matrix, other_passive_matrix)

        return id(self) == id(other)
