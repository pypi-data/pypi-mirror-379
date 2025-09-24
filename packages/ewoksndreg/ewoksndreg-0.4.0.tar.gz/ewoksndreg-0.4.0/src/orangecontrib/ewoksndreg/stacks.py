from contextlib import contextmanager
from typing import Generator
from typing import Optional

from ewoksndreg.io.input_stack import InputStacks
from ewoksndreg.io.input_stack import input_context


@contextmanager
def stacks_context(
    owwidget, input: bool = False, stacks: Optional[InputStacks] = None
) -> Generator[Optional[InputStacks], None, None]:
    if stacks is None:
        if input:
            image_stacks = owwidget.get_task_input_value("image_stacks", default=None)
        else:
            image_stacks = owwidget.get_task_output_value("image_stacks", default=None)
    else:
        image_stacks = stacks
    if image_stacks is None:
        yield
    else:
        with input_context(image_stacks) as stacks:
            yield stacks
