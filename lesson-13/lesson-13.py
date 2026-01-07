import numpy as np

# 1. Vector with values from 10 to 49
vector_10_49 = np.arange(10, 50)
print("1. Vector (10 to 49):\n", vector_10_49)

# 2. 3x3 matrix with values from 0 to 8
matrix_0_8 = np.arange(9).reshape(3, 3)
print("\n2. 3x3 matrix (0 to 8):\n", matrix_0_8)

# 3. 3x3 identity matrix
identity_matrix = np.eye(3)
print("\n3. 3x3 Identity Matrix:\n", identity_matrix)

# 4. 3x3x3 array with random values
array_3x3x3 = np.random.random((3, 3, 3))
print("\n4. 3x3x3 Array with Random Values:\n", array_3x3x3)

# 5. 10x10 array with random values and min/max
array_10x10 = np.random.random((10, 10))
print("\n5. 10x10 Array with Random Values:\n", array_10x10)
print("Min:", array_10x10.min(), "Max:", array_10x10.max())

# 6. Random vector of size 30 and mean value
random_vector_30 = np.random.random(30)
print("\n6. Random Vector Size 30:\n", random_vector_30)
print("Mean:", random_vector_30.mean())

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.random((5, 5))
normalized_matrix_5x5 = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())
print("\n7. Normalized 5x5 Matrix:\n", normalized_matrix_5x5)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)
print("\n8. 5x3 * 3x2 Product:\n", product_5x2)

# 9. Dot product of two 3x3 matrices
matrix1_3x3 = np.random.random((3, 3))
matrix2_3x3 = np.random.random((3, 3))
dot_product_3x3 = np.dot(matrix1_3x3, matrix2_3x3)
print("\n9. Dot Product of Two 3x3 Matrices:\n", dot_product_3x3)

# 10. Transpose of a 4x4 matrix
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T
print("\n10. Transpose of 4x4 Matrix:\n", transpose_4x4)

# 11. Determinant of a 3x3 matrix
matrix_det_3x3 = np.random.random((3, 3))
det_value = np.linalg.det(matrix_det_3x3)
print("\n11. Determinant of 3x3 Matrix:\n", matrix_det_3x3)
print("Determinant:", det_value)

# 12. Product of A (3x4) and B (4x3)
A_3x4 = np.random.random((3, 4))
B_4x3 = np.random.random((4, 3))
product_AB = np.dot(A_3x4, B_4x3)
print("\n12. Product of A (3x4) and B (4x3):\n", product_AB)

# 13. Matrix-vector product (3x3 matrix and 3x1 vector)
matrix_mv_3x3 = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_mv_3x3, vector_3x1)
print("\n13. Matrix-Vector Product:\n", matrix_vector_product)

# 14. Solve Ax = b
A_solve = np.random.rand(3, 3)
b_solve = np.random.rand(3, 1)
x_solution = np.linalg.solve(A_solve, b_solve)
print("\n14. Solution to Ax = b:")
print("A:\n", A_solve)
print("b:\n", b_solve)
print("x:\n", x_solution)

# 15. Row-wise and column-wise sums of 5x5 matrix
matrix_5x5_sum = np.random.random((5, 5))
row_sums = matrix_5x5_sum.sum(axis=1)
col_sums = matrix_5x5_sum.sum(axis=0)
print("\n15. 5x5 Matrix Row-wise and Column-wise Sums:")
print("Matrix:\n", matrix_5x5_sum)
print("Row-wise sums:", row_sums)
print("Column-wise sums:", col_sums)
