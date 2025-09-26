import numpy as np
from scipy.sparse.csgraph import shortest_path
from sklearn.manifold import MDS
from sklearn.neighbors import kneighbors_graph

from thesis.AdaptiveLearning import AdaptiveLearning

class IsomapA(AdaptiveLearning):
    def __init__(self, X, n_iter=10, Dthr=6.67, r='opt', verbose=False):
        super().__init__()
        self.verbose = verbose

        # --- "Adaptive IsoMap" (Implementazione Manuale) ---
        if self.verbose:
            print("\n--- Esecuzione di 'Adaptive IsoMap' ---")
        self.X = X

        # 1 Calcola i valori di k* per ogni punto
        self.ids, self.kstars = super().return_ids_kstar_binomial(X=self.X, n_iter=n_iter, Dthr=Dthr, r=r)
        self.n_components = super().find_components(ids=self.ids, n_iter=n_iter)
        max_k = np.max(self.kstars)
        if self.verbose:
            print(f"Il k* massimo calcolato è: {max_k}")

        # 2 Costruzione del Grafo di Vicinato Adattivo
        if self.verbose:
            print("Costruzione del grafo di vicinato adattivo...")
        # Calcola un grafo iniziale con k_max per efficienza
        initial_graph = kneighbors_graph(self.X, n_neighbors=max_k, mode='distance')
        # Potatura del grafo basata sui valori k_i*
        adjacency_lil = initial_graph.tolil()
        for i in range(self.X.shape[0]):
            k_i = self.kstars[i]
            neighbors_indices = initial_graph[i].indices
            if len(neighbors_indices) > k_i:
                indices_to_remove = neighbors_indices[k_i:]
                adjacency_lil[i, indices_to_remove] = 0

        # Assicura che il grafo sia simmetrico (non orientato)
        adjacency_csr = adjacency_lil.tocsr()
        adjacency_symmetric = np.maximum(adjacency_csr.toarray(), adjacency_csr.toarray().T)

        # 3 Calcolo delle Distanze Geodetiche
        if self.verbose:
            print("Calcolo delle distanze geodetiche (cammini minimi)...")
        self.geodesic_distances = shortest_path(csgraph=adjacency_symmetric, directed=False)

        # Gestione di eventuali componenti disconnesse
        if np.any(np.isinf(self.geodesic_distances)):
            print("ATTENZIONE: Il grafo non è completamente connesso.")
            max_dist = np.max(self.geodesic_distances[~np.isinf(self.geodesic_distances)])
            self.geodesic_distances[np.isinf(self.geodesic_distances)] = max_dist * 1.5

    def fit(self):
        # 4 Applicazione di MDS
        if self.verbose:
            print("Applicazione di MDS per ottenere l'embedding finale...")
        mds = MDS(n_components=self.n_components, dissimilarity='precomputed', normalized_stress=False)
        embedding_adaptive = mds.fit_transform(self.geodesic_distances)

        if self.verbose:
            print("Embedding adattivo calcolato.")
        return embedding_adaptive

