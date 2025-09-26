import numpy as np
from sklearn.cluster import DBSCAN as dbscan
from sklearn.neighbors import NearestNeighbors

from thesis.AdaptiveLearning import AdaptiveLearning

class DBSCAN(AdaptiveLearning):
    def __init__(self, X, n_iter, Dthr, r='opt', verbose=False):
        super().__init__()

        self.X = X
        self.ids, self.kstars = super().return_ids_kstar_binomial(X=X, n_iter=n_iter, Dthr=Dthr, r=r, verbose=verbose)

        # Calculate min_samples and eps parameters
        self.min_samples = np.maximum(2, np.round(self.kstars / 2)).astype(int)
        self.eps_values = self.compute_adaptive_eps(self.min_samples)

        self.dbscan_model = dbscan(eps=np.median(self.eps_values), min_samples=int(np.median(self.min_samples)))

    def compute_adaptive_eps(self, min_neighbors=5):
        kstars = np.clip(self.kstars, min_neighbors, self.X.shape[0] - 1)
        nn = NearestNeighbors(n_jobs=-1)
        nn.fit(self.X)
        eps_values = np.zeros(self.X.shape[0])

        for i in range(self.X.shape[0]):
            distances, _ = nn.kneighbors([self.X[i]], n_neighbors=kstars[i] + 1)
            eps_values[i] = np.mean(distances[0][1:])

        return eps_values

    def fit_predict(self):
        return self.dbscan_model.fit_predict(self.X)