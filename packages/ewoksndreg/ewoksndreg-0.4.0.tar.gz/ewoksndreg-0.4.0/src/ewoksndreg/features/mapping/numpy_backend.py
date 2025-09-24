import numpy

from ...transformation import TransformationType
from ...transformation.numpy_backend import NumpyHomography
from ..detection.base import Features
from .base import FeatureMapping
from .lstsq import get_lstsq_solver

__all__ = ["NumpyLstSqFeatureMapping"]


class NumpyLstSqFeatureMapping(
    FeatureMapping, registry_id=FeatureMapping.RegistryId("LstSq", "Numpy")
):
    def __init__(self, transfo_type: TransformationType) -> None:
        super().__init__(transfo_type)
        self._solver = get_lstsq_solver(self._transfo_type)

    def calculate(
        self, from_features: Features, to_features: Features
    ) -> NumpyHomography:
        passive_matrix = self._solver(
            to_features.coordinates, from_features.coordinates
        )
        return NumpyHomography(passive_matrix, self._transfo_type)

    def identity(self) -> NumpyHomography:
        return NumpyHomography(numpy.identity(3), TransformationType.identity)
