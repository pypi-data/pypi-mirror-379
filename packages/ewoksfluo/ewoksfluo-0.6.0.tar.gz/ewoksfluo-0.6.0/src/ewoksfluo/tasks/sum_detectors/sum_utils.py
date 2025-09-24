import itertools
import logging
from typing import Any
from typing import Dict
from typing import Generator
from typing import Iterator
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import Union

import numpy
from numpy.typing import DTypeLike

from ...io import hdf5
from ...resource_utils import array_chunk_size
from ...resource_utils import log_required_memory
from .. import xrf_results
from ..math import eval_hdf5_expression
from ..math import format_expression_template

_logger = logging.getLogger(__name__)


def detector_weight_iterator(
    weight_uri_root: str, weight_expressions: Sequence[str]
) -> Generator[numpy.ndarray, None, None]:
    """
    :param weight_uri_root: HDF5 root group under which the detector weight datasets can be found.
    :param weight_expressions: Arithmetic expression for each detector to calculated the weight for addition from HDF5 datasets.
    """
    for weight_expression in weight_expressions:
        yield eval_hdf5_expression(weight_uri_root, weight_expression)


def detector_weight_iterator_stack(
    weight_uri_roots: Sequence[str], weight_expressions: Sequence[str]
) -> Generator[numpy.ndarray, None, None]:
    """
    :param weight_uri_roots: HDF5 root group under which the detector weight datasets can be found.
    :param weight_expressions: Arithmetic expression for each detector to calculated the weight for addition from HDF5 datasets.
    """
    for weight_expression in weight_expressions:
        detector_weight = [
            eval_hdf5_expression(weight_uri_root, weight_expression)
            for weight_uri_root in weight_uri_roots
        ]
        yield numpy.stack(detector_weight, axis=0)


def save_summed_xrf_results(
    xrf_results_uris: Sequence[str],
    detector_weights: Iterator[numpy.ndarray],
    output_root_uri: str,
    process_config: Dict[str, Any],
) -> str:
    """
    :param xrf_results_uris: HDF5 group for each detector that contains the "parameters", "uncertainties" and "massfractions" groups.
    :param detector_weights: Weights for each detector.
    :param output_root_uri: Root HDF5 URL under which to save the results as NXprocess
    :returns: URI to summed fit result group
    """
    parameters, uncertainties, massfractions = compute_summed_xrf_results(
        xrf_results_uris, detector_weights
    )
    return xrf_results.save_xrf_results(
        output_root_uri,
        "sum",
        process_config,
        parameters,
        uncertainties,
        massfractions,
    )


def compute_summed_xrf_results(
    xrf_results_uris: Sequence[str], detector_weights: Iterator[numpy.ndarray]
) -> Tuple[
    Dict[str, numpy.ndarray], Dict[str, numpy.ndarray], Dict[str, numpy.ndarray]
]:
    r"""Compute the weighted sum of the peak areas, associated uncertainties and mass fractions for several detectors.

    For elemental peak areas

    .. math::

        A(\mathrm{Fe}) = \sum_i{\left[ W_i A_i(\mathrm{Fe}) \right] }

    For their uncertainties

    .. math::

        \sigma_{A}(\mathrm{Fe}) = \sqrt{ \sum_i\left[ W_i^2 \sigma_{A_i}^2(\mathrm{Fe}) \right] }

    For elemental mass fractions, in addition to the detector weight we also weight for the peak area

    .. math::

        M(\mathrm{Fe}) = \sum_i{\left[ W_i M_i(\mathrm{Fe}) \frac{W_i A_i(\mathrm{Fe})}{A(\mathrm{Fe})} \right] }

    The variable :math:`W_i` is the weight for detector :math:`i` which is typically the inverse of the live time.

    :param xrf_results_uris: HDF5 group for each detector that contains the "parameters", "uncertainties" and "massfractions" groups.
    :param detector_weights: Weights for each detector.
    :returns: summed peak areas, associated uncertainties, averaged weight fractions
    """
    summed_parameters = {}
    summed_variances = {}
    averaged_massfractions = {}

    for xrf_results_uri, detector_weight in itertools.zip_longest(
        xrf_results_uris, detector_weights, fillvalue=None
    ):
        if xrf_results_uri is None or detector_weight is None:
            raise ValueError(
                "The number of arithmetic expressions but be equal to the number of detectors"
            )

        fit_filename, fit_h5path = xrf_results_uri.split("::")

        with hdf5.FileReadAccess(fit_filename) as h5file:
            xrf_results_group = h5file[fit_h5path]
            assert hdf5.is_group(xrf_results_group)

            # Sum the peak areas and average mass fractions
            param_group = xrf_results_group["parameters"]
            assert hdf5.is_group(param_group)
            massfrac_group = xrf_results_group.get("massfractions", dict())
            for dset_name, dset in param_group.items():
                if not xrf_results.is_peak_area(dset):
                    continue

                wparam_value = dset[()] * detector_weight
                if dset_name in summed_parameters:
                    summed_parameters[dset_name] += wparam_value
                else:
                    summed_parameters[dset_name] = wparam_value

                if dset_name not in massfrac_group:
                    continue

                wmassfrac_value = massfrac_group[dset_name][()] * detector_weight
                wmassfrac_num = wparam_value * wmassfrac_value
                if dset_name in averaged_massfractions:
                    averaged_massfractions[dset_name] += wmassfrac_num
                else:
                    averaged_massfractions[dset_name] = wmassfrac_num

            # Propagate error on peak areas
            uncertainties_group = xrf_results_group["uncertainties"]
            assert hdf5.is_group(uncertainties_group)
            for dset_name, dset in uncertainties_group.items():
                if not hdf5.is_dataset(dset):
                    continue
                wvar_value = dset[()] ** 2 * detector_weight**2
                if dset_name in summed_variances:
                    summed_variances[dset_name] += wvar_value
                else:
                    summed_variances[dset_name] = wvar_value

    summed_uncertainties = {k: numpy.sqrt(v) for k, v in summed_variances.items()}

    if averaged_massfractions:
        averaged_massfractions = {
            k: v / summed_parameters[k] for k, v in averaged_massfractions.items()
        }

    return summed_parameters, summed_uncertainties, averaged_massfractions


