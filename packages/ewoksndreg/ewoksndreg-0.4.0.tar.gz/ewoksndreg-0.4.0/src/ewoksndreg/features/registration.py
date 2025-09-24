from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

from ..io.input_stack import InputStacks
from ..math.indices import get_positive_index
from ..transformation.base import Transformation
from .detection.base import FeatureDetector
from .features.base import Features
from .mapping.base import FeatureMapping
from .matching.base import FeatureMatching


def detect_features(
    stacks: InputStacks,
    detector: FeatureDetector,
    include: Optional[Sequence[int]] = None,
) -> Dict[str, List[Features]]:
    if include is None:
        include = list(range(stacks.stack_len))
    features = dict()
    for name, stack in stacks.items():
        features[name] = [detector.find(stack[i]) for i in include]
    return features


def match_features(
    stacks: InputStacks,
    features: Dict[str, List[Features]],
    matcher: FeatureMatching,
    include: Optional[Sequence[int]] = None,
    reference_image: Union[int, float] = 0,
) -> Dict[str, List[Tuple[Optional[Features], Optional[Features]]]]:
    if set(stacks) != set(features):
        raise ValueError(
            f"Stack names {set(stacks)} are not equal to feature names {set(features)}"
        )
    stack_len = stacks.stack_len
    reference_image = get_positive_index(reference_image, stack_len)
    if include is None:
        include = list(range(stack_len))
    matches = dict()
    for name, stack in stacks.items():
        matches_ = list()
        features_ = features[name]
        ref_image = stack[reference_image]
        ref_features = features_[reference_image]
        for i in include:
            new_image = stack[i]
            if i == reference_image:
                from_features = None
                to_features = None
            else:
                from_features, to_features = matcher.match(
                    ref_features, features_[i], ref_image, new_image
                )
            matches_.append((from_features, to_features))
        matches[name] = matches_
    return matches


def transformations_from_features(
    matches: Dict[str, List[Tuple[Optional[Features], Optional[Features]]]],
    mapper: FeatureMapping,
) -> Dict[str, List[Transformation]]:
    transformations = dict()
    for name, matches_ in matches.items():
        transformations_ = list()
        for ref_features, new_features in matches_:
            if ref_features and new_features:
                transformations_.append(mapper.calculate(new_features, ref_features))
            else:
                transformations_.append(mapper.identity())
        transformations[name] = transformations_
    return transformations


def calculate_transformations(
    stacks: InputStacks,
    detector: FeatureDetector,
    matcher: FeatureMatching,
    mapper: FeatureMapping,
    include: Optional[Sequence[int]] = None,
    reference_image: int = 0,
) -> Dict[str, List[Transformation]]:
    features = detect_features(stacks, detector, include=include)
    matches = match_features(
        stacks, features, matcher, include=include, reference_image=reference_image
    )
    return transformations_from_features(matches, mapper)
