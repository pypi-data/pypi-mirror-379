import json

from AnyQt.QtWidgets import QTabWidget
from AnyQt.QtWidgets import QVBoxLayout
from AnyQt.QtWidgets import QWidget
from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.tasks.reg2d_posteval import Reg2DPostEvaluation

from .stacks import stacks_context

__all__ = ["OWReg2DPostEvaluation"]


class OWReg2DPostEvaluation(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Reg2DPostEvaluation
):
    name = "Post-Registration Evaluation"
    description = "Choose the best registration based on the calculated transformations for each stack"
    icon = "icons/reg2d_posteval.png"

    def __init__(self):
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self):
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
            "output_root_uri": {"value_for_type": ""},
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
        self._tabs = QTabWidget(parent=self.mainArea)
        layout.addWidget(self._tabs)

        w = QWidget(parent=self.mainArea)
        layout = QVBoxLayout()
        w.setLayout(layout)
        self.best_plot = Plot2D(parent=w)
        self._best_image_slider = HorizontalSliderWithBrowser(parent=w)
        layout.addWidget(self.best_plot)
        layout.addWidget(self._best_image_slider)
        self._tabs.addTab(w, "Best Stack")

        w = QWidget(parent=self.mainArea)
        layout = QVBoxLayout()
        w.setLayout(layout)
        self.allplot = Plot2D(parent=w)
        self._stack_selector = HorizontalStackSelector(parent=w)

        self._image_slider = HorizontalSliderWithBrowser(parent=w)
        layout.addWidget(self.allplot)
        layout.addWidget(self._stack_selector)
        layout.addWidget(self._image_slider)
        self._tabs.addTab(w, "All Stacks")

        self._stack_selector.selectionChanged.connect(self._select_image)
        self._best_image_slider.valueChanged[int].connect(self._select_image)
        self._image_slider.valueChanged[int].connect(self._select_image)

    def _update_input_data(self) -> None:
        dynamic = self.get_dynamic_input_names()
        for name in self.get_input_names():
            self._default_inputs_form.set_parameter_enabled(name, name not in dynamic)

    def _update_output_data(self) -> None:
        with stacks_context(self) as stacks:
            if stacks is None:
                return
            self._stack_selector.setStackNames(list(stacks))
            self._best_image_slider.setMaximum(max(len(stacks) - 1, 0))
            self._image_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._select_image(None, stacks=stacks)

    def _select_image(self, _, stacks=None) -> None:
        with stacks_context(self, stacks=stacks) as stacks:
            if stacks is None:
                return
            current_stack = self._stack_selector.getStackName()
            current_image = self._image_slider.value()
            self.allplot.addImage(
                stacks[current_stack][current_image],
                legend="image",
                colormap=Colormap(name="viridis"),
            )

            best_stack = self.get_task_input_value("reference_stack", default=None)
            best_stack = self.get_task_output_value(
                "reference_stack", default=best_stack
            )
            if best_stack:
                best_image = self._best_image_slider.value()
                self.best_plot.addImage(
                    stacks[best_stack][best_image],
                    legend="image",
                    colormap=Colormap(name="viridis"),
                )