def sum_spectra_from_hdf5(
    bliss_scan_uri: str,
    xrf_spectra_uri_template: str,
    detector_normalization_template: Optional[str],
    detector_names: List[str],
) -> Optional[numpy.ndarray]:
    r"""Add spectra from multiple detectors after normalizing the spectra to a common live time.

    .. math::

        MCA(\mathrm{Fe}) = \sum_i{\left[ W_i MCA_i \right] }

    :param bliss_scan_uri: BLISS scan URI. For example `"/path/to/data.g5::/1.1"`.
    :param xrf_spectra_uri_template: XRF spectra path with respect to the BLISS scan URI. For example `"instrument/{}/data"`.
    :param detector_normalization_template: XRF spectra normalization template with variables
                                            with respect to the BLISS scan URI. For example `"0.1/<instrument/{}/live_time>"`.
    :param detector_names: List of names to be used in the templates.
    :returns: summed XRF spectra
    """
    input_file, scan_h5path = hdf5.split_h5uri(bliss_scan_uri)
    with hdf5.FileReadAccess(input_file) as h5file:
        sum_spectra = None
        chunk_size = 1
        scan_group = h5file[scan_h5path]

        for detector_name in detector_names:
            # Check dataset with XRF spectra
            xrf_spectra_uri = xrf_spectra_uri_template.format(detector_name)
            xrf_spectra_dataset = scan_group[xrf_spectra_uri]
            if not hdf5.is_dataset(xrf_spectra_dataset):
                raise ValueError(f"{xrf_spectra_uri!r} is not an HDF5 dataset")
            if not xrf_spectra_dataset.ndim == 2:
                raise ValueError(f"{xrf_spectra_uri!r} is not 2D")
            shape = xrf_spectra_dataset.shape
            dtype = xrf_spectra_dataset.dtype
            if xrf_spectra_dataset.dtype == numpy.float64:
                weight_dtype = numpy.float64
            else:
                weight_dtype = numpy.float32

            # Calculate the detector weights for the sum
            weights = _get_detector_weights(
                bliss_scan_uri,
                detector_name,
                detector_normalization_template,
                weight_dtype,
            )
            if weights is None:
                final_dtype = dtype
            else:
                final_dtype = weight_dtype
                if weights.ndim > 1:
                    raise ValueError(
                        f"Weights for detector {detector_name!r} is not a scalar or 1D"
                    )
                if weights.size != shape[0]:
                    raise ValueError(
                        f"Number of detector weights and number of spectra for {detector_name!r} are not the same."
                    )
                weights = weights.astype(final_dtype)

            # Prepare array to hold the sum
            if sum_spectra is None:
                if weights is None:
                    # Memory: 1 array
                    multiplier = 1
                else:
                    # Memory: 1 array and 1 cast array
                    multiplier = 2

                log_required_memory(
                    "initialize sum spectrum",
                    shape,
                    dtype,
                    multiplier=multiplier + 0.1,
                )
                sum_spectra = xrf_spectra_dataset[()]
                if weights is not None:
                    sum_spectra = sum_spectra.astype(final_dtype)
                    sum_spectra *= weights.reshape(-1, 1)

                chunk_size = array_chunk_size(shape, dtype, multiplier=multiplier + 0.1)
                log_required_memory(
                    "sum XRF spectra with chunking",
                    shape,
                    dtype,
                    multiplier=multiplier * chunk_size / shape[0],
                )
                continue

            # Add spectra
            if weights is None:
                for i in range(0, shape[0], chunk_size):
                    chunk = xrf_spectra_dataset[i : i + chunk_size]
                    sum_spectra[i : i + chunk_size] += chunk
            else:
                for i in range(0, shape[0], chunk_size):
                    chunk = xrf_spectra_dataset[i : i + chunk_size]
                    chunk = chunk.astype(final_dtype)
                    w_chunk = weights[i : i + chunk_size].reshape(-1, 1)
                    chunk *= w_chunk
                    sum_spectra[i : i + chunk_size] += chunk

    return sum_spectra


def _get_detector_weights(
    bliss_scan_uri: str,
    detector_name: str,
    detector_normalization_template: Optional[str],
    cast_dtype: DTypeLike,
) -> Union[numpy.ndarray, None]:
    if detector_normalization_template is None:
        _logger.warning(
            "Add detector %r to sum spectra WITHOUT weights",
            detector_name,
        )
        return

    weight_expression = format_expression_template(
        detector_normalization_template, detector_name
    )
    _logger.info(
        "Add detector %r to sum spectra with weights %s",
        detector_name,
        weight_expression,
    )
    weights = eval_hdf5_expression(bliss_scan_uri, weight_expression)
    return numpy.asarray(weights, dtype=cast_dtype)
