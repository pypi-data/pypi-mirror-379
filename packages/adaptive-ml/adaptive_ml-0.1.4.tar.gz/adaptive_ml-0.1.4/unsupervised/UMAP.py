import numpy as np
import umap
from umap.umap_ import nearest_neighbors

from thesis.AdaptiveLearning import AdaptiveLearning


class UMAPA(AdaptiveLearning):
    def __init__(self, X, n_iter=10, Dthr=6.67, r='opt', verbose=False):
        super().__init__()

        self.X = X
        self.verbose = verbose
        self.n_iter = n_iter
        self.Dthr = Dthr
        self.r = r

    def fit(self):
        # --- UMAP Adattivo ---
        if self.verbose:
            print("\n--- Begin Adaptive UMAP ---")

        # Step 1: Calculate k* values for each point
        ids, self.kstars = super().return_ids_kstar_binomial(X=self.X, n_iter=self.n_iter, Dthr=self.Dthr, r=self.r)
        max_k = np.max(self.kstars)

        if self.verbose:
            print(f"Computed k* max is: {max_k}")

        n_components = super().find_components(ids=ids, n_iter=self.n_iter)

        if self.verbose:
            print(f"Number of components found: {n_components}")

        # Step 2: Compute the initial nearest neighbors graph up to max_k
        if self.verbose:
            print("Computing initial neighbors graph (k_max)...")

        # This function returns the indices and distances of the neighbors
        knn_indices, knn_dists, _ = nearest_neighbors(
            X=self.X,
            n_neighbors=max_k,
            metric='euclidean',
            metric_kwds={},
            angular=False,
            random_state=0
        )

        # Step 3: Modify the graph by pruning connections
        if self.verbose:
            print("Adapting neighbors graph using k* values...")

        for i in range(self.X.shape[0]):
            k_i = self.kstars[i]
            # Set indices for neighbors beyond k_i to -1 (indicating no connection)
            knn_indices[i, k_i:] = -1
            # Set corresponding distances to 0
            knn_dists[i, k_i:] = 0

        # Step 4: Initialize a new UMAP instance using the precomputed (and now adapted) graph
        if self.verbose:
            print("Generating Adaptive UMAP embedding...")

        reducer_adaptive = umap.UMAP(
            n_components=n_components,
            precomputed_knn=(knn_indices, knn_dists)
        )

        # Step 5: Generate the final embedding from the adapted graph
        embedding_adaptive = reducer_adaptive.fit_transform(self.X)

        if self.verbose:
            print("Adaptive embedding done.")

        return embedding_adaptive