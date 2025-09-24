from typing import Tuple

import numpy

from ...registry import Registered
from ..detection.base import Features

__all__ = ["FeatureMatching"]


class FeatureMatching(Registered, register=False):
    def match(
        self,
        from_features: Features,
        to_features: Features,
        from_image: numpy.ndarray,
        to_image: numpy.ndarray,
    ) -> Tuple[Features, Features]:
        raise NotImplementedError
