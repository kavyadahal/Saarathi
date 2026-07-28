# Day 17 — Classwork

`pip install scikit-learn pandas`. Datasets are built into sklearn — no downloads.
**Always scale before k-means** — it measures distance.

## Exercise 1: Cluster the flowers (`kmeans_basic.py`) — ~15 min
1. Scale the iris features with `StandardScaler`.
2. Fit `KMeans(n_clusters=3, n_init=10, random_state=42)` and `fit_predict`.
3. Print `km.inertia_` and the cluster sizes; cross-tab clusters vs true species.

**Expected:** inertia ≈ 139.8, sizes 53 / 50 / 47. One cluster **is** setosa exactly (50);
versicolor & virginica overlap, so the other two clusters mix them a little.

**Stretch:** run it once *without* scaling — do the clusters get worse?

## Exercise 2: The elbow (`elbow.py`) — ~10 min
Loop k = 1..10, print `km.inertia_` and the drop from the previous k.

**Expected (scaled):** 600 → 222.4 → 139.8 → 114.1 … The big drops stop after k=3 —
the elbow is around **k=3**.

## Exercise 3: The silhouette (`silhouette.py`) — ~10 min
Loop k = 2..6, print `silhouette_score`.

**Expected:** k=2 → 0.582 (highest), k=3 → 0.460, k=4 → 0.387.

**The twist:** the silhouette likes **k=2** (setosa vs the rest) but the elbow likes **k=3**
(the three species). Both are defensible — write one sentence on which k you'd pick and why.

---

## Key idea
k-means = assign → move → repeat, minimising **inertia**. It can't count the groups for you, so
use the **elbow** and **silhouette** to choose k — and when they disagree, your judgement decides.

---

## Homework (from slides, before Day 18)
- Cluster `load_wine` (13 features). Run the elbow & silhouette — how many groups?
- Repeat iris **without** scaling. How do the clusters and inertia change?
- Read `formulas.md` in the Drive course folder — inertia, distance, silhouette, first principles.
- Commit: `git add . && git commit -m "day 17"`.
