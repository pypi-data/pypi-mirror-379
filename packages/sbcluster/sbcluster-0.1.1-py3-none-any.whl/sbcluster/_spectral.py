from typing import cast

import numpy as np
from numpy.typing import NDArray
from scipy.sparse.csgraph import laplacian  # type: ignore

from ._kmeans import KMeans


class SpectralClustering:
    """Spectral clustering based on Laplacian matrix.

    Attributes:
        n_local_trials  (int | None): The number of seeding trials for
            centroids initialization.
        random_state (int | None) Determines random number generation for
            centroid initialization.
        labels_ (NDArray[np.int32] | None): Labels of each point (index) in the affinity
            matrix.
        eigvals_ (NDArray[np.float32 | np.float64] | None): The eigenvalues of the
            (normalized) laplacian matrix.
        ngap_ (float): The normalized eigengap.
    """

    n_iter: int
    n_local_trials: int | None
    random_state: int | None
    labels_: NDArray[np.int32] | None
    eigvals_: NDArray[np.float32 | np.float64] | None
    ngap_: float | None

    def __init__(
        self,
        n_clusters: int,
        n_iter: int,
        n_local_trials: int | None,
        random_state: int | None,
    ):
        """Initializes the class.

        Args:
            n_clusters (int): The number of clusters to form.
            n_iter (int): The number of iterations to run the k-means
                algorithm.
            n_local_trials  (int | None): The number of seeding trials for
                centroids initialization.
            random_state (int | None) Determines random number generation for
                centroid initialization.
            random_state (int | None): Determines random number generation for centroid
                initialization.
        """
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.labels_ = None
        self.eigvals_ = None
        self.ngap_ = None

    def fit(self, affinity: NDArray[np.float32 | np.float64]):
        """Fit the spectral clustering model on the affinity matrix.

        Parameters:
        -----------
        affinity (NDArray[np.float32]): Affinity matrix representing pairwise similarity
            between points.
        """
        L = cast(NDArray[np.float32 | np.float64], laplacian(affinity, normed=True))

        self.eigvals_, eigvecs = cast(
            tuple[NDArray[np.float32 | np.float64], ...],
            np.linalg.eigh(L),  # type: ignore
        )
        eigvecs = eigvecs[:, : self.n_clusters]
        eigvecs /= np.linalg.norm(eigvecs, axis=1)[:, None]
        kmeans = KMeans(
            self.n_clusters, self.n_iter, self.n_local_trials, self.random_state
        )
        kmeans.fit(eigvecs)

        self.ngap_ = (
            self.eigvals_[self.n_clusters] - self.eigvals_[self.n_clusters - 1]
        ) / self.eigvals_[self.n_clusters - 1]
        self.labels_ = kmeans.labels_
