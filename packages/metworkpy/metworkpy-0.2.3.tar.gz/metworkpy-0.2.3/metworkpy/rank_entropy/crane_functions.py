"""Functions for computing Centroid Rank Entropy (CRANE)"""

# Imports
# Standard Library Imports
from __future__ import annotations
from typing import Optional, Literal, Callable, Union, Tuple

# External Imports
import numpy as np
from numpy.typing import NDArray
import pandas as pd
from scipy.stats import rankdata, gaussian_kde

# Local imports
from metworkpy.rank_entropy._bootstrap_pvalue import _bootstrap_rank_entropy_p_value
from metworkpy.rank_entropy.rank_entropy_exceptions import NotFitError


# region Main Fuctions


def crane_gene_set_classification(
    expression_data: NDArray[float | int] | pd.DataFrame,
    sample_group1,
    sample_group2,
    gene_network,
    kernel_density_estimate: bool = True,
    bw_method: Optional[Union[str | float | Callable[[gaussian_kde], float]]] = None,
    iterations: int = 10_000,
    replace: bool = True,
    seed: Optional[int] = None,
    processes=1,
) -> Tuple[float, float]:
    """Calculate the classification rate using CRANE rank centroid distances for a given network and its significance

    Parameters
    ----------
    expression_data : np.ndarray | pd.DataFrame
        Gene expression data, either a numpy array or a pandas
        DataFrame, with rows representing different samples, and columns
        representing different genes
    sample_group1
        Which samples belong to group1. If expression_data is a numpy
        array, this should be a something able to index the rows of the
        array. If expression_data is a pandas dataframe, this should be
        something that can index rows of a dataframe inside a .loc (see
        pandas documentation for details)
    sample_group2
        Which samples belong to group2, see sample_group1 information
        for more details.
    gene_network
        Which genes belong to the gene network. If expression_data is a
        numpy array, this should be something able to index the columns
        of the array. If expression_data is a pandas dataframe, this
        should be something be anything that can index columns of a
        dataframe inside a .loc (see pandas documentation for details)
    kernel_density_estimate : bool
        Whether to use a kernel density estimate for calculating the
        p-value. If True, will use a Gaussian Kernel Density Estimate,
        if False will use an empirical CDF
    bw_method : Optional[Union[str|float|Callable[[gaussian_kde], float]]]
        Bandwidth method, see `scipy.stats.gaussian_kde <https://docs.sc
        ipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.h
        tml>`_ for details
    iterations : int
        Number of iterations to perform during bootstrapping the null
        distribution
    replace : bool
        Whether to sample with replacement when randomly sampling from
        the sample groups during bootstrapping
    seed : int
        Seed to use for the random number generation during
        bootstrapping
    processes : int
        Number of processes to use during the bootstrapping, default 1

    Returns
    -------
    Tuple[float,float]
        Tuple of the classification rate, and the significance level
        found via bootstrapping
    """
    return _bootstrap_rank_entropy_p_value(
        samples_array=expression_data,
        sample_group1=sample_group1,
        sample_group2=sample_group2,
        gene_network=gene_network,
        rank_entropy_fun=_crane_classification_rate,
        kernel_density_estimate=kernel_density_estimate,
        bw_method=bw_method,
        iterations=iterations,
        replace=replace,
        seed=seed,
        processes=processes,
    )


