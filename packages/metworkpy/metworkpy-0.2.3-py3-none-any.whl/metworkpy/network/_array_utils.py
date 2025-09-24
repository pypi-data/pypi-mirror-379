"""Utility methods for array manipulation for creating adjacency matrices"""

# Imports
# Future
from __future__ import annotations

# Standard Library Imports
import functools

# External Imports
import numpy as np
from numpy.typing import ArrayLike
from scipy import sparse
from scipy.sparse import csc_array, csr_array, dok_array


# Local Imports


def _split_arr_col(
    arr: ArrayLike | csc_array | csr_array, into: int = 2
) -> tuple[ArrayLike | csc_array | csr_array, ...]:
    """Splits an interleaved array by column

    Parameters
    ----------
    arr : ArrayLike | csc_array | csr_array
        Array to split
    into : int
        Number of arrays to split the original array into

    Returns
    -------
    tuple[ArrayLike | csc_array | csr_array, ...]
        Tuple of split arrays

    Notes
    -----
    This method treats the original array as though the columns were interleaved.
    So, if into is 2, it will return a tuple with each even column in the first
    subarray, and each odd column in the second subarray.
    """
    return tuple(arr[:, i::into] for i in range(into))


def _split_arr_row(
    arr: ArrayLike | csc_array | csr_array, into: int = 2
) -> tuple[ArrayLike | csc_array | csr_array, ...]:
    """Splits an interleaved array by row

    Parameters
    ----------
    arr : ArrayLike | csc_array | csr_array
        Array to split
    into
        Number of arrays to split the original array into

    Returns
    -------
    ArrayLike | csc_array | csr_array

    Notes
    -----
    This method treats the original array as though the rows were interleaved.
    So, if into is 2, it will return a tuple with each even row in the first
    subarray, and each odd row in the second subarray.
    """
    return tuple(arr[i::into, :] for i in range(into))


def _split_arr_sign(
    arr: ArrayLike | csc_array | csr_array,
) -> tuple[ArrayLike | csc_array | csr_array, ArrayLike | csc_array | csr_array]:
    """Split an array based on signs of entries

    Parameters
    ----------
    arr : ArrayLike | sparray
        Array to split, can be dense or scipy.sparse csc, csr, dok, lil

    Returns
    -------
    tuple[ArrayLike | sparray, ArrayLike | sparray]
        Tuple of arrays, first will be all the positive entries, and
        second will be all the negative entries
    """
    # Handle sparse array
    if sparse.issparse(arr):
        pos_arr = sparse.dok_array(arr.shape)
        neg_arr = sparse.dok_array(arr.shape)

        # Set positive elements
        pos_elem = arr.sign() == 1
        pos_arr[pos_elem] = arr[pos_elem]

        # Set negative elements
        neg_elem = arr.sign() == -1
        neg_arr[neg_elem] = arr[neg_elem]
        return pos_arr.asformat(arr.format), neg_arr.asformat(arr.format)
    # Convert
    try:
        arr = np.array(arr)
    except Exception as err:
        raise ValueError("Couldn't coerce arr to numpy array") from err
    pos_arr = np.zeros(arr.shape, dtype=arr.dtype)
    neg_arr = np.zeros(arr.shape, dtype=arr.dtype)

    pos_elem = np.sign(arr) == 1
    neg_elem = np.sign(arr) == -1

    pos_arr[pos_elem] = arr[pos_elem]
    neg_arr[neg_elem] = arr[neg_elem]

    return pos_arr, neg_arr


def _sparse_max(*arr_list: csc_array | csr_array) -> csc_array | csr_array:
    """Find the element wise max of a list of sparse arrays

    Parameters
    ----------
    *arr_list : list[csc_array| csr_array, ...]
        Sequence of csc or csr sparse arrays

    Returns
    -------
    csc_array | csr_array
        Element wise maximum of sparse arrays
    """
    return functools.reduce(lambda x, y: x.maximum(y), arr_list)


def _sparse_mean(*arr_list: csc_array | csr_array) -> csc_array | csr_array:
    """Find the element wise max of a list of sparse arrays

    Parameters
    ----------
    *arr_list : list[csc_array| csr_array, ...]
        Sequence of csc or csr sparse arrays

    Returns
    -------
    csc_array | csr_array
        Element wise maximum of sparse arrays
    """
    return functools.reduce(lambda x, y: x + y, arr_list) / len(arr_list)


def _broadcast_mult_arr_vec(arr: csr_array, vec: csc_array):
    """Elementwise multiplication of each row of arr by vec.

    Parameters
    ----------
    arr : csr_array
        Array to multiply
    vec : csc_array
        Vector to multiply

    Returns
    -------
    csr_array
        Result of multiplication
    """
    if arr.shape[1] != vec.shape[0]:
        raise ValueError("Shape mismatch")
    res = dok_array(arr.shape)
    for i in range(arr.shape[0]):
        res[[i], :] = arr[[i], :] * vec.T
    return res.tocsr()
