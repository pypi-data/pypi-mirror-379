from typing import Dict
from typing import Optional
from typing import Sequence

import numpy
from scipy.ndimage import affine_transform
from scipy.ndimage import shift

from .base import Transformation
from .homography import Homography
from .numpy_backend import homography_transform_coordinates

__all__ = ["ScipyHomography"]


class ScipyHomography(
    Homography, registry_id=Homography.RegistryId("Homography", "Scipy")
):
    def __init__(self, *args, warp_options: Optional[Dict] = None, **kw) -> None:
        if warp_options is None:
            warp_options = dict()
        self._warp_options = warp_options
        super().__init__(*args, **kw)

    def apply_coordinates(self, coord: Sequence[numpy.ndarray]) -> numpy.ndarray:
        """
        :param coord: shape `(N, M)`
        :returns: shape `(N, M)`
        """
        return homography_transform_coordinates(self.active_matrix, coord)

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
        kw = dict(self._warp_options)
        if shape is not None:
            kw["output_shape"] = shape
        if offset is not None:
            kw["offset"] = offset
        if cval is not None:
            kw["cval"] = cval
        if interpolation_order is not None:
            kw["order"] = interpolation_order
        # TODO: offset, shape
        if self.transformation_type == self.transformation_type.identity:
            return data
        if self.transformation_type == self.transformation_type.translation:
            return shift(data, -self.passive_matrix[:-1, -1], **kw)
        if self.transformation_type in (
            self.transformation_type.rigid,
            self.transformation_type.similarity,
            self.transformation_type.affine,
        ):
            return affine_transform(
                data,
                self.passive_matrix[0:-1, 0:-1],
                offset=self.passive_matrix[:-1, -1],
                **kw,
            )
        raise NotImplementedError

    def __matmul__(self, other: Transformation):
        if isinstance(other, ScipyHomography):
            if self.passive_matrix.shape == other.passive_matrix.shape:
                return ScipyHomography(
                    other.passive_matrix @ self.passive_matrix,
                    warp_options=self._warp_options,
                )
            else:
                raise TypeError("Homographies must have same dimensions")
        else:
            raise ValueError("Only concatenation of same types allowed")
