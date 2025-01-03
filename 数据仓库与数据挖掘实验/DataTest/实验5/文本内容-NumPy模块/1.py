import numpy as np
n1 = np.arange(10)
print(n1)
print(np.where(n1 > 5, 2, 0))
n2 = n1[np.where(n1 > 5)]
print(n2)