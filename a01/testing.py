import numpy as np
from functions import modifier, grade_stats, matrix_manipulator

# Task 1
print("If the 'data' is:")
t01_data = np.array([
    [1,2,3], 
    [2,3,4], 
    [5,6,7]
])
print(t01_data)
modifier(t01_data)

# Task 2
print("\nIf the ‘data’ is:")
t02_data = np.array([
    [123456,9,8,0,2],
    [234567,8,8,0,5],
    [345678,9,8,6,10],
    [456789,8,7,7,10]
])
print(t02_data)
grade_stats(t02_data)

# Task 3
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
matrix_manipulator(A, B)