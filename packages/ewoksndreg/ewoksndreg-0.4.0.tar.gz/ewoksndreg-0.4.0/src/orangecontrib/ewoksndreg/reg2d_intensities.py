import json
from typing import Dict

import numpy
from AnyQt import QtWidgets
from ewokscore import missing_data
from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm
from silx.gui.colors import Colormap
from silx.gui.plot import ComplexImageView
from silx.gui.plot import Plot2D
from silx.gui.widgets.FrameBrowser import HorizontalSliderWithBrowser

from ewoksndreg.gui.stack_selector import HorizontalStackSelector
from ewoksndreg.intensities import registration
from ewoksndreg.intensities.types import KorniaMetricType
from ewoksndreg.intensities.types import KorniaOptimizerType
from ewoksndreg.intensities.types import SitkMetricType
from ewoksndreg.intensities.types import SitkOptimizerType
from ewoksndreg.math.fft import fft2
from ewoksndreg.math.fft import fftshift
from ewoksndreg.math.fft import ifft2
from ewoksndreg.math.filter import FilterType
from ewoksndreg.math.filter import WindowType
from ewoksndreg.math.filter import preprocess
from ewoksndreg.registry import RegistryId
from ewoksndreg.tasks.reg2d_intensities import Reg2DIntensities
from ewoksndreg.transformation.types import TransformationType

from .stacks import stacks_context

__all__ = ["OWReg2DIntensities"]


