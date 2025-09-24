import datetime
from typing import Optional

import numpy

from ..handlers import AbstractOutputHandler
from .abstract import AbstractOutputBuffer


class ExternalOutputBuffer(AbstractOutputBuffer):
    """This is an output buffer of an external output handler."""

    def __init__(
        self,
        output_handler: AbstractOutputHandler,
        diagnostics: bool = False,
        figuresofmerit: bool = False,
    ):
        self._output_handler = output_handler
        super().__init__(
            saveResiduals=diagnostics,
            saveFit=diagnostics,
            saveData=diagnostics,
            diagnostics=diagnostics,
            saveFOM=figuresofmerit,
            nosave=True,
        )

    def _allocateRam(self, label, data=None, **kwargs) -> numpy.ndarray:
        # Fix bug in PyMca: https://github.com/silx-kit/pymca/issues/1123
        ids = set(map(id, self._buffers.values()))
        if id(data) in ids:
            data = data.copy()
        return super()._allocateRam(label, data=data, **kwargs)

    @property
    def xrf_results_uri(self) -> Optional[str]:
        return self._output_handler.xrf_results_uri

    @property
    def already_existed(self) -> bool:
        return self._output_handler.already_existed

    @property
    def output_root_uri(self) -> Optional[str]:
        return self._output_handler.output_root_uri

    def save(self):
        self._create_configuration()
        for group_name in self._results:
            self._create_nxdata_group(group_name)

    def _create_configuration(self):
        configuration = self._info["configuration"]
        data = {
            "@NX_class": "NXnote",
            "type": "text/plain",
            "data": configuration.tostring(),
            "date": datetime.datetime.now().astimezone().isoformat(),
        }
        self._output_handler.create_group("configuration", data=data)

    def _create_nxdata_group(self, group_name: str):
        group_data = self._results[group_name]

        data = {"@NX_class": "NXdata"}

        _, signal_data, _ = group_data["_signals"][0]
        if signal_data["data"].ndim == 3:
            # The shape is (nscandim1, nscandim2, nchannels).
            data["@interpretation"] = "spectrum"

        if group_data["axesused"]:
            last_axis_name = group_data["axesused"][-1]
            for axis_name, axis_data, axis_attrs in group_data["axes"]:
                if axis_name != last_axis_name:
                    continue
                data["@axes"] = [axis_name]
                data[axis_name] = axis_data
                for attr_name, attr_value in axis_attrs.items():
                    data[f"{axis_name}@{attr_name}"] = attr_value
                break

        self._output_handler.create_group(group_name, data=data)

        for signal_name, signal_data, _ in group_data["_signals"]:
            data = signal_data["data"]
            if data.ndim > 1:
                # Flatten the first two scan dimensions in (nscandim1, nscandim2, ...).
                data = data.reshape(data.shape[0] * data.shape[1], *data.shape[2:])

            nxdata_handler = self._output_handler.create_nxdata_handler(
                group_name, signal_name, len(data)
            )
            nxdata_handler.add_points(data)
