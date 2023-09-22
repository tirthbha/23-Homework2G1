#Importing some necessary liberaries for the code.
import numpy as np
import time
# Create random matrices of 100*100 dimentions. 
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)
# Method 1: Manual matrix multiplication using nested loops
def matrix_multiply_manual(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C

# Method 2: NumPy's built-in matrix multiplication
def np_matrix_multiply(A, B):
    return np.dot(A, B)

# Method 3: Matrix multiplication using Einstein notation
def matrix_multiply_einsum(A, B):
    return np.einsum('ij,jk->ik', A, B)

# Measure execution time for each method
start_time = time.time()
C1 = matrix_multiply_manual(A, B)
end_time = time.time()
print(f"Method 1 (Manual) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C2 = np_matrix_multiply(A, B)
end_time = time.time()
print(f"Method 2 (NumPy) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C3 = matrix_multiply_einsum(A, B)
end_time = time.time()
print(f"Method 3 (Einstein Notation) Execution Time: {end_time - start_time} seconds")
