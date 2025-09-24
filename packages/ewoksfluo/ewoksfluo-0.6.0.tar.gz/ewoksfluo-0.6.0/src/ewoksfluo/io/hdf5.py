import os
import pathlib
import warnings
from collections import abc
from contextlib import contextmanager
from typing import Dict
from typing import Generator
from typing import Optional
from typing import Tuple
from typing import Union

import h5py
from silx.io import h5py_utils
from silx.io.url import DataUrl


def split_h5uri(url: str) -> Tuple[str, str]:
    obj = DataUrl(url)
    return obj.file_path(), obj.data_path() or ""


def join_h5url(root_url: str, sub_url: str) -> str:
    file_path, data_path = split_h5uri(root_url)

    while data_path.endswith("/"):
        data_path = data_path[:-1]
    while data_path.endswith("::"):
        data_path = data_path[:-2]

    while sub_url.startswith("/"):
        sub_url = sub_url[1:]
    while sub_url.endswith("/"):
        sub_url = sub_url[:-1]

    return f"{file_path}::{data_path}/{sub_url}"


def is_file(item) -> bool:
    return isinstance(item, (h5py.File, FileModExtAccess))


def is_group(item) -> bool:
    return isinstance(item, (h5py.Group, GroupModExtAccess))


def is_dataset(item) -> bool:
    return isinstance(item, h5py.Dataset)


FileType = Union[h5py.File, "FileModExtAccess"]
GroupType = Union[h5py.Group, "GroupModExtAccess"]
DatasetType = h5py.Dataset


class GroupModExtAccess(abc.MutableMapping):
    """
    Wrapper around h5py.Group that delegates path resolution
    to the owning FileModExtAccess.
    """

    def __init__(self, native_group: h5py.Group, file_wrapper: "FileModExtAccess"):
        self._native_group = native_group
        self._file_wrapper = file_wrapper

    def __getitem__(self, name: str) -> Union[h5py.Dataset, "GroupModExtAccess"]:
        return self._file_wrapper._resolve_from(self._native_group, name)

    def __setitem__(self, name: str, value) -> None:
        parent_name, _, set_name = name.rpartition("/")
        parent = self._file_wrapper._resolve_from(self._native_group, parent_name)
        parent._native_group[set_name] = value

    def __delitem__(self, name: str) -> None:
        parent_name, _, del_name = name.rpartition("/")
        parent = self._file_wrapper._resolve_from(self._native_group, parent_name)
        del parent._native_group[del_name]

    def __iter__(self):
        return iter(self._native_group)

    def __len__(self) -> int:
        return len(self._native_group)

    @property
    def name(self) -> str:
        return self._native_group.name

    @property
    def file(self) -> "FileModExtAccess":
        return self._file_wrapper

    def get(self, name: str, default=None, getclass=False, getlink=False):
        if getclass or getlink:
            return self._native_group.get(
                name, default=default, getclass=getclass, getlink=getlink
            )
        if name in self._native_group:
            return self[name]
        return default

    @property
    def attrs(self):
        return self._native_group.attrs

    def __repr__(self):
        return f'<{type(self).__name__} "{self.name}">'


