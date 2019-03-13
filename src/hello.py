import numpy as np

x = np.array(range(10))
y = np.array([float(i) ** 2 for i in x])
y *= 1.02
print(y)
