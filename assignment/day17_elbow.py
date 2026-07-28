"""
Day 17 · Exercise 2 — Choosing k with the elbow method
k-means can't tell you HOW MANY groups exist - you pick k.
Trick: plot inertia (tightness) for k = 1..10. It always falls, but the
"elbow" where it stops falling fast is a good k.
Run with: python elbow.py
Needs: pip install scikit-learn
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X = load_iris(as_frame=True).data
X_scaled = StandardScaler().fit_transform(X)

print("k inertia drop-from-previous")
prev = None
for k in range(1, 11):
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_scaled)
    drop = "" if prev is None else f"{prev - km.inertia_:6.1f}"
    print(f"{k:<3} {km.inertia_:7.1f} {drop}")
    prev = km.inertia_

print("\nLook for the k where the drop suddenly gets small - that's the elbow.")
