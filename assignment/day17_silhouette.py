"""
Day 17 · Exercise 3 — Choosing k with the silhouette score
A second opinion on k. Silhouette scores each point from -1 to +1:
+1 = snug in its cluster, 0 = on the border, -1 = probably in the wrong one.
We average it over all points; the k with the HIGHEST average wins.
Run with: python silhouette.py
Needs: pip install scikit-learn
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = load_iris(as_frame=True).data
X_scaled = StandardScaler().fit_transform(X)

print("k silhouette")
for k in range(2, 7):  # silhouette needs at least 2 clusters
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = km.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)
    print(f"{k:<3} {score:.3f}")

print("\nHighest score = the cleanest grouping. Compare it with the elbow's answer.")
