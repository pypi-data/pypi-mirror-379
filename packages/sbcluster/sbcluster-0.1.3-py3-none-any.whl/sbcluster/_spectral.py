from typing import cast

import numpy as np
from scipy.sparse.csgraph import laplacian  # type: ignore

from ._kmeans import KMeans


class SpectralClustering:
    """Spectral clustering based on Laplacian matrix.

    Attributes:
        normed (bool): Whether to normalize the affinity matrix.
        n_clusters (int): The number of clusters to form.
        n_iter (int): The number of iterations to run the k-means algorithm.
        n_local_trials (int | None): The number of seeding trials for
            centroids initialization.
        random_state (int | None) Determines random number generation for
            centroid initialization.
        labels_ (np.ndarray | None): Labels of each point (index) in the affinity
            matrix.
        eigvals_ (np.ndarray | None): The eigenvalues of the
            (normalized) laplacian matrix.
        ngap_ (float): The normalized eigengap.
    """

    normed: bool
    n_clusters: int
    n_iter: int
    n_local_trials: int | None
    random_state: int | None
    labels_: np.ndarray | None
    eigvals_: np.ndarray | None
    ngap_: float | None

    def __init__(
        self,
        normed: bool,
        n_clusters: int,
        n_iter: int,
        n_local_trials: int | None,
        random_state: int | None,
    ):
        """Initializes the class.

        Args:
            normed (bool): Whether to normalize the affinity matrix.
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
        self.normed = normed
        self.n_clusters = n_clusters
        self.n_iter = n_iter
        self.n_local_trials = n_local_trials
        self.random_state = random_state
        self.labels_ = None
        self.eigvals_ = None
        self.ngap_ = None

    def fit(self, affinity: np.ndarray):
        """Fit the spectral clustering model on the affinity matrix.

        Parameters:
        -----------
        affinity (np.ndarray): Affinity matrix representing pairwise similarity
            between points.
        """
        L = cast(np.ndarray, laplacian(affinity, normed=True))

        self.eigvals_, eigvecs = cast(
            tuple[np.ndarray, ...],
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
