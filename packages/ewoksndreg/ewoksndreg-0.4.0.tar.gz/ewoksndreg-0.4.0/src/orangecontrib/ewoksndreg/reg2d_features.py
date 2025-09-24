import json

import numpy
from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.features import registration
from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.tasks.reg2d_features import Reg2DFeatures
from ewoksndreg.transformation.types import TransformationType

from .stacks import stacks_context

__all__ = ["OWReg2DFeatures"]


class OWReg2DFeatures(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Reg2DFeatures
):
    name = "2D Feature-Based Registration"
    description = "Calculate transformations of a stack of stacks based on features"
    icon = "icons/2d_features.svg"

    def __init__(self):
        super().__init__()
        self._space = 0.05
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
            "reference_image": {"value_for_type": 0},
            "reference_stack": {"value_for_type": ""},
            "transformation_type": {
                "value_for_type": list(TransformationType.__members__),
                "serialize": str,
            },
            "detector": {
                "value_for_type": registration.FeatureDetector.get_subclass_ids(),
                "serialize": str,
            },
            "matcher": {
                "value_for_type": registration.FeatureMatching.get_subclass_ids(),
                "serialize": str,
            },
            "mapper": {
                "value_for_type": registration.FeatureMapping.get_subclass_ids(),
                "serialize": str,
            },
        }

        for name, kw in options.items():
            self._default_inputs_form.addParameter(
                name,
                value=values[name],
                value_change_callback=self._default_inputs_changed,
                **kw,
            )

    def _default_inputs_changed(self):
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        self._update_data()

    def handleNewSignals(self) -> None:
        self._update_input_data()
        super().handleNewSignals()

    def task_output_changed(self):
        self._update_data()

    def _init_main_area(self):
        super()._init_main_area()
        layout = self._get_main_layout()

        self._plot = Plot2D(parent=self.mainArea)
        layout.addWidget(self._plot)

        self._stack_selector = HorizontalStackSelector(parent=self.mainArea)
        layout.addWidget(self._stack_selector)
        self._stack_selector.selectionChanged.connect(self._select_image)

        self._image_slider = HorizontalSliderWithBrowser(parent=self.mainArea)
        layout.addWidget(self._image_slider)
        self._image_slider.valueChanged[int].connect(self._select_image)

        self._update_data()

    def _update_data(self):
        with stacks_context(self, input=True) as stacks:
            if stacks is None:
                return
            self._stack_selector.setStackNames(list(stacks))
            self._image_slider.setMaximum(max(stacks.stack_len - 1, 0))
            self._select_image(None, stacks=stacks)

    def _update_input_data(self):
        dynamic = self.get_dynamic_input_names()
        for name in self.get_input_names():
            self._default_inputs_form.set_parameter_enabled(name, name not in dynamic)

    def _select_image(self, _, stacks=None):
        with stacks_context(self, input=True, stacks=stacks) as stacks:
            if stacks is None:
                return

            current_stack = self._stack_selector.getStackName()
            current_image = self._image_slider.value()
            stack = stacks[current_stack]
            reference_image = self.get_task_input_value("reference_image", 0)
            refimg = stack[reference_image]
            selimg = stack[current_image]

            space = max(int(refimg.shape[1] * self._space), 1)
            spaceimg = numpy.full((refimg.shape[0], space), numpy.nan)
            off = refimg.shape[1] + space

            self._plot.addImage(
                numpy.hstack([refimg, spaceimg, selimg]), legend="stack"
            )

            transformations = self.get_task_output_value("transformations")
            if not transformations:
                return
            transformations = transformations[current_stack]
            features = self.get_task_output_value("features")[current_stack]
            matches = self.get_task_output_value("matches")[current_stack]

            def legend_generator():
                i = 0
                while True:
                    yield f"c{i}"
                    i += 1

            legend = legend_generator()

            self._plot.remove(kind="curve")

            yref, xref = features[reference_image].coordinates
            ysel, xsel = features[current_image].coordinates
            xsel = xsel + off

            self._plot.addCurve(
                xref,
                yref,
                legend=next(legend),
                symbol="+",
                linestyle=" ",
                color="#00FF00",
            )
            self._plot.addCurve(
                xsel,
                ysel,
                legend=next(legend),
                symbol="+",
                linestyle=" ",
                color="#00FF00",
            )

            reffeatures, selfeatures = matches[current_image]
            if reffeatures is None:
                reffeatures = features[reference_image]
                selfeatures = reffeatures
            yref, xref = reffeatures.coordinates
            ysel, xsel = selfeatures.coordinates
            xsel = xsel + off

            for x0, y0, x1, y1 in zip(xref, yref, xsel, ysel):
                self._plot.addCurve(
                    [x0, x1],
                    [y0, y1],
                    legend=next(legend),
                    color="#FF0000",
                    linestyle="-",
                )
