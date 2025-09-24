import os
import stat

import h5py
import pytest

from ..io import hdf5

skip_if_root = pytest.mark.skipif(
    os.geteuid() == 0, reason="Test requires non-root permissions"
)


def test_join_h5url():
    assert hdf5.join_h5url("filename.h5", "") == "filename.h5::/"
    assert hdf5.join_h5url("filename.h5::/", "/") == "filename.h5::/"

    assert hdf5.join_h5url("filename.h5", "1.1") == "filename.h5::/1.1"
    assert hdf5.join_h5url("filename.h5::/", "/1.1/") == "filename.h5::/1.1"


@pytest.fixture
def hdf5_files(tmp_path):
    root_path = tmp_path / "root.h5"
    ext_path = tmp_path / "ext.h5"

    with h5py.File(ext_path, "w") as ext:
        ext["/group/data"] = [4, 5, 6]

    with h5py.File(root_path, "w") as root:
        root["/internal/data"] = [1, 2, 3]
        root["/external1"] = h5py.ExternalLink("ext.h5", "/")
        root["/external2/data"] = h5py.ExternalLink("ext.h5", "/group/data")

    os.chmod(ext_path, stat.S_IREAD)
    yield root_path, ext_path
    os.chmod(ext_path, stat.S_IWRITE | stat.S_IREAD)


def test_read_access(hdf5_files):
    root_path, _ = hdf5_files

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        root.set_external_access(mode="r")

        assert "/internal/data" in root
        dset = root["/internal/data"]
        assert dset[()].tolist() == [1, 2, 3]

        assert "/external1/group/data" in root
        dset = root["/external1/group/data"]
        assert dset[()].tolist() == [4, 5, 6]

        assert "/external2/data" in root
        dset = root["/external2/data"]
        assert dset[()].tolist() == [4, 5, 6]

        assert "/internal/notexisting" not in root
        assert "/external1/group" in root
        assert "/external1/group/notexisting" not in root
        assert "/external2/notexisting" not in root


def test_write_access(hdf5_files):
    root_path, _ = hdf5_files

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        root.set_external_access(mode="r")
        dset = root["/internal/data"]
        dset[0] = 99
        assert dset[()].tolist() == [99, 2, 3]

        dset = root["/external1/group/data"]
        with pytest.raises(OSError):
            dset[0] = 99
        assert dset[()].tolist() == [4, 5, 6]

        dset = root["/external2/data"]
        with pytest.raises(OSError):
            dset[0] = 99
        assert dset[()].tolist() == [4, 5, 6]


@skip_if_root
def test_create_access(hdf5_files):
    root_path, ext_path = hdf5_files

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        root["/internal/new"] = 10
        assert root["/internal/new"][()] == 10

        with pytest.raises(PermissionError):
            root["/external1/group/new"] = 20

    os.chmod(ext_path, stat.S_IWRITE | stat.S_IREAD)

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        root["/external1/group/new"] = 30
        assert root["/external1/group/new"][()] == 30


@skip_if_root
def test_delete_access(hdf5_files):
    root_path, ext_path = hdf5_files

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        del root["/internal/data"]
        assert "/internal/data" not in root

        with pytest.raises(PermissionError):
            del root["/external1/group/data"]

        del root["/external2/data"]
        assert "/external2/data" not in root

    os.chmod(ext_path, stat.S_IWRITE | stat.S_IREAD)

    with hdf5.FileModExtAccess(root_path, mode="a") as root:
        del root["/external1/group/data"]

        assert "/external1/group/data" not in root
