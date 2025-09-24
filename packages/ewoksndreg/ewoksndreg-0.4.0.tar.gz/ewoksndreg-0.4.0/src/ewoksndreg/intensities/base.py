from typing import List

import numpy

from ..registry import Registered
from ..transformation.base import Transformation
from ..transformation.types import TransformationType

__all__ = ["IntensityMapping"]


class IntensityMapping(Registered, register=False):
    SUPPORTED_TRANSFORMATIONS: List[str] = []

    def __init__(self, transfo_type: TransformationType, **_) -> None:
        if transfo_type in self.SUPPORTED_TRANSFORMATIONS:
            self._transfo_type = TransformationType(transfo_type)
        else:
            raise ValueError(
                f"{transfo_type} is not supported by {self.__class__.__name__}"
            )
        super().__init__()

    @property
    def transformation_type(self) -> TransformationType:
        return self._transfo_type

    def identity(self, dimension: int = 2) -> Transformation:
        raise NotImplementedError

    def calculate(
        self, from_image: numpy.ndarray, to_image: numpy.ndarray
    ) -> Transformation:
        raise NotImplementedError