def crane_gene_set_entropy(
    expression_data: NDArray[float | int] | pd.DataFrame,
    sample_group1,
    sample_group2,
    gene_network,
    kernel_density_estimate: bool = True,
    bw_method: Optional[Union[str | float | Callable[[gaussian_kde], float]]] = None,
    iterations: int = 1_000,
    replace: bool = True,
    seed: Optional[int] = None,
    processes=1,
) -> Tuple[float, float]:
    """Calculate the difference in centroid rank entropy, and it's significance

    Parameters
    ----------
    expression_data : np.ndarray | pd.DataFrame
        Gene expression data, either a numpy array or a pandas
        DataFrame, with rows representing different samples, and columns
        representing different genes
    sample_group1
        Which samples belong to group1. If expression_data is a numpy
        array, this should be a something able to index the rows of the
        array. If expression_data is a pandas dataframe, this should be
        something that can index rows of a dataframe inside a .loc (see
        pandas documentation for details)
    sample_group2
        Which samples belong to group2, see sample_group1 information
        for more details.
    gene_network
        Which genes belong to the gene network. If expression_data is a
        numpy array, this should be something able to index the columns
        of the array. If expression_data is a pandas dataframe, this
        should be something be anything that can index columns of a
        dataframe inside a .loc (see pandas documentation for details)
    kernel_density_estimate : bool
        Whether to use a kernel density estimate for calculating the
        p-value. If True, will use a Gaussian Kernel Density Estimate,
        if False will use an empirical CDF
    bw_method : Optional[Union[str|float|Callable[[gaussian_kde], float]]]
        Bandwidth method, see `scipy.stats.gaussian_kde <https://docs.sc
        ipy.org/doc/scipy/reference/generated/scipy.stats.gaussian_kde.h
        tml>`_ for details
    iterations : int
        Number of iterations to perform during bootstrapping the null
        distribution
    replace : bool
        Whether to sample with replacement when randomly sampling from
        the sample groups during bootstrapping
    seed : int
        Seed to use for the random number generation during
        bootstrapping
    processes : int
        Number of processes to use during the bootstrapping, default 1

    Returns
    -------
    Tuple[float,float]
        Tuple of the difference in centroid rank entropy, and the
        significance level found via bootstrapping
    """
    return _bootstrap_rank_entropy_p_value(
        samples_array=expression_data,
        sample_group1=sample_group1,
        sample_group2=sample_group2,
        gene_network=gene_network,
        rank_entropy_fun=_crane_differential_entropy,
        kernel_density_estimate=kernel_density_estimate,
        bw_method=bw_method,
        iterations=iterations,
        replace=replace,
        seed=seed,
        processes=processes,
    )


# endregion Main Functions

# region CRANE Classifier


class CraneClassifier:
    """Class for using CRANE to perform classification

    Parameters
    ----------
    rank_centroids
    """

    def __init__(self):
        self.rank_centroids = None
        self.classes = None
        self.num_labels = None

    def fit(
        self,
        X: NDArray[float | int] | pd.DataFrame,
        y: NDArray[float | int] | pd.DataFrame | pd.Series,
    ) -> CraneClassifier:
        """Fit the classifier

        Parameters
        ----------
        X : NDArray[float|int]|pd.DataFrame
            Features array, should be a pandas DataFrame or numpy
            ndarray with columns representing genes in a gene network,
            and rows representing different samples, and values
            corresponding to expression level
        y : NDArray[float|int]|pd.DataFrame|pd.Series
            Target array, should be a pandas Series or numpy ndarray,
            with length equal to the number of rows in X. Each entry
            should represent the class of the corresponding sample in X.
            The order should correspond between X and y, and the indexes
            will not be aligned between them.

        Returns
        -------
        DiracClassifier
            Fitted DIRAC classifier object

        Notes
        -----
        This updates the classifier in place, and also returns itself.
        """
        rank_centroids = []
        classes = np.unique(y)

        if isinstance(X, pd.DataFrame):
            X = X.to_numpy()
        elif isinstance(X, np.ndarray):
            pass
        else:
            raise ValueError(
                "Invalid feature array type, must be pandas DataFrame or numpy ndarray"
            )

        if isinstance(y, pd.DataFrame) or isinstance(y, pd.Series):
            y = y.to_numpy()
        elif isinstance(y, np.ndarray):
            pass
        else:
            raise ValueError(
                "Invalid feature array type, must be pandas DataFrame or numpy ndarray"
            )

        # Reshape y to be 1D for easier indexing
        y = y.reshape(-1)

        for c in classes:
            # get all the rows corresponding to this class
            c_X = X[y == c, :]
            rank_centroids.append(_rank_centroid(c_X))

        self.rank_centroids = rank_centroids
        self.classes = classes
        self.num_labels = len(classes)
        return self

    def classify(
        self, X: NDArray[float | int] | pd.DataFrame
    ) -> Union[pd.Series, NDArray]:
        """Use the fitted classifier to classify samples

        Parameters
        ----------
        X : NDArray[float|int]|pd.DataFrame
            Features array, should be a pandas DataFrame or numpy
            ndarray with columns representing genes in a gene network,
            and rows representing different samples, and values
            corresponding to expression level

        Returns
        -------
        pd.Series|NDArray
            Predicted classes for all the samples. If X is a DataFrame,
            this will be a pandas Series; if X is a ndarray, this will
            be a 1-dimensional numpy array
        """
        if self.rank_centroids is None:
            raise NotFitError(
                "DIRAC Classifier must be fit before use (try calling the fit method)"
            )
        if isinstance(X, pd.DataFrame):
            return pd.Series(self._classify_arr(X.to_numpy()), index=X.index)
        elif isinstance(X, np.ndarray):
            return self._classify_arr(X)
        else:
            raise ValueError(
                f"X must be either a pandas DataFrame or a numpy ndarray, received {type(X)}"
            )

    def _classify_arr(self, X: NDArray[float | int]) -> NDArray:
        class_array = np.zeros((X.shape[0], self.num_labels), dtype=float)
        rank_array = _rank_array(X)
        for idx, centroid in enumerate(self.rank_centroids):
            class_array[:, idx] = np.sqrt(
                np.square(np.subtract(rank_array, centroid)).sum(axis=1)
            )
        return self.classes[np.argmin(class_array, axis=1)]


