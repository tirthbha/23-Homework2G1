import numpy as np
import time

# Define two matrices (they can have different dimensions)
matrix1 = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
matrix2 = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

# Method 1: Using NumPy's np.sum
start_time = time.time()
dot_product_np_sum = np.sum(matrix1 * matrix2)
end_time = time.time()

assert dot_product_np_sum == 49093067, "first method doesn't return correct dot product"

print(f"Dot Product using np.sum: {dot_product_np_sum}")
print(f"Execution time using np.sum: {end_time - start_time} seconds")

# Method 2: Using a nested loop
def dot_product_loop(matrix1, matrix2):
    """
    Calculate the dot product of two matrices using a nested loop.

    Args:
        matrix1 (numpy.ndarray): The first matrix.
        matrix2 (numpy.ndarray): The second matrix.

    Returns:
        float: The dot product of the two matrices.
    """
    result = 0
    for i in range(matrix1.shape[0]):
        for j in range(matrix1.shape[1]):
            result += matrix1[i, j] * matrix2[i, j]
    return result
    
    assert result == 49093067, "second method doesn't return correct dot product"

start_time = time.time()
dot_product_loop_result = dot_product_loop(matrix1, matrix2)
end_time = time.time()
print(f"Dot Product using a loop: {dot_product_loop_result}")
print(f"Execution time using a loop: {end_time - start_time} seconds")

# Method 3: Using NumPy's np.einsum
start_time = time.time()
dot_product_einsum = np.einsum('ij,ij->', matrix1, matrix2)

assert dot_product_einsum == 49093067, "third method doesn't return correct dot product"

end_time = time.time()
print(f"Dot Product using np.einsum: {dot_product_einsum}")
print(f"Execution time using np.einsum: {end_time - start_time} seconds")
