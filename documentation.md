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

## Performance Comparison

###### Based on the performance results given by three different approaches, we can make following conclusion

- Numpy einsum is the fastest, taking only 8.702278137207031e-05 seconds. This is because it allows for efficient customizations     and optimizations, making it a strong choice for complex matrix operations.

- Numpy built-in functions are the second fastest, taking 8.893013000488281e-05 seconds. These functions are highly optimized and    offer a good balance between performance and simplicity. They are a reliable choice for most matrix operations.

- Nested loops are the slowest, taking 32.781758069992065 seconds. This is because they lack the optimizations that numpy            provides, and they involve nested loops, leading to longer execution times, especially for larger matrices.

In conclusion, the choice of method should depend on our specific use case. If you need the fastest execution and have a good understanding of Einstein notation, numpy einsum is a great option. Numpy built-in functions offer a good balance between performance and simplicity. For loops (nested) are the most straightforward but should be reserved for small matrices or when simplicity is more important than performance.

# Dot Product
The dot product of the two matrices matrix1 and matrix2 is computed using Nested Loops, Numpy Built-In Functions, and Numpy Einstein Notation Function (einsum). Similar to what we observed in the prior example, using NumPy's np.einsum is once again the best choice in this scenario where execution time is critical. NumPy's np.einsum is appropriate for managing huge matrices and maximizing the project's execution time, since it is both concise and effective. Here's how we used these approaches to compute  dot product of two matrices:
![Green White Aesthetic Floral Blank Document Border](https://github.com/tirthbha/23-Homework2G1/assets/143649367/c8a03375-1870-42ef-91f7-5bb1b91232c5)
![Screenshot from 2023-09-26 00-26-18](https://github.com/tirthbha/23-Homework2G1/assets/143649367/0da350e9-9a52-4733-b9d8-e646ceaf1344)

In summary, while np.einsum may have a learning curve due to its index notation, it provides a powerful and efficient way to work with complex tensor operations, making it a valuable tool in scientific computing and data manipulation tasks. Its advantages include conciseness, readability, performance, versatility, customization, broadcasting support, and the ability to handle complex operations with ease.




  
 


