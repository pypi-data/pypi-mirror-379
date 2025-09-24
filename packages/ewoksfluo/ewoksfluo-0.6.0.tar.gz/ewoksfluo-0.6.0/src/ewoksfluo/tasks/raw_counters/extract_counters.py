from typing import Optional

from ewokscore import Task

from ...io import hdf5
from .. import hdf5_utils
from .. import nexus_utils


class ExtractRawCounters(
    Task,
    input_names=["bliss_scan_uri", "output_root_uri"],
    optional_input_names=["xrf_results_uri"],
    output_names=["xrf_results_uri", "bliss_scan_uri", "output_root_uri"],
):
    """Extract raw single-scan counters and save them like XRF results."""

    def run(self):
        start_time = nexus_utils.now()
        bliss_scan_uri: str = self.inputs.bliss_scan_uri
        output_root_uri: str = self.inputs.output_root_uri
        previous_xrf_results_uri: Optional[str] = self.get_input_value(
            "xrf_results_uri", None
        )

        input_file, scan_h5path = hdf5.split_h5uri(self.inputs.bliss_scan_uri)
        if previous_xrf_results_uri:
            default_nprocess_name = "merge"
        else:
            default_nprocess_name = "raw"

        with nexus_utils.save_in_ewoks_process(
            output_root_uri,
            start_time,
            process_config=dict(),
            default_levels=(scan_h5path, default_nprocess_name),
        ) as (process_group, already_existed):
            if already_existed:
                merged_xrf_results = process_group["results"]
            else:
                merged_xrf_results = process_group.create_group("results")
                merged_xrf_results.attrs["NX_class"] = "NXcollection"

                with hdf5.FileReadAccess(input_file) as h5file:
                    _link_raw_counters(
                        h5file[scan_h5path], merged_xrf_results, "rawcounters"
                    )

                    if previous_xrf_results_uri:
                        input_file, parent_path = hdf5.split_h5uri(
                            previous_xrf_results_uri
                        )
                        with hdf5.FileReadAccess(input_file) as h5file:
                            _link_xrf_results(h5file[parent_path], merged_xrf_results)

            self.outputs.xrf_results_uri = (
                f"{merged_xrf_results.file.filename}::{merged_xrf_results.name}"
            )

        self.outputs.bliss_scan_uri = bliss_scan_uri
        self.outputs.output_root_uri = output_root_uri


def _link_raw_counters(
    raw_scan: hdf5.GroupType, process_group: hdf5.GroupType, name: str
) -> None:
    destination = nexus_utils.create_nxdata(process_group, name)
    measurement = raw_scan["measurement"]
    signals = list()
    for name, dset in measurement.items():
        if dset.ndim == 1:
            hdf5_utils.create_hdf5_link(destination, name, dset)
            signals.append(name)
    nexus_utils.set_nxdata_signals(destination, signals=signals)


def _link_xrf_results(
    xrf_results: hdf5.GroupType, process_group: hdf5.GroupType
) -> None:
    for name, group in xrf_results.items():
        hdf5_utils.create_hdf5_link(process_group, name, group)
