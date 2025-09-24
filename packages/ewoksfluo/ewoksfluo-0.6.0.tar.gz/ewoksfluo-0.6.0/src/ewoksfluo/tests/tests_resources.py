import logging
from contextlib import contextmanager

import numpy

from .. import resource_utils


def test_job_parameters(system_4cpus_8gb):
    # 8 GB array
    shape = (1024, 1024, 1024)
    dtype = numpy.float64

    njobs = 1
    narrays_in_parallel, chunk_size_dim0 = resource_utils.job_parameters(
        njobs, shape, dtype
    )
    assert narrays_in_parallel == 1
    assert chunk_size_dim0 == 1024

    # Check MEM limit with chunking
    njobs = 2
    narrays_in_parallel, chunk_size_dim0 = resource_utils.job_parameters(
        njobs, shape, dtype
    )
    assert narrays_in_parallel == 2
    assert chunk_size_dim0 == 512

    # Check MEM limit without chunking
    njobs = 2
    narrays_in_parallel, chunk_size_dim0 = resource_utils.job_parameters(
        njobs, shape, dtype, chunking_possible=False
    )
    assert narrays_in_parallel == 1
    assert chunk_size_dim0 == 1024

    # Check CPU limit
    njobs = 16
    narrays_in_parallel, chunk_size_dim0 = resource_utils.job_parameters(
        njobs, shape, dtype
    )
    assert narrays_in_parallel == 3
    assert chunk_size_dim0 == 341


def test_log_required_memory(system_4cpus_8gb, caplog):
    # 4 GB array
    shape = (1024, 1024, 1024)
    dtype = numpy.float32
    level = logging.INFO
    expected = "Memory required to process data: 4.00 GB (available: 8.00 GB)"

    with _assert_logging(caplog, level, expected):
        resource_utils.log_required_memory("process data", shape, dtype)

    # 16 GB array
    shape = (2048, 1024, 1024)
    dtype = numpy.float64
    level = logging.WARNING
    expected = "Memory required to process data: 16.00 GB (available: 8.00 GB)"

    with _assert_logging(caplog, level, expected):
        resource_utils.log_required_memory("process data", shape, dtype)


@contextmanager
def _assert_logging(caplog, level, message):
    with caplog.at_level(level):
        yield

    messages = {r.message for r in caplog.records}
    assert message in messages
