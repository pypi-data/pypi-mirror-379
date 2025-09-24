import logging
import os
import re
import subprocess
from typing import Optional
from typing import Tuple

import numpy
import psutil
from numpy.typing import DTypeLike

logger = logging.getLogger(__name__)


def log_required_memory(
    action: str, shape: Tuple[int, ...], dtype: DTypeLike, multiplier: int = 1
) -> None:
    """Log the memory required for the processing of an array."""
    required_bytes = _calculate_array_memory(shape, dtype) * multiplier
    required_bytes_str = _format_mem_size(required_bytes)
    available_bytes = _get_available_memory_bytes()
    available_bytes_str = _format_mem_size(available_bytes)

    logger.log(
        logging.WARNING if required_bytes > available_bytes else logging.INFO,
        "Memory required to %s: %s (available: %s)",
        action,
        required_bytes_str,
        available_bytes_str,
    )


def array_chunk_size(
    shape: Tuple[int, ...], dtype: DTypeLike, multiplier: int = 1
) -> int:
    """Process array with a chunk size along the first dimension to fit in memory."""
    required_bytes = _calculate_array_memory(shape, dtype) * multiplier
    available_mem = _get_available_memory_bytes()

    if required_bytes <= available_mem:
        logger.info("Process array in 1 chunk.")
        return shape[0]

    chunk_fraction = available_mem / required_bytes
    chunk_size_dim0 = max(1, int(shape[0] * chunk_fraction))
    nchunks = numpy.ceil(shape[0] / chunk_size_dim0)
    logger.info("Process array in %d chunks.", nchunks)
    return chunk_size_dim0


