#Importing some necessary liberaries for the code.
import numpy as np
import time
import matplotlib.pyplot as plt

method_list = ["For Loops", "NumPy", "EinSum"] # List To Store Methods Used
time_list = [0,0,0] # List to execution time for each method

# Creating two matrices A, B of dimention 3*3. 
A = np.array([[200,533,233],[532,332,534],[6342,4434,3434]])
B = np.array([[4454,5545,5456],[2423,434,345],[6434,84,344]])
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
time_list[0]=end_time - start_time
print(f"Method 1 (Manual) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C2 = np_matrix_multiply(A, B)
end_time = time.time()
time_list[1]=end_time - start_time
print(f"Method 2 (NumPy) Execution Time: {end_time - start_time} seconds")

start_time = time.time()
C3 = matrix_multiply_einsum(A, B)
end_time = time.time()
time_list[2]=end_time - start_time
print(f"Method 3 (Einstein Notation) Execution Time: {end_time - start_time} seconds")

# Plotting Results

# Create a bar graph
#plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.bar(method_list, time_list)

# Adding labels and title
#plt.xlabel('Method')
plt.ylabel('Time (s)')
plt.title('Execution Time of a Program Calculating Product of two 3x3 Matrices')

# Display the plot
plt.show()
