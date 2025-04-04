import numpy as np

np.random.seed(42)
array1 = np.random.randint(0, 21, size=(3, 3))
array2 = np.random.randint(0, 21, size=(3, 3))

matrix_sum = array1 + array2
matrix_product = np.matmul(array1, array2)
matrix_product_transpose = matrix_product.transpose()