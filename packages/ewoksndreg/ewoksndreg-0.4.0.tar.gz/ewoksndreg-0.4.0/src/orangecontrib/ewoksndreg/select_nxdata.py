from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm

from ewoksndreg.tasks.select_nxdata import SelectNXdataImageStacks

__all__ = ["OWSelectNXdataImageStacks"]


class OWSelectNXdataImageStacks(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=SelectNXdataImageStacks
):
    name = "NXdata stacks"
    description = "Select NXdata image stacks"
    icon = "icons/load_stacks.svg"

    def __init__(self):
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self):
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        values = self.get_default_input_values(include_missing=True)
        options = {
            "input_root_uri": {"value_for_type": ""},
            "output_root_uri": {"value_for_type": ""},
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

    def _update_input_data(self) -> None:
        pass

    def _update_output_data(self) -> None:
        pass
