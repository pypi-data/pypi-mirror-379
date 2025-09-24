import h5py
import numpy
import pytest

from ..tasks.sum_detectors import sum_utils


@pytest.mark.parametrize("array_chunk_size", [1, 2, 3])
@pytest.mark.parametrize("normalize", [True, False])
def test_sum_spectra(tmp_path, monkeypatch, array_chunk_size, normalize):
    filename = str(tmp_path / "data.h5")

    npts = 10
    data = {
        "mca_det0": {
            "data": numpy.random.uniform(10, 100, (npts, 2048)),
            "live_time": numpy.random.uniform(0.05, 0.099, npts),
        },
        "mca_det1": {
            "data": numpy.random.uniform(10, 100, (npts, 2048)),
            "live_time": numpy.random.uniform(0.05, 0.099, npts),
        },
    }

    if normalize:
        mca_det0_weighted = (
            data["mca_det0"]["data"]
            / data["mca_det0"]["live_time"][:, numpy.newaxis]
            * 0.1
        )
        mca_det1_weighted = (
            data["mca_det1"]["data"]
            / data["mca_det1"]["live_time"][:, numpy.newaxis]
            * 0.1
        )
        expected_sum_spectra = mca_det0_weighted + mca_det1_weighted
    else:
        expected_sum_spectra = data["mca_det0"]["data"] + data["mca_det1"]["data"]

    with h5py.File(filename, "w") as f:
        f["/1.1/instrument/mca_det0/data"] = data["mca_det0"]["data"]
        f["/1.1/instrument/mca_det0/live_time"] = data["mca_det0"]["live_time"]
        f["/1.1/instrument/mca_det1/data"] = data["mca_det1"]["data"]
        f["/1.1/instrument/mca_det1/live_time"] = data["mca_det1"]["live_time"]

    def patched_array_chunk_size(*args, **_):
        return array_chunk_size

    monkeypatch.setattr(sum_utils, "array_chunk_size", patched_array_chunk_size)

    if normalize:
        detector_normalization_template = "0.1/<instrument/{}/live_time>"
    else:
        detector_normalization_template = None

    sum_spectra = sum_utils.sum_spectra_from_hdf5(
        bliss_scan_uri=f"{filename}::/1.1",
        xrf_spectra_uri_template="instrument/{}/data",
        detector_normalization_template=detector_normalization_template,
        detector_names=["mca_det0", "mca_det1"],
    )

    numpy.testing.assert_allclose(sum_spectra, expected_sum_spectra)
