import numpy as np

# ====================== Task-1: Basic Array Creation & Indexing ======================
# 1. Create 1D array with numbers 10-20
base_array = np.arange(10, 21)
print("Task 1.1 - Base array (10-20):\n", base_array)

# 2. Extract first three elements
first_three = base_array[:3]
print("\nTask 1.2 - First three elements:\n", first_three)

# 3. Modify last element to 100
base_array[-1] = 100
print("\nTask 1.3 - Modified last element:\n", base_array)

# ====================== Task-2: Array Slicing & Views ======================
# 4. Create array 1-10 and extract even numbers
numbers = np.arange(1, 11)
even_numbers = numbers[numbers % 2 == 0]
print("\nTask 2.4 - Even numbers slice:\n", even_numbers)

# 5. Test array view behavior
even_numbers[0] = 200  # This modifies the copy, not original
print("\nTask 2.5 - Original array unaffected?",
      numbers[1] != 200)  # First even number is at index 1 (value 2)

# ====================== Task-3: Multi-Dimensional Arrays ======================
# 6. Create 3x3 matrix
matrix_3x3 = np.arange(1, 10).reshape(3, 3)
print("\nTask 3.6 - 3x3 matrix:\n", matrix_3x3)

# 7. Get element at 2nd row (index 1), 3rd column (index 2)
element = matrix_3x3[1, 2]
print("\nTask 3.7 - Element at 2nd row, 3rd column:", element)

# 8. Extract second column as 1D array
second_column = matrix_3x3[:, 1]
print("\nTask 3.8 - Second column as 1D array:\n", second_column)

# ====================== Task-4: Array Attributes ======================
# 9. Create random 4x2 array
random_array = np.random.randint(0, 51, size=(4, 2))
print("\nTask 4.9 - Random 4x2 array:\n", random_array)

# 10. Display array properties
print("\nTask 4.10 - Array Properties:")
print("Shape:", random_array.shape)
print("Size (total elements):", random_array.size)
print("Dimensions:", random_array.ndim)

# ====================== Task-5: Array Creation Functions ======================
# 11. Integer zeros array
zero_array = np.zeros(5, dtype=int)
print("\nTask 5.11 - Integer zeros array:\n", zero_array)

# 12. Identity matrix
identity_matrix = np.eye(3)
print("\nTask 5.12 - 3x3 identity matrix:\n", identity_matrix)

# 13. Evenly spaced values
spaced_array = np.linspace(0, 100, 10)
print("\nTask 5.13 - 10 values from 0-100:\n", spaced_array)

# ====================== Task-6: Sorting & Concatenation ======================
# 14. Sort array in ascending order
original_array = np.array([8, 2, 5, 1, 7])
sorted_array = np.sort(original_array)
print("\nTask 6.14 - Sorted ascending:\n", sorted_array)

# 15. Concatenate two arrays
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
combined = np.concatenate((array_a, array_b))
print("\nTask 6.15 - Combined arrays:\n", combined)

# ====================== Task-7: Reshaping & Expanding Dimensions ======================
# 16. Reshape 6-element array to 2x3
original_1d = np.arange(6)
reshaped_2x3 = original_1d.reshape(2, 3)
print("\nTask 7.16 - Reshaped 2x3 matrix:\n", reshaped_2x3)

# 17. Create column vector
column_vector = original_1d[:, np.newaxis]
print("\nTask 7.17 - Column vector:\n", column_vector)

# 18. Create row vector using expand_dims
row_vector = np.expand_dims(original_1d, axis=0)
print("\nTask 7.18 - Row vector:\n", row_vector)