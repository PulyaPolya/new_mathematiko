import numpy as np
from matrix import Matrix
from settings import Settings

g_settings = Settings()
m = Matrix(g_settings)

A = [[4, 2, 8, 8, 13], [10, 2, 7, 7, 10], [4, 11, 3, 6, 11], [5, 12, 6, 5, 12], [1, 3, 9, 9, 1]]
A = np.array(A)
m.matrix = A

print(m.count_points())


