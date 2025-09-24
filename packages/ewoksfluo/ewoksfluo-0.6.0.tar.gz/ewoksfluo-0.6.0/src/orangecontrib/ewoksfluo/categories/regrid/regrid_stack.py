import json

from ewoksorange.bindings import OWEwoksWidgetOneThread
from ewoksorange.bindings import ow_build_opts
from ewoksorange.gui.parameterform import ParameterForm

from ewoksfluo.gui import serialize
from ewoksfluo.gui.data_viewer import DataViewer
from ewoksfluo.io.hdf5 import split_h5uri
from ewoksfluo.tasks.regrid.regrid_stack import RegridXrfResultsStack

__all__ = ["OWRegridStack"]


class OWRegridStack(
    OWEwoksWidgetOneThread, **ow_build_opts, ewokstaskclass=RegridXrfResultsStack
):
    name = "Regrid Stack"
    description = "Regrid XRF stack results"

    def __init__(self):
        super().__init__()
        self._init_control_area()
        self._init_main_area()

    def _init_control_area(self):
        super()._init_control_area()
        self._default_inputs_form = ParameterForm(parent=self.controlArea)
        defaults = {
            "output_root_uri": "processed_data.h5",
        }
        values = self.get_default_input_values(include_missing=True, defaults=defaults)
        self.update_default_inputs(**values)

        parameters = {
            "bliss_scan_uris": {
                "label": "Scan URI's",
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "xrf_results_uri": {
                "label": "URI to the fit results to regrid",
                "value_for_type": "",
                "select": "h5group",
            },
            "output_root_uri": {
                "label": "Output URI",
                "value_for_type": "",
                "select": "h5group",
            },
            "stack_positioner": {
                "label": "Stack positioner name",
                "value_for_type": "",
            },
            "positioners": {
                "label": "List of scan positioner names",
                "value_for_type": "",
                "serialize": serialize.strings_serializer,
                "deserialize": serialize.strings_deserializer,
            },
            "ignore_positioners": {
                "label": "List of positioner names to ignore",
                "value_for_type": "",
                "serialize": serialize.strings_serializer,
                "deserialize": serialize.strings_deserializer,
            },
            "positioner_uri_template": {
                "label": "Positioners template",
                "value_for_type": "",
            },
            "axes_units": {
                "label": "Axes units",
                "value_for_type": "",
                "serialize": json.dumps,
                "deserialize": json.loads,
            },
            "interpolate": {
                "label": "Interpolation method",
                "value_for_type": ["nearest", "linear", "cubic"],
                "select": "choices",
            },
        }

        for name, kw in parameters.items():
            self._default_inputs_form.addParameter(
                name,
                value=values[name],
                value_change_callback=self._default_inputs_changed,
                **kw,
            )

    def _default_inputs_changed(self):
        self.update_default_inputs(**self._default_inputs_form.get_parameter_values())
        self._update_input_data()
        self._update_output_data()

    def handleNewSignals(self) -> None:
        self._update_input_data()
        super().handleNewSignals()

    def task_output_changed(self):
        self._update_output_data()

    def _init_main_area(self):
        super()._init_main_area()
        layout = self._get_main_layout()

        self._viewer = DataViewer(parent=self.mainArea)
        self._viewer.setVisible(True)
        layout.addWidget(self._viewer)
        layout.setStretchFactor(self._viewer, 1)

        self._update_output_data()

    def _update_input_data(self):
        dynamic = self.get_dynamic_input_names()
        for name in self.get_input_names():
            self._default_inputs_form.set_parameter_enabled(name, name not in dynamic)

    def _update_output_data(self):
        self._refresh_output_file()

    def _refresh_output_file(self):
        uri = self.get_task_output_value("xrf_results_uri")
        if uri:
            self._viewer.updateFile(split_h5uri(uri)[0])
