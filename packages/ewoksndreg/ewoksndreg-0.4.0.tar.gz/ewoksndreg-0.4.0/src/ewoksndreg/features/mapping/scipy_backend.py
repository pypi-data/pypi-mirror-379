import numpy

from ...transformation import TransformationType
from ...transformation.scipy_backend import ScipyHomography
from ..detection.base import Features
from .base import FeatureMapping
from .lstsq import get_lstsq_solver

__all__ = ["ScipyLstSqFeatureMapping"]


class ScipyLstSqFeatureMapping(
    FeatureMapping, registry_id=FeatureMapping.RegistryId("LstSq", "Scipy")
):
    def __init__(self, transfo_type: TransformationType) -> None:
        super().__init__(transfo_type)
        self._solver = get_lstsq_solver(self._transfo_type)

    def calculate(
        self, from_features: Features, to_features: Features
    ) -> ScipyHomography:
        passive_matrix = self._solver(
            to_features.coordinates, from_features.coordinates
        )
        return ScipyHomography(passive_matrix, self._transfo_type)

    def identity(self) -> ScipyHomography:
        return ScipyHomography(numpy.identity(3), TransformationType.identity)
