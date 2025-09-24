import json
from typing import Optional

from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.io.input_stack import InputStacks
from ewoksndreg.tasks.example2d_stacks import Example2DStacks
from ewoksndreg.transformation.types import TransformationType

from .stacks import stacks_context

__all__ = ["OWExample2DStacks"]


class OWExample2DStacks(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Example2DStacks
):
    name = "2D Example Stacks"
    description = "Generate a stack of 2D example stacks"
    icon = "icons/load_stacks.svg"

    def __init__(self) -> None:
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self) -> None:
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        values = self.get_default_input_values(include_missing=True)

        options = {
            "name": {
                "value_for_type": [
                    "astronaut",
                    "camera",
                    "brick",
                    "grass",
                    "gravel",
                    "cell",
                ]
            },
            "transformation_type": {
                "value_for_type": list(TransformationType.__members__),
                "serialize": str,
            },
            "nimages": {"value_for_type": 0, "label": "# images per stack"},
            "shape": {
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "nstacks": {"value_for_type": 0, "label": "# stacks"},
            "noise": {"value_for_type": ["none", "s&p", "uniform"]},
        }

        for name, kw in options.items():
            self._default_inputs_form.addParameter(
                name,
                value=values[name],
                value_change_callback=self._default_inputs_changed,
                **kw,
            )

    def _default_inputs_changed(self) -> None:
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        self._update_input_data()

    def handleNewSignals(self) -> None:
        self._update_input_data()
        super().handleNewSignals()

    def task_output_changed(self) -> None:
        self._update_output_data()

    def _init_main_area(self) -> None:
        super()._init_main_area()
        layout = self._get_main_layout()
        self._plot = Plot2D(parent=self.mainArea)
        layout.addWidget(self._plot)

        self._stack_selector = HorizontalStackSelector(parent=self.mainArea)
        layout.addWidget(self._stack_selector)
        self._stack_selector.selectionChanged.connect(self._select_output_image)

        self._image_slider = HorizontalSliderWithBrowser(parent=self.mainArea)
        layout.addWidget(self._image_slider)
        self._image_slider.valueChanged[int].connect(self._select_output_image)

        self._update_output_data()

    def _update_input_data(self) -> None:
        dynamic = self.get_dynamic_input_names()
        for name in self.get_input_names():
            self._default_inputs_form.set_parameter_enabled(name, name not in dynamic)

    def _update_output_data(self) -> None:
        with stacks_context(self) as stacks:
            if stacks is None:
                return
            self._image_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._stack_selector.setStackNames(list(stacks))
            self._select_output_image(None, stacks=stacks)

    def _select_output_image(self, _, stacks: Optional[InputStacks] = None) -> None:
        with stacks_context(self, stacks=stacks) as stacks:
            if stacks is None:
                return
            stack_name = self._stack_selector.getStackName()
            image_index = self._image_slider.value()
            self._plot.addImage(stacks[stack_name][image_index], legend="image")