class OWReg2DIntensities(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=Reg2DIntensities
):
    name = "2D Intensity-Based Registration"
    description = "Calculate transformations of a stack of stacks based on intensities"
    icon = "icons/registration.png"

    _MAPPER_OPTIONS = {
        "Numpy": {},
        "SimpleITK": {
            "metric": {
                "value_for_type": list(SitkMetricType.__members__),
                "serialize": str,
            },
            "optimizer": {
                "value_for_type": list(SitkOptimizerType.__members__),
                "serialize": str,
            },
            "pyramid_levels": {"value_for_type": 0},
            "order": {"value_for_type": 0},
            "sampling": {
                "value_for_type": ["none", "random", "regular"],
                "serialize": str,
            },
            "sampling%": {
                "value_for_type": 0.5,
                "serialize": str,
            },
        },
        "Kornia": {
            "metric": {
                "value_for_type": list(KorniaMetricType.__members__),
                "serialize": str,
            },
            "optimizer": {
                "value_for_type": list(KorniaOptimizerType.__members__),
                "serialize": str,
            },
            "pyramid_levels": {"value_for_type": 0},
        },
        "SciKitImage": {
            "normalized": {"value_for_type": False},
            "upsample_factor": {"value_for_type": 0},
            "sim_normalized": {"value_for_type": False},
            "sim_upsample_factor": {"value_for_type": 0},
        },
    }

    _PREPROC_OPTIONS = {
        "apply_filter": {
            "value_for_type": list(FilterType.__members__),
            "serialize": str,
        },
        "filter_parameter": {"value_for_type": 0.1},
        "apply_low_pass": {"value_for_type": 0.1},
        "apply_high_pass": {"value_for_type": 0.1},
        "pin_range": {"value_for_type": False},
        "apply_window": {
            "value_for_type": list(WindowType.__members__),
            "serialize": str,
        },
    }

    def __init__(self):
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self):
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        values = self.get_default_input_values(include_missing=True)
        proper_transformations = list(TransformationType.__members__)
        try:
            proper_transformations.remove("composite")
            proper_transformations.remove("identity")
        except ValueError:
            pass
        options = {
            "image_stacks": {
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "transformation_type": {
                "value_for_type": proper_transformations,
                "serialize": str,
            },
            "reference_image": {"value_for_type": 0},
            "reference_stack": {"value_for_type": ""},
            "block_size": {"value_for_type": 1},
        }

        for name, kw in options.items():
            self._default_inputs_form.addParameter(
                name,
                value=values[name],
                value_change_callback=self._default_inputs_changed,
                **kw,
            )
        self._default_inputs_form.addParameter(
            "mapper",
            value=values["mapper"],
            value_for_type=registration.IntensityMapping.get_subclass_ids(),
            serialize=str,
            value_change_callback=self._mapper_changed,
        )

        layout = self._get_control_layout()
        self._tabs = QtWidgets.QTabWidget(parent=self.controlArea)
        layout.addWidget(self._tabs)

        # preprocessing tab
        self._prep_widget = QtWidgets.QWidget(parent=self.controlArea)
        layout = QtWidgets.QVBoxLayout()
        self._prep_widget.setLayout(layout)
        self._prepform = ParameterForm(parent=self.controlArea)
        for name, kw in self._PREPROC_OPTIONS.items():
            self._prepform.addParameter(
                name,
                value_change_callback=self._preproc_inputs_changed,
                **kw,
            )
        if values["preprocessing_options"]:
            self._prepform.set_parameter_values(values["preprocessing_options"])
        layout.addWidget(self._prepform)
        self._tabs.addTab(self._prep_widget, "Preprocessing")

        # tabs for each of the backends
        self._pforms: Dict[str, ParameterForm] = {}
        self._tab_widgets: Dict[str, QtWidgets.QWidget] = {}
        for mapper in registration.IntensityMapping.get_subclass_ids():
            mapper_options = [
                self._MAPPER_OPTIONS[key]
                for key in self._MAPPER_OPTIONS.keys()
                if key in str(mapper)
            ][0]

            w = QtWidgets.QWidget(parent=self.controlArea)
            layout = QtWidgets.QVBoxLayout()
            w.setLayout(layout)
            self._pforms[str(mapper)] = ParameterForm(parent=w)
            for name, options in mapper_options.items():
                self._pforms[str(mapper)].addParameter(
                    name,
                    value_change_callback=self._other_inputs_changed,
                    **options,
                )
            layout.addWidget(self._pforms[str(mapper)])
            self._tabs.addTab(w, mapper.backend)
            self._tab_widgets[str(mapper)] = w
        if values["mapper"] and values["mapper_options"]:
            self._pforms[values["mapper"]].set_parameter_values(
                values["mapper_options"]
            )

    def _default_inputs_changed(self):
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        self._update_data()

    def _preproc_inputs_changed(self):
        kw = {
            key: item
            for key, item in self._prepform.get_parameter_values().items()
            if not missing_data.is_missing_data(item)
        }
        self.update_default_inputs(preprocessing_options=kw)
        self._select_image(None)

    def _other_inputs_changed(self):
        current_mapper = self._default_inputs_form.get_parameter_value("mapper")
        if current_mapper:
            mapper_options = self._pforms[current_mapper].get_parameter_values()
            kw = {
                key: item
                for key, item in mapper_options.items()
                if not missing_data.is_missing_data(item)
            }
            self.update_default_inputs(mapper_options=kw)
        self._update_data()

    def _mapper_changed(self):
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        mapper = self.get_task_input_value("mapper", None)
        if mapper is None:
            self._tabs.setCurrentWidget(self._prep_widget)
            self._update_data()
            return
        self._update_transfo_types(RegistryId.factory(mapper))
        self._tabs.setCurrentWidget(self._tab_widgets[mapper])
        mapper_options = self._pforms[mapper].get_parameter_values()
        kw = {
            key: item
            for key, item in mapper_options.items()
            if not missing_data.is_missing_data(item)
        }
        self.update_default_inputs(mapper_options=kw)

    def _update_transfo_types(self, mapper: RegistryId):
        cls = registration.IntensityMapping.get_subclass(mapper)
        current_type = str(self.get_task_input_value("transformation_type"))
        allowed_types = cls.SUPPORTED_TRANSFORMATIONS
        transfo_widg = self._default_inputs_form._get_value_widget(
            "transformation_type"
        )
        transfo_widg.clear()
        transfo_widg.addItem("<missing>", missing_data.MISSING_DATA)
        for _type in allowed_types:
            transfo_widg.addItem(str(_type), str(_type))
        if current_type in allowed_types:
            transfo_widg.setCurrentText(current_type)
            self.update_default_inputs(transformation_type=current_type)

    def handleNewSignals(self) -> None:
        self._update_input_data()
        self._update_data()
        super().handleNewSignals()

    def task_output_changed(self):
        self._update_data()

    def _init_main_area(self):
        super()._init_main_area()
        layout = self._get_main_layout()

        self._vtab = QtWidgets.QTabWidget(parent=self.mainArea)

        layout.addWidget(self._vtab)

        self._main_visual = QtWidgets.QWidget(parent=self.mainArea)
        tab_layout = QtWidgets.QVBoxLayout()
        self._main_visual.setLayout(tab_layout)
        self._plot = Plot2D(parent=self._main_visual)
        self._plot.setDefaultColormap(Colormap("viridis"))
        tab_layout.addWidget(self._plot)
        self._vtab.addTab(self._main_visual, "Images")
        self._plot.getMaskToolsDockWidget().sigMaskChanged.connect(self._mask_changed)

        self._fft_visual = QtWidgets.QWidget(parent=self.mainArea)
        tab_layout = QtWidgets.QVBoxLayout()
        self._fft_visual.setLayout(tab_layout)
        self._fftplot = ComplexImageView.ComplexImageView(parent=self._fft_visual)
        self._fftplot.setColormap(Colormap("viridis", normalization=Colormap.LOGARITHM))
        tab_layout.addWidget(self._fftplot)
        self._vtab.addTab(self._fft_visual, "Fourier")

        self._fftprod_visual = QtWidgets.QWidget(parent=self.mainArea)
        tab_layout = QtWidgets.QVBoxLayout()
        self._fftprod_visual.setLayout(tab_layout)
        self._fftprodplot = ComplexImageView.ComplexImageView(
            parent=self._fftprod_visual
        )
        self._fftprodplot.setColormap(Colormap("viridis"))
        tab_layout.addWidget(self._fftprodplot)
        self._vtab.addTab(self._fftprod_visual, "Cross-correlogram")
        self._vtab.currentChanged[int].connect(self._select_image)

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

            tab = self._vtab.currentIndex()
            current_stack = self._stack_selector.getStackName()
            current_image = self._image_slider.value()
            stack = stacks[current_stack]

            preprocessing_options = self.get_task_input_value(
                "preprocessing_options", {}
            )
            image = preprocess(
                stack[current_image],
                **preprocessing_options,
            )
            if tab == 0:
                self._plot.addImage(image, legend="image")
            elif tab == 1:
                self._fftplot.setData(fft2(image, centered=True), False)
            elif tab == 2:
                reference_image = self.get_task_input_value("reference_image", 0)
                if reference_image == -1:
                    reference_image = stacks.stack_len // 2
                ref = preprocess(stack[reference_image], **preprocessing_options)
                prod = fft2(image) * fft2(ref).conj()
                pcc = ifft2(prod / numpy.abs(prod))
                self._fftprodplot.setData(fftshift(pcc), False)

    def _mask_changed(self):
        mask = self._plot.getSelectionMask()
        if mask.ndim == 2:
            if numpy.any(mask):
                self.update_default_inputs(mask=mask)
            else:
                self.update_default_inputs(mask=missing_data.MISSING_DATA)
            self._default_inputs_changed()
