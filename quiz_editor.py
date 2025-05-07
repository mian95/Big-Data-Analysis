import numpy as np

print("Task-1: Basic Array Creation & Indexing")
# Create a 1D array from 10 to 20
arr1 = np.arange(10, 21)
print("Original array:", arr1)

# Extract first three elements
first_three = arr1[:3]
print("First three elements:", first_three)

# Modify last element to 100
arr1[-1] = 100
print("Array after modifying last element:", arr1)

print("\nTask-2: Array Slicing & Views")
# Create array from 1 to 10
arr2 = np.arange(1, 11)
print("Original array:", arr2)

# Extract even numbers using slicing
even_numbers = arr2[1::2]
print("Even numbers:", even_numbers)

# Modify an element in the slice
even_numbers[0] = 20
print("After modifying slice:", arr2)  # Original array is affected because slice is a view

print("\nTask-3: Multi-Dimensional Arrays")
# Create 3x3 array
arr3 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("3x3 array:\n", arr3)

# Get element in second row, third column
element = arr3[1, 2]
print("Element in second row, third column:", element)

# Extract second column
second_column = arr3[:, 1]
print("Second column:", second_column)

print("\nTask-4: Array Attributes")
# Create 4x2 array of random integers
arr4 = np.random.randint(0, 51, size=(4, 2))
print("Random array:\n", arr4)
print("Shape:", arr4.shape)
print("Size:", arr4.size)
print("Number of dimensions:", arr4.ndim)

print("\nTask-5: Array Creation Functions")
# Array of zeros
zeros_arr = np.zeros(5, dtype=int)
print("Array of zeros:", zeros_arr)

# Identity matrix
identity_matrix = np.eye(3)
print("3x3 Identity matrix:\n", identity_matrix)

# Evenly spaced numbers
linspace_arr = np.linspace(0, 100, 10)
print("Evenly spaced numbers:", linspace_arr)

print("\nTask-6: Sorting & Concatenation")
# Sort array
arr6 = np.array([8, 2, 5, 1, 7])
sorted_arr = np.sort(arr6)
print("Sorted array:", sorted_arr)

# Concatenate arrays
arr1_concatenate = np.array([1, 2, 3])
arr2_concatenate = np.array([4, 5, 6])
concatenated = np.concatenate([arr1_concatenate, arr2_concatenate])
print("Concatenated array:", concatenated)

print("\nTask-7: Reshaping & Expanding Dimensions")
# Create and reshape array
arr7 = np.arange(6)
reshaped = arr7.reshape(2, 3)
print("Reshaped array:\n", reshaped)

# Convert to column vector
column_vector = arr7[:, np.newaxis]
print("Column vector:\n", column_vector)

# Convert to row vector
row_vector = np.expand_dims(arr7, axis=0)
print("Row vector:\n", row_vector)