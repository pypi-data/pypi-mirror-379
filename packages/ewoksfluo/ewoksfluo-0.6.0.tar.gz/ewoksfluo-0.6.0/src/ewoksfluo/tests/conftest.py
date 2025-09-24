import gc
import time

import psutil
import pytest
from ewoksorange.canvas.handler import OrangeCanvasHandler
from ewoksorange.tests.conftest import qtapp  # noqa F401

from .. import resource_utils
from ..io import hdf5


@pytest.fixture(scope="session")
def ewoks_orange_canvas(qtapp):  # noqa F811
    with OrangeCanvasHandler() as handler:
        yield handler
    # _close_hdf5_files()


def _close_hdf5_files():
    # TODO: ewoksfluo.gui.data_viewer.DataViewer.closeEvent does not get
    #       called so HDF5 stay open and this can cause a SEGFAULT
    while gc.collect():
        time.sleep(0.1)
    for obj in gc.get_objects():
        try:
            b = hdf5.is_file(obj)
        except Exception:
            continue
        if b:
            print(f"File object {obj}: filename={obj.filename}")
        if b and obj.id:
            obj.close()


@pytest.fixture(params=["normal", "slurm"])
def system_4cpus_8gb(request, monkeypatch) -> None:
    # Force known CPU count of 4 and memory of 8 GB

    class FakeProcess:
        def cpu_affinity(self):
            return [0, 1, 2, 3]  # Simulate 4 CPUs

    monkeypatch.setattr(psutil, "Process", lambda: FakeProcess())

    if request.param == "normal":
        monkeypatch.setattr(
            resource_utils, "_get_available_memory", lambda: 8 * 1024**3
        )
    elif request.param == "slurm":

        class SubprocessResponse:
            def __init__(self, stdout):
                self.stdout = stdout
                self.returncode = 0

        def mock_subprocess_run(cmd, **kwargs):
            if "sacct" in cmd:
                return SubprocessResponse("16G\n")  # 16 GB requested
            elif "sstat" in cmd:
                return SubprocessResponse("8G\n")  # 8 GB used
            return SubprocessResponse("")

        monkeypatch.setenv("SLURM_JOB_ID", "12345")
        monkeypatch.setattr(resource_utils.subprocess, "run", mock_subprocess_run)
    else:
        raise ValueError(f"{request.param}")

    # Verify that the patching works as expected
    cpus = resource_utils._get_available_cpus()
    assert cpus == 3
    mem = resource_utils._get_available_memory()
    assert mem == 8 * 1024**3