class FileModExtAccess(GroupModExtAccess):
    """
    Wrapper around an ``h5py_utils.File`` that ensures any ``h5py.ExternalLink``
    is opened with alternative access parameters.
    """

    def __init__(self, filename: Union[str, pathlib.Path], **open_options):
        if not isinstance(filename, (str, pathlib.Path)):
            raise TypeError("filename must be a string")

        self._external_open_options = dict(open_options)
        self._native_file = h5py_utils.File(filename, **open_options)
        self._external_files: Dict[str, FileModExtAccess] = {}
        super().__init__(self._native_file, self)

    def set_external_access(self, **opts):
        self._external_open_options.update(opts)

    @property
    def filename(self) -> str:
        return self._native_file.filename

    def close(self):
        # Close external files then root file
        for root in list(self._external_files.values()):
            try:
                root.close()
            except Exception:
                pass
        self._external_files.clear()
        if self._native_file is not None:
            try:
                self._native_file.close()
            finally:
                self._native_file = None

    def __enter__(self) -> "FileModExtAccess":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()

    def _open_external(
        self, filename: str, owner_file: h5py_utils.File
    ) -> h5py_utils.File:
        """Open (or return cached) external file. Always opened with read + no locking."""
        if not os.path.isabs(filename):
            base_dir = os.path.dirname(owner_file.filename)
            filename = os.path.join(base_dir, filename)

        key = os.path.realpath(filename)
        if key in self._external_files:
            return self._external_files[key]

        ext_h5 = FileModExtAccess(filename, **self._external_open_options)
        self._external_files[key] = ext_h5
        return ext_h5

    def _resolve_from(
        self, native_parent: Union[h5py_utils.File, h5py.Group], name: str
    ) -> Union[h5py.Dataset, "GroupModExtAccess"]:
        # If absolute, start from the file that owns the parent
        is_absolute = name.startswith("/")
        if is_absolute:
            native_current = native_parent.file
        else:
            native_current = native_parent
        current_file = self

        # Traverse tree structure explicitly with explicit link resolution
        parts = [p for p in name.split("/") if p]
        i = 0
        while i < len(parts):
            part = parts[i]
            try:
                link = native_current.get(part, getlink=True)
            except Exception:
                link = None

            if isinstance(link, h5py.ExternalLink):
                ext_file = self._open_external(link.filename, native_current.file)
                link_parts = [p for p in link.path.split("/") if p]
                # jump into external target path + remaining tail
                parts = link_parts + parts[i + 1 :]
                native_current = ext_file._native_file
                current_file = ext_file
                i = 0
                continue

            if isinstance(link, h5py.SoftLink):
                link_parts = [p for p in link.path.split("/") if p]
                parts = link_parts + parts[i + 1 :]
                link_is_absolute = link.path.startswith("/")
                if link_is_absolute:
                    native_current = native_current.file
                i = 0
                continue

            # Hard link, dataset, group or virtual dataset
            obj = native_current[part]

            i += 1
            if i < len(parts):
                # Need to descend further: obj must be a group
                if isinstance(obj, h5py.Group):
                    native_current = obj
                    continue
                else:
                    raise KeyError(
                        f"Cannot descend into non-group '{part}' while resolving path '{name}'"
                    )
            else:
                # Last component: return dataset or wrapped group
                native_current = obj

        # Return dataset or wrapped group
        if isinstance(native_current, h5py.Group):
            return GroupModExtAccess(native_current, current_file)
        return native_current


class FileReadAccess(FileModExtAccess):
    """Use in cases where you want to read something from an HDF5 which
    might be already open for writing.
    """

    def __init__(self, filename: Union[str, pathlib.Path], mode: str = "r", **kwargs):
        if not isinstance(filename, (str, pathlib.Path)):
            raise TypeError("filename must be a string")
        assert mode == "r", "must be opened read-only"
        try:
            super().__init__(filename, mode=mode, **kwargs)
        except Exception:
            super().__init__(filename, mode="a", **kwargs)
            self.set_external_access(mode="r")


class ReadHdf5File(FileReadAccess):

    def __init__(self, *args, **kwargs):
        warnings.warn(
            "ReadHdf5File is deprecated, please use FileReadAccess instead.",
            category=DeprecationWarning,
            stacklevel=2,
        )
        super().__init__(*args, **kwargs)


@contextmanager
def retry_external_link(
    group: h5py.Group, name: str, item: Optional[Union[h5py.Group, h5py.Dataset]] = None
) -> Generator[Union[h5py.Group, h5py.Dataset], None, None]:
    """The file we save results in is opened in append mode. If we access external links to
    the raw Bliss data we might not have permission to open it in append mode (e.g. restored data).
    """
    warnings.warn(
        "retry_external_link is deprecated, please use ReadHdf5File instead to open the file.",
        category=DeprecationWarning,
        stacklevel=2,
    )

    if item is None:
        try:
            item = group[name]
        except (KeyError, ValueError):
            item = None
    if item is None:
        link = group.get(name, getlink=True)
        if not isinstance(link, h5py.ExternalLink):
            raise RuntimeError(f"Broken link '{group.name}/{name}'")

        external_filename = link.filename
        if not os.path.isabs(external_filename):
            parent_dir = os.path.dirname(group.file.filename)
            external_filename = os.path.abspath(
                os.path.normpath(os.path.join(parent_dir, external_filename))
            )

        with h5py_utils.File(external_filename, mode="r") as f:
            yield f[link.path]
    else:
        yield item
