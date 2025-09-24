import json
from typing import Optional

from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.io.input_stack import InputStacks
from ewoksndreg.tasks.reg2d_preeval import Reg2DPreEvaluation

from .stacks import stacks_context

__all__ = ["OWReg2DPreEvaluation"]


class OWReg2DPreEvaluation(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Reg2DPreEvaluation
):
    name = "Pre-Registration Evaluation"
    description = "Generate ranking of most promising stacks based on noisiness and peak in phase cross correlation"
    icon = "icons/reg2d_preeval.svg"

    def __init__(self) -> None:
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self) -> None:
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        values = self.get_default_input_values(include_missing=True)

        options = {
            "image_stacks": {
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "reference_stack": {"value_for_type": ""},
            "skip": {"value_for_type": False},
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
            self._stack_selector.setStackNames(list(stacks))
            self._image_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._select_output_image(None, stacks=stacks)

    def _select_output_image(self, _, stacks: Optional[InputStacks] = None):
        with stacks_context(self, stacks=stacks) as stacks:
            if stacks is None:
                return
            reference_stack = self._stack_selector.getStackName()
            image_index = self._image_slider.value()
            self._plot.addImage(
                stacks[reference_stack][image_index],
                legend="image",
                colormap=Colormap(name="viridis"),
            )
