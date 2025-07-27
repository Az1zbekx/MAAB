import numpy as np

# 1. Vector with values from 10 to 49
vector_10_49 = np.arange(10, 50)

# 2. 3x3 matrix with values from 0 to 8
matrix_0_8 = np.arange(9).reshape(3, 3)

# 3. 3x3 identity matrix
identity_3x3 = np.eye(3)

# 4. 3x3x3 array with random values
random_3x3x3 = np.random.random((3, 3, 3))

# 5. 10x10 array with random values, find min and max
random_10x10 = np.random.random((10, 10))
min_val = random_10x10.min()
max_val = random_10x10.max()

# 6. Random vector of size 30, find mean value
random_vec_30 = np.random.random(30)
mean_val = random_vec_30.mean()

# 7. Normalize a 5x5 random matrix
random_5x5 = np.random.random((5, 5))
norm_5x5 = (random_5x5 - np.min(random_5x5)) / (np.max(random_5x5) - np.min(random_5x5))

# 8. Multiply 5x3 by 3x2 (real matrix product)
mat_5x3 = np.random.random((5, 3))
mat_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(mat_5x3, mat_3x2)

# 9. Two 3x3 matrices, compute their dot product
A = np.random.random((3, 3))
B = np.random.random((3, 3))
dot_product = np.dot(A, B)

# 10. Transpose of 4x4 matrix
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T

# 11. 3x3 matrix, calculate determinant
matrix_3x3 = np.random.random((3, 3))
det = np.linalg.det(matrix_3x3)

# 12. A (3x4) and B (4x3), compute A·B
A_3x4 = np.random.random((3, 4))
B_4x3 = np.random.random((4, 3))
product_AB = np.dot(A_3x4, B_4x3)

# 13. 3x3 matrix and 3-element column vector, matrix-vector product
matrix3 = np.random.random((3, 3))
vector3 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix3, vector3)

# 14. Solve Ax = b for 3x3 A and 3x1 b
A_lin = np.random.random((3, 3))
b_lin = np.random.random((3, 1))
x = np.linalg.solve(A_lin, b_lin)

# 15. Row-wise and column-wise sums of 5x5 matrix
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
