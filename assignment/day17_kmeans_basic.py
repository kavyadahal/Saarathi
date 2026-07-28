"""
Day 17 · Exercise 1 — k-means clustering
UNSUPERVISED: no labels. k-means finds k groups by itself.
Algorithm: put down k centres -> assign each point to nearest -> move each
centre to its points' average -> repeat until nothing moves.
Run with: python kmeans_basic.py
Needs: pip install scikit-learn
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd

data = load_iris(as_frame=True)
X = data.data  # 4 features, NO labels used for training
species = data.target  # kept ONLY to check our clusters afterwards

# ALWAYS scale before k-means - it measures distance (like Week 3's models)
X_scaled = StandardScaler().fit_transform(X)

# n_clusters = how many groups we ask for; n_init = restarts to avoid bad luck
km = KMeans(n_clusters=3, n_init=10, random_state=42)
labels = km.fit_predict(X_scaled)  # each row gets a cluster number 0/1/2

print(f"Inertia (total within-cluster distance): {km.inertia_:.1f}")
print("\nCluster sizes:")
print(pd.Series(labels).value_counts().sort_index().to_string())

# Did the clusters match the real species? (we never told k-means the answer)
print("\nClusters vs true species (rows = cluster, cols = species):")
print(pd.crosstab(labels, species))
