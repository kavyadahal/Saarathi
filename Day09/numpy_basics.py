import numpy as np

#Week 1 way:

b = [n*2 for n in [1,2,4]]
print(b)

#numpy way:
a = np.array([1,2,3])
print(a**2)

print(
a.shape,"\n",
a.mean(),"\n",
a.sum(),"\n",
a[a<20]
)
