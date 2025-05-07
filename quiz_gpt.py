import numpy as np

# Task-1: Basic Array Creation & Indexing
arr1 = np.arange(10, 21)  # 10 to 20 inclusive
print("Task 1 - Original Array:", arr1)

first_three = arr1[:3]
print("First three elements:", first_three)

arr1[-1] = 100
print("Modified last element:", arr1)


# Task-2: Array Slicing & Views
arr2 = np.arange(1, 11)
print("\nTask 2 - Original Array:", arr2)

even_slice = arr2[1::2]  # index 1 is 2, then every 2nd element
print("Even numbers slice:", even_slice)

even_slice[0] = 99
print("Modified slice:", even_slice)
print("Check if original array is affected:", arr2)


# Task-3: Multi-Dimensional Arrays
arr3 = np.arange(1, 10).reshape(3, 3)
print("\nTask 3 - 3x3 Array:\n", arr3)

element = arr3[1, 2]  # second row, third column (indexing from 0)
print("Element at (2nd row, 3rd column):", element)

second_column = arr3[:, 1]
print("Second column as 1D array:", second_column)


# Task-4: Array Attributes
arr4 = np.random.randint(0, 51, (4, 2))
print("\nTask 4 - 4x2 Random Array:\n", arr4)

print("Shape:", arr4.shape)
print("Size:", arr4.size)
print("Number of dimensions:", arr4.ndim)


# Task-5: Array Creation Functions
zeros_arr = np.zeros(5, dtype=int)
print("\nTask 5 - Array of 5 zeros (int):", zeros_arr)

identity_matrix = np.eye(3)
print("3x3 Identity matrix:\n", identity_matrix)

linspace_arr = np.linspace(0, 100, 10)
print("10 evenly spaced numbers between 0 and 100:", linspace_arr)


# Task-6: Sorting & Concatenation
arr6 = np.array([8, 2, 5, 1, 7])
sorted_arr = np.sort(arr6)
print("\nTask 6 - Sorted array:", sorted_arr)

arr_a = np.array([1, 2, 3])
arr_b = np.array([4, 5, 6])
concatenated = np.concatenate((arr_a, arr_b))
print("Concatenated arrays:", concatenated)


# Task-7: Reshaping & Expanding Dimensions
arr7 = np.arange(1, 7)
reshaped = arr7.reshape(2, 3)
print("\nTask 7 - Reshaped to 2x3:\n", reshaped)

column_vector = arr7[:, np.newaxis]
print("Column vector:\n", column_vector)

row_vector = np.expand_dims(arr7, axis=0)
print("Row vector using expand_dims:\n", row_vector)
