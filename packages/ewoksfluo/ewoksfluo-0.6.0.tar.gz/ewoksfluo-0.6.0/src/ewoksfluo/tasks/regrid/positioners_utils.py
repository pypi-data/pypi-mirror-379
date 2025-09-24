from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple

import numpy

from ...io import hdf5


def read_position_suburis(
    bliss_scan_uri: str,
    position_suburis: Sequence[str],
    axes_units: Optional[Dict[str, str]] = None,
) -> Tuple[List[numpy.ndarray], List[str], List[Optional[str]]]:
    data = [
        get_position_data(bliss_scan_uri, position_suburi)
        for position_suburi in position_suburis
    ]
    positions, units = zip(*data)
    names = [[s for s in name.split("/") if s][-1] for name in position_suburis]
    if axes_units:
        units = [
            unit if unit else axes_units.get(name) for name, unit in zip(names, units)
        ]
    return positions, names, units


def get_position_data(
    bliss_scan_uri: str, position_suburi: str
) -> Tuple[numpy.ndarray, Optional[str]]:
    """Get position data with units from HDF5"""
    scan_filename, scan_h5path = hdf5.split_h5uri(bliss_scan_uri)

    with hdf5.FileReadAccess(scan_filename) as scan_file:
        scan_grp = scan_file[scan_h5path]
        pos_dataset = scan_grp[position_suburi]
        assert hdf5.is_dataset(pos_dataset)

        unit = pos_dataset.attrs.get("units")
        if not unit:
            posi = position_suburi.split("/")[-1]
            url = f"instrument/positioners_start/{posi}"
            if url in scan_grp:
                unit = scan_grp[url].attrs.get("units")

        return pos_dataset[()], unit


def get_scan_position_suburis(
    bliss_scan_uri: str, ignore_positioners: Optional[Sequence[str]] = None
) -> List[str]:
    """Get all scan sub-URI's for positioners which were scanned."""
    scan_filename, scan_h5path = hdf5.split_h5uri(bliss_scan_uri)

    with hdf5.FileReadAccess(scan_filename) as scan_file:
        scan_grp = scan_file[scan_h5path]
        positioners = scan_grp["instrument/positioners_start"]
        positioners = set(positioners)
        counters = set(scan_grp["measurement"])
        positioners &= counters
        if ignore_positioners:
            positioners -= set(ignore_positioners)
        # E.g. order ["sampz", "sampy"]
        # The first dimension in pymca and silx is plotted vertically
        return [f"measurement/{s}" for s in reversed(sorted(positioners))]
