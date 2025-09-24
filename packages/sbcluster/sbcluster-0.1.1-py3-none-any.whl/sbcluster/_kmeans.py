from typing import cast

import faiss  # type: ignore
import numpy as np
from numpy.typing import NDArray
from pydantic import ConfigDict, validate_call
from scipy.linalg.blas import sgemm  # type: ignore


class KMeans:
    """K-means clustering using FAISS.

    Attributes:
        cluster_centers_  (NDArray[np.float32] | None): Coordinates of cluster centers.
        labels_ (NDArray[np.int32] | None): Labels of each point (index) in X.

    Methods:
    --------
    fit(X):
        Run k-means clustering on the input data X.
    """

    cluster_centers_: NDArray[np.float32] | None
    labels_: NDArray[np.int32] | None

    def __init__(
        self,
        n_clusters: int,
        n_iter: int,
        n_local_trials: int | None,
        random_state: int | None,
    ):
        """Initializes the KMeans class.

        Args:
            n_clusters (int): The number of clusters to form.
            n_iter (int): The number of iterations to run the k-means
                algorithm.
            n_local_trials  (int | None): The number of seeding trials for
                centroids initialization.
            random_state (int | None) Determines random number generation for
                centroid initialization.
        """
        self.n_clusters = n_clusters
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.random_state = random_state
        self.cluster_centers_ = None
        self.labels_ = None

    @staticmethod
    def _dists(
        X: NDArray[np.float32], y: NDArray[np.float32], XX: NDArray[np.float32]
    ) -> NDArray[np.float32]:
        """Computes the pairwise distances between a fixed data matrix and some points.

        Args:
            X (NDArray[np.float32]): The fixed data matrix.
            y (NDArray[np.float32]): The non fixed points.
            XX (NDArray[np.float32]): The fixed matrix squared norm.

        Returns:
            NDArray[np.float32]: The computed pairwise distances.
        """
        yy = np.einsum("ij,ij->i", y, y)
        dists = XX - sgemm(2.0, X, y, trans_b=True) + yy
        np.clip(dists, 0, None, out=dists)
        return dists

    def _init_centroids(self, X: NDArray[np.float32]) -> NDArray[np.float32]:
        """Initializes the centroids in a K-means++ fashion.

        Args:
            X (NDArray[np.float32]): The fixed data matrix.

        Returns:
            NDArray[np.float32]: The initialized centroids.
        """
        rng = np.random.default_rng(self.random_state)

        centroids = np.empty((self.n_clusters, X.shape[1]), dtype=X.dtype)
        centroids[0] = X[rng.integers(X.shape[0])]

        XX = np.einsum("ij,ij->i", X, X)[:, None]

        dists = self._dists(X, centroids[0:1], XX).ravel()
        inertia = dists.sum()

        if self.n_local_trials is None:
            self.n_local_trials = 2 + int(np.log(self.n_clusters))

        for i in range(1, self.n_clusters):
            candidate_ids = rng.choice(
                X.shape[0], size=self.n_local_trials, p=dists / inertia
            )
            candidates = np.asfortranarray(X[candidate_ids])

            current_candidates_dists = self._dists(X, candidates, XX)
            candidates_dists = np.minimum(current_candidates_dists, dists[:, None])

            inertias = candidates_dists.sum(axis=0)
            best_inertia = inertias.argmin()
            best_candidate = candidate_ids[best_inertia]
            dists = candidates_dists[:, best_inertia]
            inertia = inertias[best_inertia]

            centroids[i] = X[best_candidate]

        return centroids

    @staticmethod
    def _validate_X(X: NDArray[np.float32 | np.float64]) -> NDArray[np.float32]:
        """Validates and converts the data matrix.

        Args:
            X (NDArray[np.float32  |  np.float64]): The fixed data matrix.

        Raises:
            ValueError: If `X``contains inf values.
            ValueError: If `X``contains NaN values.

        Returns:
            NDArray[np.float32]: The validated and converted data matrix.
        """
        if np.isinf(X).any():
            raise ValueError("X must not contain inf values")
        if np.isnan(X).any():
            raise ValueError("X must not contain NaN values")

        return np.array(X, dtype=np.float32, order="F")

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True))
    def fit(self, X: np.ndarray):
        """Run k-means clustering on the input data X.

        Args:
            X (np.ndarray): Input data matrix to cluster.
        """
        X_f32 = self._validate_X(X)

        index = faiss.IndexFlatL2(X.shape[1])
        kmeans = faiss.Clustering(X.shape[1], self.n_clusters)

        init_centroids = self._init_centroids(X_f32)

        kmeans.centroids.resize(init_centroids.size)
        faiss.copy_array_to_vector(init_centroids.ravel(), kmeans.centroids)  # type: ignore
        kmeans.niter = self.n_iter
        kmeans.min_points_per_centroid = 0
        kmeans.max_points_per_centroid = -1
        kmeans.train(X_f32, index)  # type: ignore

        self.cluster_centers_ = cast(
            NDArray[np.float32],
            faiss.vector_to_array(kmeans.centroids).reshape(  # type: ignore
                self.n_clusters, X.shape[1]
            ),
        )
        self.labels_ = cast(NDArray[np.int32], index.search(X_f32, 1)[1].ravel())  # type: ignore
