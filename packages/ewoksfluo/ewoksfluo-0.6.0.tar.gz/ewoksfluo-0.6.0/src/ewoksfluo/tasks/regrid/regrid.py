from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence

from ewokscore import Task

from ...io import hdf5
from ...math.regular_grid import ScatterDataInterpolator
from ...math.rounding import round_to_significant
from .. import nexus_utils
from ..xrf_results import get_xrf_result_groups
from . import positioners_utils


class RegridXrfResults(
    Task,
    input_names=["xrf_results_uri", "bliss_scan_uri", "output_root_uri"],
    optional_input_names=[
        "positioners",
        "positioner_uri_template",
        "ignore_positioners",
        "interpolate",
        "resolution",
        "axes_units",
    ],
    output_names=["xrf_results_uri", "bliss_scan_uri", "output_root_uri"],
):
    """Regrid single-scan XRF results on a regular grid by interpolation."""

    def run(self):
        start_time = nexus_utils.now()
        output_root_uri: str = self.inputs.output_root_uri

        with nexus_utils.save_in_ewoks_subprocess(
            output_root_uri, start_time, {}, default_levels=("results", "regrid")
        ) as (regrid_results, already_existed):
            if not already_existed:
                self._regrid(regrid_results)

            self.outputs.xrf_results_uri = (
                f"{regrid_results.file.filename}::{regrid_results.name}"
            )
        self.outputs.bliss_scan_uri = self.inputs.bliss_scan_uri
        self.outputs.output_root_uri = output_root_uri

    def _regrid(self, regrid_results):
        bliss_scan_uri: str = self.inputs.bliss_scan_uri
        xrf_results_uri: str = self.inputs.xrf_results_uri
        ignore_positioners: Optional[Sequence[str]] = self.get_input_value(
            "ignore_positioners", None
        )
        position_suburis = self._get_position_suburis(
            bliss_scan_uri, ignore_positioners=ignore_positioners
        )
        interpolate: str = self.get_input_value("interpolate", "nearest") or "nearest"
        resolution: Optional[dict] = self.get_input_value("resolution", None)
        axes_units: Optional[Dict[str, str]] = self.get_input_value("axes_units", None)

        coordinates, grid_names, grid_units = positioners_utils.read_position_suburis(
            bliss_scan_uri, position_suburis, axes_units=axes_units
        )
        if resolution:
            resolution = [resolution[name] for name in grid_names]
        else:
            resolution = None
        interpolator = ScatterDataInterpolator(
            coordinates,
            grid_names,
            grid_units,
            method=interpolate,
            resolution=resolution,
        )

        xrf_results_filename, xrf_results_h5path = hdf5.split_h5uri(xrf_results_uri)
        with hdf5.FileReadAccess(xrf_results_filename) as xrf_results_file:
            xrf_results_grp = xrf_results_file[xrf_results_h5path]
            if not hdf5.is_group(xrf_results_grp):
                raise TypeError(f"'{xrf_results_uri}' must be a group")

            nxdata_groups = get_xrf_result_groups(xrf_results_grp)

            title_parts = list()
            for group_name in reversed(list(nxdata_groups)):
                input_grp = xrf_results_grp[group_name]
                input_datasets = {
                    dset_name: dset
                    for dset_name, dset in input_grp.items()
                    if hdf5.is_dataset(dset) and dset_name not in grid_names
                }
                if not input_datasets:
                    # NXdata group which does not plot scan data
                    continue

                # NXdata signals
                output_grp = nexus_utils.create_nxdata(regrid_results, group_name)
                for dset_name, dset in input_datasets.items():
                    output_grp.create_dataset(
                        dset_name, data=interpolator.regrid(dset[()])
                    )

                nexus_utils.set_nxdata_signals(
                    output_grp, signals=tuple(input_datasets.keys())
                )

                # NXdata axes
                axes = list()
                for i, (axisname, arr) in enumerate(
                    zip(grid_names, interpolator.grid_axes)
                ):
                    axes.append(axisname)
                    dset = output_grp.create_dataset(axisname, data=arr)
                    if interpolator.units is not None:
                        dset.attrs["units"] = interpolator.units
                        dset.attrs["long_name"] = f"{axisname} ({interpolator.units})"
                    output_grp.create_dataset(f"{axisname}_indices", data=i)
                    title_parts.append(
                        (
                            axisname,
                            len(arr),
                            round_to_significant(abs(arr[1] - arr[0])),
                            interpolator.units,
                        )
                    )
                output_grp.attrs["axes"] = axes

            interpolator.save_coordinates_as_nxdata(regrid_results)

            if title_parts:
                title = [
                    f"{axisname} ({size} x {resolution} {units})"
                    for axisname, size, resolution, units in title_parts
                ]
                regrid_results["title"] = " x ".join(title)

    def _get_position_suburis(
        self, bliss_scan_uri: str, ignore_positioners: Optional[Sequence[str]] = None
    ) -> List[str]:
        positioners = self.get_input_value("positioners", None)
        if not positioners:
            return positioners_utils.get_scan_position_suburis(
                bliss_scan_uri, ignore_positioners=ignore_positioners
            )
        if isinstance(positioners, str):
            positioners = [positioners]
        template = self.get_input_value("positioner_uri_template", "measurement/{}")
        return [template.format(s) for s in positioners]
