import numpy as np
from scipy.spatial import distance
from sklearn.semi_supervised import LabelPropagation as lp

from thesis.AdaptiveLearning import AdaptiveLearning

class LabelPropagation(AdaptiveLearning):
    def __init__(self, X):
        super().__init__()

        self.X = X
        self.ids, self.kstars = super().return_ids_kstar_binomial(X=X, n_iter=10, Dthr=6.7, initial_id=None, r='opt', verbose=False)
        self.n_components = super().find_components(ids=self.ids, n_iter=10)

        self.label_propagation_model = lp(kernel=self.create_similarity_matrix, n_neighbors=self.n_components)

    def create_similarity_matrix(self, X, y=None):
        """
        Create similarity matrix based on K* neighbors.

        Args:
            X: Input data matrix.
        """
        use_distances = True
        sigma = 1.0

        n_samples = X.shape[0]
        similarity_matrix = np.zeros((n_samples, n_samples))

        neighs_ind = super().find_Kstar_neighs(X, self.kstars)

        if use_distances:
            for i in range(n_samples):
                for j_index, neighbor_index in enumerate(neighs_ind[i]):
                    dist = distance.euclidean(X[i], X[neighbor_index])
                    # Convert distance to similarity using a Gaussian-like kernel
                    similarity = np.exp(-dist ** 2 / (2 * sigma ** 2))
                    similarity_matrix[i, neighbor_index] = similarity
        else:
            for i in range(n_samples):
                similarity_matrix[i, neighs_ind[i]] = 1.0

        similarity_matrix = 0.5 * (similarity_matrix + similarity_matrix.T)
        return similarity_matrix

    def fit(self, y):
        return self.label_propagation_model.fit(self.X, y)

    def predict(self):
        return self.label_propagation_model.predict(self.X)