# endregion CRANE Classifier

# region Rank Centroid Functions


def _rank_array(
    in_array: NDArray[int | float],
    method: Literal[
        "average",
        "min",
        "max",
        "dense",
        "ordinal",
    ] = "average",
) -> NDArray[float]:
    return rankdata(in_array, method=method, axis=1, nan_policy="omit")


def _rank_centroid(in_array: [int | float]) -> NDArray[int]:
    return _rank_array(in_array=in_array).mean(axis=0).reshape(1, -1)


def _rank_grouping_score(in_array: [int | float]) -> NDArray[int]:
    ranked_array = _rank_array(in_array)
    centroid = ranked_array.mean(axis=0)
    return np.sqrt(np.square(np.subtract(ranked_array, centroid)).sum(axis=1)).mean()


def _crane_differential_entropy(
    a: NDArray[int | float],
    b: NDArray[int | float],
) -> float:
    return np.abs(_rank_grouping_score(a) - _rank_grouping_score(b))


# endregion Rank Centroid Functions

# region Classification rate functions


def _crane_classification_rate(
    a: NDArray[float | int], b: NDArray[float | int]
) -> float:
    # Compute the rank arrays
    rank_array_a = _rank_array(a)
    rank_array_b = _rank_array(b)

    # Compute the rank centroids
    centroid_a = rank_array_a.mean(axis=0).reshape(1, -1)
    centroid_b = rank_array_b.mean(axis=0).reshape(1, -1)

    # Calculate distances from the rank arrays to the centroids
    centroid_distance_a_array_a = np.sqrt(
        np.square(np.subtract(rank_array_a, centroid_a)).sum(axis=1)
    )
    centroid_distance_b_array_a = np.sqrt(
        np.square(np.subtract(rank_array_a, centroid_b)).sum(axis=1)
    )

    centroid_distance_a_array_b = np.sqrt(
        np.square(np.subtract(rank_array_b, centroid_a)).sum(axis=1)
    )
    centroid_distance_b_array_b = np.sqrt(
        np.square(np.subtract(rank_array_b, centroid_b)).sum(axis=1)
    )

    # Calculate the rank centroid distance difference
    dist_diff_a = centroid_distance_a_array_a - centroid_distance_b_array_a
    dist_diff_b = centroid_distance_a_array_b - centroid_distance_b_array_b

    # Calculate the accuracy
    total_samples = a.shape[0] + b.shape[0]
    correct_samples = (dist_diff_a < 0.0).sum() + (dist_diff_b >= 0.0).sum()

    return correct_samples / total_samples

    pass


# endregion Classification rate functions
