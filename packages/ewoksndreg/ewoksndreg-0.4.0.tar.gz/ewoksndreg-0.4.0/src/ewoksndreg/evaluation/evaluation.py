from typing import Dict
from typing import List

from ..io.input_stack import InputStacks
from ..transformation.homography import Homography
from .eval_metrics import mse_eval
from .eval_metrics import peak_eval
from .eval_metrics import smoothness_eval


def pre_evaluation(stacks: InputStacks) -> List[str]:
    """
    Evaluates what the most successful stacks for registration might be based
    on how distinct the phase cross correlation peak is.
    """
    evals = dict()
    for name, stack in stacks.items():
        evals[name] = peak_eval(stack, 0)
    return sorted(evals, key=evals.get)


def post_evaluation(
    aligned_stacks: InputStacks,
    transformations: Dict[str, List[Homography]],
) -> List[str]:
    """
    Evaluation of the stack after alignment based on the mse error and the
    smoothness of the transformations.
    """
    errors = dict()
    for name, aligned_stack in aligned_stacks.items():
        transformation = transformations[name]
        err1 = mse_eval(aligned_stack, 0)
        err2 = smoothness_eval(transformation, aligned_stack[0].shape)
        errors[name] = err1 + err2
    return sorted(errors, key=errors.get)
