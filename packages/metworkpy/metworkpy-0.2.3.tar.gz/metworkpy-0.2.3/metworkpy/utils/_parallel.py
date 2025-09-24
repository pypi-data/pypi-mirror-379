"""Utility functions for working with python multiprocessing"""

from __future__ import annotations

from multiprocessing import shared_memory
from typing import Tuple

import numpy as np


def _create_shared_memory_numpy_array(
    input_array, name: str | None = None
) -> Tuple[int, int, np.dtype, str]:
    """Create a numpy array in shared memory from `input_array`

    Parameters
    ----------
    input_array : np.ndarray
        Numpy array to create shared memory array from
    name : str
        Name to give shared memory

    Returns
    -------
    Tuple[int, int, np.dtype, str]
        Tuple of (number of rows, number of columns, dtype, name)
    """
    shm = shared_memory.SharedMemory(name=name, create=True, size=input_array.nbytes)
    shared_array = np.ndarray(
        input_array.shape, dtype=input_array.dtype, buffer=shm.buf
    )
    shared_array[:] = input_array
    nrow, ncol = input_array.shape
    return nrow, ncol, input_array.dtype, shm.name
