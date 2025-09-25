from collections.abc import Iterable
from typing import Final, Self, cast

import faiss  # type: ignore
import numpy as np
from pydantic import ConfigDict, validate_call
from scipy.linalg.blas import sgemm  # type: ignore

from ._defs import (
    AffinityTransform,
    ExpQuantileTransform,
    IntStrictlyPositive,
    NumStrictlyPositive,
    Matrix,
)
from ._kmeans import KMeans
from ._spectral import SpectralClustering

# Constants
DEFAULT_AFFINITY_TRANSFORM: Final = ExpQuantileTransform(0.1, 1e4)


class SpectralBridges:
    """Spectral Bridges clustering algorithm.

    Attributes:
        random_state (int | None): Determines random number generation for centroid
            initialization.
        n_clusters (int): The number of clusters to form.
        n_nodes (int): Number of nodes or initial clusters.
        p (float): Power of the alpha_i.
        normed (bool): Whether to normalize the affinity matrix.
        n_iter (int): Number of iterations to run the k-means algorithm.
        n_local_trials (int or None): Number of seeding trials for centroids
            initialization.
        random_state (int | None): Determines random number generation for centroid
            initialization.
        affinity_transform (AffinityTransform): Affinity transform to apply to the
            affinity matrix.
        cluster_centers_ (list[NDArray[np.float32]] | None): Coordinates of cluster
            centers.
        eigvals_ (NDArray[np.float32 | np.float64] | None): The eigenvalues of the
            (normalized) laplacian matrix.
        ngap_ (float): The normalized eigengap.
    """

    n_clusters: int
    n_nodes: int | None
    p: float
    normed: bool
    n_iter: int
    n_local_trials: IntStrictlyPositive | None
    random_state: int | None
    cluster_centers_: list[np.ndarray] | None
    eigvals_: np.ndarray | None
    ngap_: float | None
    affinity_transform: AffinityTransform

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def __init__(
        self,
        n_clusters: IntStrictlyPositive,
        n_nodes: IntStrictlyPositive | None = None,
        *,
        p: NumStrictlyPositive = 2,
        normed: bool = True,
        n_iter: IntStrictlyPositive = 20,
        n_local_trials: IntStrictlyPositive | None = None,
        random_state: int | None = None,
        affinity_transform: AffinityTransform = DEFAULT_AFFINITY_TRANSFORM,
    ):
        """Initialize the Spectral Bridges model.

        Args:
            n_clusters  (IntStrictlyPositive): The number of clusters to form.
            n_nodes  (IntStrictlyPositive | None): Number of nodes or initial clusters.
            p (NumStrictlyPositive, optional): Power of the alpha_i. Defaults to 2.
            n_iter (int, optional): Number of iterations to run the k-means algorithm.
                Defaults to 20.
            normed (bool, optional): Whether to normalize the affinity matrix. Defaults
                to True.
            n_local_trials (int or None, optional): Number of seeding trials for
                centroids initialization.
            random_state (int or None, optional): Determines random number generation
                for centroid initialization.
            affinity_transform (AffinityTransform, optional): Affinity transform
                to apply to the affinity matrix. Defaults to DEFAULT_AFFINITY_TRANSFORM.
        """
        self.n_clusters = n_clusters
        self.n_nodes = n_nodes
        self.p = p
        self.normed = normed
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.random_state = random_state
        self.affinity_transform = affinity_transform
        self.cluster_centers_ = None
        self.eigvals_ = None
        self.ngap_ = None

        if self.n_nodes is not None and self.n_nodes <= self.n_clusters:
            raise ValueError(
                f"n_nodes must be greater than n_clusters, got {self.n_nodes} <= "
                "{self.n_clusters}"
            )

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def fit(self, X: Matrix) -> Self:
        """Fit the Spectral Bridges model on the input data X.

        Args:
            X : Matrix
                Input data to cluster.

        Raises:
            ValueError: If the number of samples is less than the number of clusters.
            ValueError: If n_nodes is not provided.

        Returns:
            Self: The fitted model.
        """
        if X.shape[0] < self.n_clusters:
            raise ValueError(
                f"n_samples={X.shape[0]} must be >= n_clusters={self.n_clusters}."
            )
        if self.n_nodes is None:
            raise ValueError("n_nodes must be provided")

        kmeans = KMeans(
            self.n_nodes,
            self.n_iter,
            self.n_local_trials,
            self.random_state,
        )
        kmeans.fit(X)
        centers = cast(np.ndarray, kmeans.cluster_centers_)

        affinity = np.empty((self.n_nodes, self.n_nodes))

        X_centered = [
            np.array(
                X[kmeans.labels_ == i] - cast(np.ndarray, kmeans.cluster_centers_)[i],
                dtype=np.float32,
                order="F",
            )
            for i in range(self.n_nodes)
        ]

        counts = np.array([X_centered[i].shape[0] for i in range(self.n_nodes)])
        counts = counts[None, :] + counts[:, None]

        for i in range(self.n_nodes):
            segments = np.asfortranarray(centers - centers[i])
            dists = np.einsum("ij,ij->i", segments, segments)
            dists[i] = 1

            projs = cast(np.ndarray, sgemm(1.0, X_centered[i], segments, trans_b=True))
            np.clip(projs / dists, 0, None, out=projs)
            projs = np.power(projs, self.p)

            affinity[i] = projs.sum(axis=0)

        affinity = np.power((affinity + affinity.T) / counts, 1 / self.p)

        affinity = self.affinity_transform(affinity)

        spectralclustering = SpectralClustering(
            self.normed,
            self.n_clusters,
            self.n_iter,
            self.n_local_trials,
            self.random_state,
        )
        spectralclustering.fit(affinity)

        self.eigvals_ = spectralclustering.eigvals_
        self.ngap_ = spectralclustering.ngap_
        self.cluster_centers_ = [
            centers[spectralclustering.labels_ == i] for i in range(self.n_clusters)
        ]

        return self

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def fit_select(
        self,
        X: np.ndarray,
        n_nodes_range: Iterable[int] | None = None,
        n_redo: IntStrictlyPositive = 10,
    ) -> dict[int, float]:
        """Selects and fits the best model from a range of possible node counts.

        It evaluates the mean normalized eigengap (ngap) for each candidate.

        For each `n_nodes` in `n_nodes_range`, multiple models are fit to the data,
        and the one with the highest mean normalized eigengap over `n_redo` runs
        is selected. The method then updates the current instance to use the
        attributes of the best candidate model.

        Args:
            X (np.ndarray): The input data.
            n_nodes_range (Iterable[int] | None): The range of possible node counts.
            n_redo (int): The number of times to run the model.

        Returns:
            dict[int, float]: The mean normalized eigengap for each node count.
        """
        if n_nodes_range is None:
            if self.n_nodes is None:
                raise ValueError("n_nodes_range or self.n_nodes must be provided")
            n_nodes_range = [self.n_nodes]

        rng = np.random.default_rng(self.random_state)
        max_int = np.iinfo(np.int32).max

        best_candidate = None
        best_mean_ngap = -1
        mean_ngaps: dict[int, float] = {}

        for n_nodes in n_nodes_range:
            candidate = None
            cum_ngap = 0

            for _ in range(n_redo):
                model = SpectralBridges(
                    n_clusters=self.n_clusters,
                    n_nodes=n_nodes,
                    p=self.p,
                    n_iter=self.n_iter,
                    n_local_trials=self.n_local_trials,
                    random_state=self.random_state,
                    affinity_transform=self.affinity_transform,
                )
                model.fit(X)

                cum_ngap += cast(float, model.ngap_)

                if candidate is None or cast(float, model.ngap_) > cast(
                    float, candidate.ngap_
                ):
                    candidate = model

                self.random_state = int(rng.integers(max_int + 1))

            mean_ngap = cum_ngap / n_redo
            mean_ngaps[n_nodes] = mean_ngap

            if mean_ngap > best_mean_ngap:
                best_candidate = candidate
                best_mean_ngap = mean_ngap

        self.__dict__.update(best_candidate.__dict__)

        return mean_ngaps

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def predict(self, x: Matrix) -> np.ndarray:
        """Predict the nearest cluster index for each input data point x.

        Args:
            x (Matrix): The input data.

        Raises:
            ValueError: If `x` contains inf or NaN values.
            ValueError: If `x` contains inf or NaN values.
            ValueError: If `self.cluster_centers_` is not set.

        Returns:
            np.ndarray The predicted cluster indices.
        """
        x_f32 = x.astype(np.float32)

        if np.isinf(x_f32).any():
            raise ValueError("x must not contain inf values")
        if np.isnan(x_f32).any():
            raise ValueError("x must not contain NaN values")
        if self.cluster_centers_ is None:
            raise ValueError("SpectralBridges must be fitted first")

        cluster_centers = np.vstack(self.cluster_centers_)
        cluster_cutoffs = np.cumsum(
            [cluster.shape[0] for cluster in self.cluster_centers_]
        )

        index = faiss.IndexFlatL2(x_f32.shape[1])
        index.add(cluster_centers)  # type: ignore
        winners = cast(np.ndarray, index.search(x_f32, 1)[1]).ravel()  # type: ignore

        return np.searchsorted(cluster_cutoffs, winners, side="right")

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def fit_predict(self, X: Matrix) -> np.ndarray:
        """Fits and predicts the nearest cluster index for each input data point X.

        Args:
            X (Matrix): The input data.

        Returns:
            np.ndarray: The predicted cluster indices.
        """
        return self.fit(X).predict(X)
