from typing import MutableMapping
from typing import Optional
from typing import Tuple

from silx.opencl import sift
from silx.opencl.common import ocl
from silx.opencl.sift.match import match_py

from ..features import Features
from ..features import SilxDescriptorFeatures
from .base import FeatureMatching

__all__ = ["SilxDescriptorFeatureMatching"]


class SilxDescriptorFeatureMatching(
    FeatureMatching, registry_id=FeatureMatching.RegistryId("Descriptor", "Silx")
):
    def __init__(self, match_options: Optional[MutableMapping] = None, **kw) -> None:
        if match_options is None:
            match_options = dict()
        self._match_options = match_options
        if ocl is None:
            assert not self._match_options, "No options without opencl"
        self._feature_matcher: Optional[sift.MatchPlan] = None
        super().__init__(**kw)

    def match(
        self, from_features: Features, to_features: Features, *_
    ) -> Tuple[Features, Features]:
        silx_from_features = from_features.as_type(SilxDescriptorFeatures).silx_features
        silx_to_features = to_features.as_type(SilxDescriptorFeatures).silx_features

        nfeatures = max(len(silx_from_features), len(silx_to_features))

        if ocl is None:
            func = match_py
        else:
            if (
                self._feature_matcher is None
                or self._feature_matcher.kpsize < nfeatures
            ):
                self._match_options["size"] = nfeatures
                self._feature_matcher = sift.MatchPlan(**self._match_options)
            func = self._feature_matcher.match
        idx_from, idx_to = func(
            silx_from_features, silx_to_features, raw_results=True
        ).T
        return (from_features[idx_from], to_features[idx_to])
