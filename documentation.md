# Matrix Multiplication and Dot Product



We compared the execution time of different implementations of matrix operations and used Matrix Multiplication and Dot Product operations. We compared the execution time of different implementations for matrix multiplication and dot product operations in Python. We explored three methods:

1. **Using For Loops**
2. **Using NumPy Built-in Functions**
3. **Using NumPy Einstein Notation Function**

## Prerequisites
- Python (3) (IBM Quantum Lab)
- NumPy library

# Matrix Multiplication

  ### 1. Using Nested Loops
For loop-based matrix multiplication is a straightforward method, but it may not be as efficient as numpy's built-in functions. Here's how have implemented it:


![Screenshot from 2023-09-25 20-20-46](https://github.com/tirthbha/23-Homework2G1/assets/143649367/0abec22c-85eb-4efb-9809-69284dfc5194)
![Screenshot from 2023-09-25 20-21-07](https://github.com/tirthbha/23-Homework2G1/assets/143649367/62f1c99c-567b-4e47-99ae-908e86b0e55f)


### 2. Numpy Built-In Functions
NumPy provides efficient matrix multiplication and dot product functions. Here's how we how implemented it to preform matrix multiplication:

![Screenshot from 2023-09-25 20-22-29](https://github.com/tirthbha/23-Homework2G1/assets/143649367/a735cc84-42af-4594-b1c5-a157aba3ab8a)

### 3. Using Numpy Einstein Notation Function (einsum)
Nested Loops, Numpy Built-In Functions, and Numpy Einstein Notation Function (einsum)
Numpy's Einstein notation function allows you to specify contraction indices for complex operations. Here's how we used use it:

![Screenshot from 2023-09-25 20-25-32](https://github.com/tirthbha/23-Homework2G1/assets/143649367/9a6b5b37-80de-4492-887c-10318b99132e)

###### The entire code used to compute matrix multiplication of two matrices is given as below:
```python
# Importing necessary libraries
import numpy as np
import time
import matplotlib.pyplot as plt

# List to store the names of methods used
method_list = ["For Loops", "NumPy", "EinSum"]  # List to store methods used
time_list = [0, 0, 0]  # List to store execution time for each method

# Creating two matrices A, B of dimension 3x3
A = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
B = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

# Method 1: Manual matrix multiplication using nested loops
def matrix_multiply_manual(A, B):
    """
    Perform matrix multiplication using nested loops.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    C = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i, j] += A[i, k] * B[k, j]
    return C

# Method 2: NumPy's built-in matrix multiplication
def np_matrix_multiply(A, B):
    """
    Perform matrix multiplication using NumPy's built-in function.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    return np.dot(A, B)

# Method 3: Matrix multiplication using Einstein notation
def matrix_multiply_einsum(A, B):
    """
    Perform matrix multiplication using Einstein notation.

    Parameters:
    - A (numpy.ndarray): The first matrix.
    - B (numpy.ndarray): The second matrix.

    Returns:
    - C (numpy.ndarray): The result of matrix multiplication.
    """
    return np.einsum('ij,jk->ik', A, B)

# Measure execution time for each method
start_time = time.time()
C1 = matrix_multiply_manual(A, B)
end_time = time.time()
time_list[0] = end_time - start_time
print(f"Method 1 (Manual) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C2 = np_matrix_multiply(A, B)
end_time = time.time()
time_list[1] = end_time - start_time
print(f"Method 2 (NumPy) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C3 = matrix_multiply_einsum(A, B)
end_time = time.time()
time_list[2] = end_time - start_time
print(f"Method 3 (Einstein Notation) Execution Time: {end_time - start_time} seconds")

# Plotting Results

# Create a bar graph
plt.bar(method_list, time_list)

# Adding labels and title
plt.ylabel('Time (s)')
plt.title('Execution Time of a Program Calculating Multiplication of two 3x3 Matrices')

# Display the plot
plt.show()

```
## Performance Comparison

![Screenshot from 2023-09-26 12-02-02](https://github.com/tirthbha/23-Homework2G1/assets/143649367/68fe94c3-eed9-4b09-abcf-8f88d81dad35)

###### Based on the performance results given by three different approaches, we can make following conclusion

- Numpy einsum is the fastest, taking only 8.702278137207031e-05 seconds. This is because it allows for efficient customizations     and optimizations, making it a strong choice for complex matrix operations.

- Numpy built-in functions are the second fastest, taking 8.893013000488281e-05 seconds. These functions are highly optimized and    offer a good balance between performance and simplicity. They are a reliable choice for most matrix operations.

- Nested loops are the slowest, taking 32.781758069992065 seconds. This is because they lack the optimizations that numpy            provides, and they involve nested loops, leading to longer execution times, especially for larger matrices.

In conclusion, the choice of method should depend on our specific use case. If you need the fastest execution and have a good understanding of Einstein notation, numpy einsum is a great option. Numpy built-in functions offer a good balance between performance and simplicity. For loops (nested) are the most straightforward but should be reserved for small matrices or when simplicity is more important than performance.

# Dot Product
The dot product of the two matrices matrix1 and matrix2 is computed using Nested Loops, Numpy Built-In Functions, and Numpy Einstein Notation Function (einsum). Similar to what we observed in the prior example, using NumPy's np.einsum is once again the best choice in this scenario where execution time is critical. NumPy's np.einsum is appropriate for managing huge matrices and maximizing the project's execution time, since it is both concise and effective. Here's how we used these approaches to compute  dot product of two matrices:

###### The entire code used to compute dot product of two matrices is given as below:

```python
import numpy as np
import time

# Define two matrices (they can have different dimensions)
matrix1 = np.array([[200, 533, 233], [532, 332, 534], [6342, 4434, 3434]])
matrix2 = np.array([[4454, 5545, 5456], [2423, 434, 345], [6434, 84, 344]])

# Method 1: Using NumPy's np.sum
start_time = time.time()
dot_product_np_sum = np.sum(matrix1 * matrix2)
end_time = time.time()
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

start_time = time.time()
dot_product_loop_result = dot_product_loop(matrix1, matrix2)
end_time = time.time()
print(f"Dot Product using a loop: {dot_product_loop_result}")
print(f"Execution time using a loop: {end_time - start_time} seconds")

# Method 3: Using NumPy's np.einsum
start_time = time.time()
dot_product_einsum = np.einsum('ij,ij->', matrix1, matrix2)
end_time = time.time()
print(f"Dot Product using np.einsum: {dot_product_einsum}")
print(f"Execution time using np.einsum: {end_time - start_time} seconds")
```
###### Output
![Screenshot from 2023-09-26 00-26-18](https://github.com/tirthbha/23-Homework2G1/assets/143649367/0da350e9-9a52-4733-b9d8-e646ceaf1344)

In summary, while np.einsum may have a learning curve due to its index notation, it provides a powerful and efficient way to work with complex tensor operations, making it a valuable tool in scientific computing and data manipulation tasks. Its advantages include conciseness, readability, performance, versatility, customization, broadcasting support, and the ability to handle complex operations with ease.

# References
- IBM Quantum lab
- Google colab
- CHATgpt
- https://github.com/ubsuny/CompPhys/blob/main/ReviewPython/EinsteinNotation.ipynb 