def job_parameters(
    narrays: int,
    shape: Tuple[int, ...],
    dtype: DTypeLike,
    multiplier: int = 1,
    chunking_possible: bool = True,
) -> Tuple[int, int]:
    """
    Return maximum number of parallel jobs and chunk size along the first
    dimension so that CPU and memory usage stay within available limits.
    """
    if narrays <= 0 or not shape or shape[0] == 0:
        return 0, 0  # scalar or empty or no array

    # Number of arrays we can process in parallel capped by available CPUs.
    cpu_cap = _get_available_cpus()
    narrays_in_parallel = min(cpu_cap, narrays)

    # Total memory required for processing full array's in parallel.
    mem_per_array = _calculate_array_memory(shape, dtype) * multiplier
    required_mem = narrays_in_parallel * mem_per_array

    # Allow when the available memory is not exceeded.
    available_mem = _get_available_memory_bytes()
    available_mem_str = _format_mem_size(available_mem)
    if required_mem <= available_mem:
        used_mem_str = _format_mem_size(required_mem)
        logger.info(
            "Process %d arrays with %d workers. Requires %s, %s available.",
            narrays,
            narrays_in_parallel,
            used_mem_str,
            available_mem_str,
        )
        return narrays_in_parallel, shape[0]

    if not chunking_possible:
        # Memory is exceeded and chunking is NOT allowed.
        # So reduce number of parallel jobs but require at
        # least one which could cause memory overuse.
        narrays_in_parallel = max(available_mem // mem_per_array, 1)
        required_mem = narrays_in_parallel * mem_per_array
        used_mem_str = _format_mem_size(required_mem)
        logger.info(
            "Process %d arrays with %d workers. Requires %s, %s available.",
            narrays,
            narrays_in_parallel,
            used_mem_str,
            available_mem_str,
        )
        return narrays_in_parallel, shape[0]

    # Memory is exceeded and chunking is allowed.
    # Reduce chunk size to fit memory but requires at
    # least chunk size 1 which could cause memory overuse.
    chunk_fraction = available_mem / required_mem
    chunk_size_dim0 = max(1, int(shape[0] * chunk_fraction))
    required_mem = narrays_in_parallel * int(mem_per_array * chunk_size_dim0 / shape[0])
    used_mem_str = _format_mem_size(required_mem)
    chunks_per_array = numpy.ceil(chunk_size_dim0 / shape[0]).astype(int)
    narray_chunks = narrays * chunks_per_array
    logger.info(
        "Process %d array chunks with %d workers. Requires %s, %s available.",
        narray_chunks,
        narrays_in_parallel,
        used_mem_str,
        available_mem_str,
    )
    return narrays_in_parallel, chunk_size_dim0


def _get_available_cpus(exclude_current: bool = True) -> int:
    """Get available CPUs. At least one."""
    cpus = psutil.Process().cpu_affinity() or ()
    return max(len(cpus) - exclude_current, 1)


def _get_available_memory_bytes() -> int:
    """Get available memory in bytes. Zero or higher."""
    available = _get_available_slurm_job_memory_bytes()
    if available is not None:
        return available
    available = _get_available_cgroup_memory_bytes()
    if available is not None:
        return available
    return _get_available_system_memory_bytes()


def _get_available_system_memory_bytes() -> int:
    return psutil.virtual_memory().available


def _get_available_slurm_job_memory_bytes() -> Optional[int]:
    requested = _get_slurm_requested_memory_bytes()
    current = _get_slurm_current_memory_usage_bytes()
    if current is None or requested is None:
        return
    return max(requested - current, 0)


def _get_slurm_requested_memory_bytes() -> Optional[int]:
    job_id = os.getenv("SLURM_JOB_ID")
    if not job_id:
        return None
    try:
        result = subprocess.run(
            ["sacct", "-j", job_id, "--format=ReqMem", "-P", "-n"],
            capture_output=True,
            text=True,
            check=True,
        )
        req_mem_str = result.stdout.strip()
        return _parse_mem_size(req_mem_str)
    except Exception:
        return None


def _get_slurm_current_memory_usage_bytes() -> Optional[int]:
    job_id = os.getenv("SLURM_JOB_ID")
    if not job_id:
        return None
    try:
        # Query sstat for the job's batch step memory usage
        result = subprocess.run(
            ["sstat", "-j", job_id, "--format=MaxRSS", "-P", "-n"],
            capture_output=True,
            text=True,
            check=True,
        )
        mem_str = result.stdout.strip()
        return _parse_mem_size(mem_str)
    except Exception:
        return None


def _get_available_cgroup_memory_bytes() -> Optional[int]:
    try:
        # cgroups v2
        if os.path.exists("/sys/fs/cgroup/memory.max"):
            with open("/sys/fs/cgroup/memory.max") as f:
                limit = f.read().strip()
            if limit == "max":
                return None
            limit = int(limit)
            with open("/sys/fs/cgroup/memory.current") as f:
                current = int(f.read().strip())
            return max(limit - current, 0)

        # cgroups v1
        if os.path.exists("/sys/fs/cgroup/memory/memory.limit_in_bytes"):
            with open("/sys/fs/cgroup/memory/memory.limit_in_bytes") as f:
                limit = int(f.read().strip())
            if limit > 1 << 60:
                return None  # unlimited
            with open("/sys/fs/cgroup/memory/memory.usage_in_bytes") as f:
                current = int(f.read().strip())
            return max(limit - current, 0)

    except Exception:
        return None


def _parse_mem_size(mem_str: str) -> Optional[int]:
    """
    Parse memory string from sstat (e.g. '500M', '1.2G') to an integer in bytes.
    Returns None if parsing fails.
    """
    if not mem_str:
        return None
    mem_str = mem_str.strip().upper()
    match = re.match(r"([\d\.]+)([KMGTP])?", mem_str)
    if not match:
        return None
    value, unit = match.groups()
    try:
        value = float(value)
    except ValueError:
        return None
    unit_multipliers = {
        None: 1,
        "K": 1024,
        "M": 1024**2,
        "G": 1024**3,
        "T": 1024**4,
        "P": 1024**5,
    }
    return int(value * unit_multipliers.get(unit, 1))


def _format_mem_size(num_bytes: int) -> str:
    units = ["bytes", "KB", "MB", "GB", "TB"]
    size = float(num_bytes)
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.2f} {units[unit_index]}"


def _calculate_array_memory(shape: Tuple[int, ...], dtype: DTypeLike) -> int:
    dtype = numpy.dtype(dtype)
    num_elements = numpy.prod(shape) if shape else 1
    return num_elements * dtype.itemsize


if __name__ == "__main__":
    available = _get_available_memory_bytes()
    available_slurm = _get_available_slurm_job_memory_bytes()
    available_cgroup = _get_available_cgroup_memory_bytes()
    available_system = _get_available_system_memory_bytes()

    print(
        f"Available memory: {_format_mem_size(available) if available else float('nan')}"
    )
    print(
        f"Available memory (SLURM): {_format_mem_size(available_slurm) if available_slurm else float('nan')}"
    )
    print(
        f"Available memory (cgroup): {_format_mem_size(available_cgroup) if available_cgroup else float('nan')}"
    )
    print(
        f"Available memory (system): {_format_mem_size(available_system) if available_system else float('nan')}"
    )
