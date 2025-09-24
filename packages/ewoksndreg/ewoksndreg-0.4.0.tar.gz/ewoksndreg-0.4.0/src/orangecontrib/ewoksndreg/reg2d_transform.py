import json

from AnyQt import QtWidgets
from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.colors import Colormap
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.tasks.reg2d_transform import Reg2DTransform

from .stacks import stacks_context

__all__ = ["OWReg2DTransform"]


class OWReg2DTransform(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Reg2DTransform
):
    name = "2D Transformation"
    description = "Apply image transformations to a stack of stacks"
    icon = "icons/transformation.png"

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self):
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        values = self.get_default_input_values(
            include_missing=True, defaults={"interpolation_order": 1}
        )

        options = {
            "image_stacks": {
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "output_root_uri": {"value_for_type": ""},
            "interpolation_order": {"value_for_type": 0},
            "crop": {"value_for_type": False},
        }

        for name, kw in options.items():
            if name not in options:
                continue
            self._default_inputs_form.addParameter(
                name,
                value=values[name],
                value_change_callback=self._default_inputs_changed,
                **kw,
            )

    def _default_inputs_changed(self):
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        self._update_input_data()

    def handleNewSignals(self) -> None:
        self._update_input_data()
        super().handleNewSignals()

    def task_output_changed(self):
        self._update_output_data()

    def _init_main_area(self):
        super()._init_main_area()
        layout = self._get_main_layout()

        self._tabs = QtWidgets.QTabWidget(parent=self.mainArea)
        layout.addWidget(self._tabs)

        w = QtWidgets.QWidget(parent=self.mainArea)
        layout = QtWidgets.QVBoxLayout()
        w.setLayout(layout)
        self._oplot = Plot2D(parent=w)
        self._oplot.setDefaultColormap(Colormap("viridis"))
        self._ostack_selector = HorizontalStackSelector(parent=w)
        self.current_in_stack = 0
        self._oimage_slider = HorizontalSliderWithBrowser(parent=w)
        self.current_in_image = 0
        layout.addWidget(self._oplot)
        layout.addWidget(self._ostack_selector)
        layout.addWidget(self._oimage_slider)
        self._tabs.addTab(w, "Aligned")

        w = QtWidgets.QWidget(parent=self.mainArea)
        layout = QtWidgets.QVBoxLayout()
        w.setLayout(layout)
        self._iplot = Plot2D(parent=w)
        self._iplot.setDefaultColormap(Colormap("viridis"))
        self._istack_selector = HorizontalStackSelector(parent=w)
        self._iimage_slider = HorizontalSliderWithBrowser(parent=w)
        layout.addWidget(self._iplot)
        layout.addWidget(self._istack_selector)
        layout.addWidget(self._iimage_slider)
        self._tabs.addTab(w, "Original")

        self._istack_selector.selectionChanged.connect(self._select_in_image)
        self._ostack_selector.selectionChanged.connect(self._select_out_image)
        self._iimage_slider.valueChanged[int].connect(self._select_in_image)
        self._oimage_slider.valueChanged[int].connect(self._select_out_image)
        self._update_input_data()

    def _update_input_data(self):
        dynamic = self.get_dynamic_input_names()
        for name in self.get_input_names():
            self._default_inputs_form.set_parameter_enabled(name, name not in dynamic)

        with stacks_context(self, input=True) as stacks:
            if stacks is None:
                return
            self._istack_selector.setStackNames(list(stacks))
            self._iimage_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._select_in_image(None, stacks=stacks)

    def _update_output_data(self):
        with stacks_context(self, input=False) as stacks:
            if stacks is None:
                return
            self._ostack_selector.setStackNames(list(stacks))
            self._oimage_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._select_out_image(None, stacks=stacks)

    def _select_in_image(self, _, stacks=None):
        with stacks_context(self, input=True, stacks=stacks) as stacks:
            if stacks is None:
                return
            current_stack = self._istack_selector.getStackName()
            current_image = self._iimage_slider.value()
            self._iplot.addImage(stacks[current_stack][current_image], legend="image")

    def _select_out_image(self, _, stacks=None):
        with stacks_context(self, input=False, stacks=stacks) as stacks:
            if stacks is None:
                return
            current_stack = self._ostack_selector.getStackName()
            current_image = self._oimage_slider.value()
            self._oplot.addImage(stacks[current_stack][current_image], legend="image")
