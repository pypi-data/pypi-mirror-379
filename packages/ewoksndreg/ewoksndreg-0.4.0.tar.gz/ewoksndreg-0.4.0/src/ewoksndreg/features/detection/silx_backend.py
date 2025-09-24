from typing import Mapping
from typing import Optional

import numpy
from silx.opencl import sift
from silx.opencl.common import ocl

from ..features import SilxDescriptorFeatures
from .base import FeatureDetector

if ocl is None:
    raise ImportError("pyopencl missing")

__all__ = ["SilxSiftFeatureDetector"]


class SilxSiftFeatureDetector(
    FeatureDetector, registry_id=FeatureDetector.RegistryId("Sift", "Silx")
):
    def __init__(
        self,
        feature_options: Optional[Mapping] = None,
        mask: Optional[numpy.ndarray] = None,
    ) -> None:
        if feature_options is None:
            feature_options = dict()
        self._feature_options = feature_options
        self._feature_detector: Optional[sift.SiftPlan] = None
        super().__init__(mask=mask)

    def find(self, image: numpy.ndarray) -> SilxDescriptorFeatures:
        if (
            self._feature_detector is None
            or self._feature_detector.dtype is not image.dtype
            or self._feature_detector.shape != image.shape
        ):
            self._feature_detector = sift.SiftPlan(
                dtype=image.dtype, shape=image.shape, **self._feature_options
            )
        silx_features = self._feature_detector.keypoints(image)

        if self._mask is not None:
            kp1 = numpy.round(silx_features.x).astype(numpy.int32)
            kp0 = numpy.round(silx_features.y).astype(numpy.int32)
            mask = self._mask[(kp0, kp1)].astype(bool)
            silx_features = silx_features[mask]

        return SilxDescriptorFeatures(silx_features)
