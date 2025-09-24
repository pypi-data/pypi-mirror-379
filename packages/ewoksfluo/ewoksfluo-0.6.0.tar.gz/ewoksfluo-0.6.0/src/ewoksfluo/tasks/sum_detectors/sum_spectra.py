from typing import Sequence

import numpy
from ewokscore import Task
from ewoksdata.data.hdf5.config import guess_dataset_config

from ...io.hdf5 import split_h5uri
from .. import nexus_utils
from ..hdf5_utils import create_hdf5_link
from ..hdf5_utils import link_bliss_scan
from .sum_utils import sum_spectra_from_hdf5

DEFAULTS = {
    "xrf_spectra_uri_template": "instrument/{}/data",
    "detector_normalization_template": "1./<instrument/{}/live_time>",
    "output_detector_name": "mcasum",
}


class SumXrfSpectra(
    Task,
    input_names=[
        "bliss_scan_uri",
        "detector_names",
        "output_root_uri",
    ],
    optional_input_names=[
        "xrf_spectra_uri_template",
        "detector_normalization_template",
        "output_detector_name",
    ],
    output_names=[
        "bliss_scan_uri",
        "detector_name",
        "xrf_spectra_uri_template",
        "output_root_uri",
    ],
):
    """Add single-scan XRF spectra from multiple detectors"""

    def run(self):
        start_time = nexus_utils.now()
        params = {**DEFAULTS, **self.get_input_values()}

        bliss_scan_uri: str = params["bliss_scan_uri"]
        detector_names: Sequence[str] = params["detector_names"]
        xrf_spectra_uri_template: str = params["xrf_spectra_uri_template"]
        detector_normalization_template: str = params["detector_normalization_template"]
        output_root_uri: str = params["output_root_uri"]

        if len(detector_names) < 1:
            raise ValueError("Expected at least 1 detector to sum")

        _, scan_h5path = split_h5uri(bliss_scan_uri)

        sumdetector_name = params["output_detector_name"]

        with nexus_utils.save_in_ewoks_process(
            output_root_uri,
            start_time,
            process_config={
                "detector_normalization_template": detector_normalization_template
            },
            default_levels=(scan_h5path, "sumspectra"),
        ) as (process_group, already_existed):
            outentry = process_group.parent
            if not already_existed:
                sum_spectra: numpy.ndarray = sum_spectra_from_hdf5(
                    bliss_scan_uri,
                    xrf_spectra_uri_template,
                    detector_normalization_template,
                    detector_names,
                )

                link_bliss_scan(outentry, bliss_scan_uri, retry_timeout=0)

                nxdata = nexus_utils.create_nxdata(
                    process_group, "mcasum", signal="data"
                )
                nxdata.attrs["interpretation"] = "spectrum"

                dataset_kwargs = guess_dataset_config(
                    scan_shape=(sum_spectra.shape[0],),
                    detector_shape=(sum_spectra.shape[1],),
                    dtype=sum_spectra.dtype,
                )
                dset = nxdata.create_dataset("data", data=sum_spectra, **dataset_kwargs)

                nxdetector = outentry["instrument"].create_group(sumdetector_name)
                nxdetector.attrs["NX_class"] = "NXdetector"
                create_hdf5_link(nxdetector, "data", dset)
                create_hdf5_link(outentry["measurement"], sumdetector_name, dset)

            output_root_uri = f"{outentry.file.filename}::{outentry.name}"

        self.outputs.bliss_scan_uri = output_root_uri
        self.outputs.detector_name = sumdetector_name
        self.outputs.xrf_spectra_uri_template = DEFAULTS["xrf_spectra_uri_template"]
        self.outputs.output_root_uri = output_root_uri
