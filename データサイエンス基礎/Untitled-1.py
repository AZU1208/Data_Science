import numpy as np
a = np.full((2, 3), np.pi).T.ravel()
b = np.linspace(0, 1, 5)
c = np.hstack([a, b])
print(a)
print(b)
print(c)