import h5py
import numpy

from ..tasks.normalization import norm_utils


def test_normalization_coefficient(tmp_path):
    live_time = numpy.random.uniform(low=0.08, high=0.1, size=11)
    iodet = numpy.random.uniform(low=0.08, high=0.1, size=10)
    with h5py.File(str(tmp_path / "dataset.h5"), mode="w") as f:
        f["/1.1/instrument/fx_sxm_det0/live_time"] = live_time
        f["/1.1/instrument/iodet/data"] = iodet
        weight_uri_root = f"{f.filename}::/1.1"

    normalization_expression = "0.1/<instrument/fx_sxm_det0/live_time>*np.nanmean(<instrument/iodet/data>)/<instrument/iodet/data>"

    expected = numpy.empty((11,), dtype=float)
    expected[:10] = 0.1 / live_time[:10] * numpy.mean(iodet[:10]) / iodet[:10]
    expected[-1] = numpy.nan
    coefficient = norm_utils.normalization_coefficient(
        weight_uri_root, normalization_expression
    )
    numpy.testing.assert_array_equal(expected, coefficient)
