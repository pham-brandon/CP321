import numpy as np

# Task 1
def modifier(data):
    # 1. Print the first and last elements from the first and the last row.
    print("\nOutput of item 1 above is:")
    print(f"{data[0,0]}, {data[0,-1]}, {data[-1,0]}, {data[-1,-1]}")
    
    # 2. Create an array of random values. Round the random values to 0 digits after the decimal point. Combine it as the last column to ‘data’. Print the ‘data’.
    print("\nOutput of item 2 above is:")
    random_val = np.random.randint(0,100, size=(data.shape[0],1))
    random_val = np.round(random_val,0).astype(int)
    data = np.hstack((data, random_val.reshape(-1,1)))
    print(data)

    # 3. Extract the second last row from the ‘data’ and print it in reverse order.
    print("\nOutput of item 3 above is:")
    print(data[-2,::-1])

    # 4. Calculate mean for each column in the data and return all the means as a list.
    print("\nOutput of item 4 above is:")
    mean_col = np.mean(data, axis=0)
    mean_col = np.round(mean_col,2)
    print(mean_col)
    return mean_col.tolist()

# Task 2
def grade_stats(data):
    # 1. Prints the quiz numbers where the mean is above 70%
    print("\nThe output for item 1 above is:")
    quiz_mean = np.mean(data[:,1:], axis=0)
    quiz_mean_gt_70 = [f"Quiz {x+1}" for x, mean in enumerate(quiz_mean) if mean>7]
    print("Quizzes with mean above 70%:", ", ".join(quiz_mean_gt_70))

    # 2. Prints student Id for all the students whose mean in above 79%
    print("\nThe output for item 2 above is:")
    student_mean = np.mean(data[:,1:], axis=1)
    student_mean_gt_79 = data[:,0][student_mean>7.9]
    print("Students with mean above 79%:", ", ".join(map(str, student_mean_gt_79)))

    # 3. Prints student Id for all the students who scored 100% in the last quiz.
    print("\nThe output for item 3 above is:")
    student_100 = data[:,0][data[:,-1]==10]
    print("Students with 100% in last quiz:", ", ".join(map(str, student_100)))

# Task 3
def matrix_manipulator(A, B):
    # 1. Calculate the transpose of matrix A and store it in a variable A_transpose and print it.
    print("\nThe output for item 1 above is:")
    A_transpose = np.transpose(A)
    print(A_transpose)

    # 2. Calculate the dot product of A and B and store it in a variable AB_dot. Print AB_dot in the terminal.
    print("\nThe output for item 2 above is:")
    AB_dot = np.dot(A,B)
    print(AB_dot)

    # 3. Add AB_dot to the transpose of B and store the result in result. Print the resulting matric in the terminal.
    print("\nThe output for item 3 above is:")
    result = np.transpose(B) + AB_dot
    print(result)