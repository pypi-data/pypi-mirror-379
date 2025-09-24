from ...registry import Registered
from ...transformation import TransformationType
from ...transformation.base import Transformation
from ..detection.base import Features

__all__ = ["FeatureMapping"]


class FeatureMapping(Registered, register=False):
    def __init__(self, transfo_type: TransformationType) -> None:
        self._transfo_type = TransformationType(transfo_type)

    @property
    def transformation_type(self) -> TransformationType:
        return self._transfo_type

    def identity(self) -> Transformation:
        raise NotImplementedError

    def calculate(
        self, from_features: Features, to_features: Features
    ) -> Transformation:
        raise NotImplementedError
