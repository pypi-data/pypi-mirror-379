import numpy as np
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsClassifier

from thesis.AdaptiveLearning import AdaptiveLearning

class KNN(AdaptiveLearning):
    def __init__(self, X):
        super().__init__()

        self.X_train = None
        self.X = X
        _, self.kstars = super().return_ids_kstar_binomial(X=self.X, n_iter=10, Dthr=6.7, initial_id=None, r='opt', verbose=False)
        # mean_kstar = int(np.round(np.min(kstar)))
        mean_kstar = int(np.round(np.min(self.kstars)))
        if mean_kstar == 0: mean_kstar = 1  # Ensure k is at least 1

        # Create a KNN classifier.  n_neighbors is the 'k' in k-nearest neighbors.
        self.knn_model = KNeighborsClassifier(n_neighbors=mean_kstar, metric='precomputed')


    def fit(self, X_train, y_train):
        self.X_train = X_train
        D_train = self.create_distance_matrix(X=self.X_train)

        # Train the classifier on the training data
        self.knn_model.fit(D_train, y_train)


    def predict(self, X_test):
        D_test = self.create_precomputed_distance_matrix(X_test, self.X_train)

        # Make predictions on the test data
        return self.knn_model.predict(D_test)

    def create_distance_matrix(self, X, y=None):
        """
        Create distance matrix based on K* neighbors.

        Args:
            X: Input data matrix.
        Returns:
            A symmetric distance matrix where entry (i, j) is the Euclidean distance between X[i] and X[j]
            if j is in the K* neighbors of i, and 0 otherwise.
        """
        n_samples = X.shape[0]
        distance_matrix = np.zeros((n_samples, n_samples))

        neighs_ind = super().find_Kstar_neighs(X, self.kstars)

        for i in range(n_samples):
            for j_index, neighbor_index in enumerate(neighs_ind[i]):
                dist = distance.euclidean(X[i], X[neighbor_index])
                distance_matrix[i, neighbor_index] = dist

        # Make the matrix symmetric
        distance_matrix = 0.5 * (distance_matrix + distance_matrix.T)
        return distance_matrix

    def create_precomputed_distance_matrix(self, X_test, X_train, k_neighbors=None):
        """
        Create a distance matrix for KNN with a 'precomputed' metric,
        calculating distances between X_test and X_train.

        Optionally, applies a K-neighbor constraint by setting distances
        to non-K-neighbors to 0 for each X_test sample.

        Args:
            X_test (np.ndarray): Input test data matrix (n_test_samples, n_features).
            X_train (np.ndarray): Input training data matrix (n_train_samples, n_features).
            k_neighbors (int, optional): If provided, for each sample in X_test,
                                         only the distances to its k_neighbors nearest
                                         neighbors in X_train will be kept. Other
                                         distances in that row will be set to 0.
                                         If None, the full pairwise distance matrix is returned.

        Returns:
            np.ndarray: A distance matrix of shape (n_test_samples, n_train_samples).
                        Entry (i, j) is the Euclidean distance between X_test[i] and X_train[j].
                        If k_neighbors is specified, distances to non-k_neighbors are 0.
        """
        n_test_samples = X_test.shape[0]
        n_train_samples = X_train.shape[0]

        # Calculate the full pairwise Euclidean distance matrix
        # cdist(XA, XB) computes the distance between each pair of the two collections of inputs.
        # The output is a matrix of shape (len(XA), len(XB)).
        # For 'euclidean' metric, this is sqrt(sum((u-v)^2)).
        distance_matrix = distance.cdist(X_test, X_train, 'euclidean')

        # Apply the K-neighbor constraint if specified
        if k_neighbors is not None:
            if not isinstance(k_neighbors, int) or k_neighbors <= 0:
                raise ValueError("k_neighbors must be a positive integer or None.")
            if k_neighbors > n_train_samples:
                print(
                    f"Warning: k_neighbors ({k_neighbors}) is greater than the number of training samples ({n_train_samples}). All distances will be kept.")
                # No need to zero out, as all will be considered 'neighbors'

            constrained_distance_matrix = np.zeros_like(distance_matrix)
            for i in range(n_test_samples):
                # Get the indices that would sort the distances for the current X_test sample
                # argsort returns the indices that would sort an array.
                sorted_indices = np.argsort(distance_matrix[i, :])

                # Select the indices of the k_neighbors smallest distances
                # We take the first k_neighbors indices as they correspond to the smallest distances
                k_nearest_indices = sorted_indices[:k_neighbors]

                # Copy the distances for these k_nearest_neighbors
                constrained_distance_matrix[i, k_nearest_indices] = distance_matrix[i, k_nearest_indices]

            distance_matrix = constrained_distance_matrix

        return distance_matrix