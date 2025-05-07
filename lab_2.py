import numpy as np

# Create a zeros array with given shape and datatype
# np.zeros() creates an array filled with zeros. The first argument is the shape of the array, and the second argument is the data type.
# In this case, we're creating a 4-dimensional array with shape (2,3,4,6) and data type np.int64.
zeros = np.zeros([2,3,4,6], dtype=np.int64)
# print(zeros)

# Create ones array with given datatype
# np.ones() creates an array filled with ones. The first argument is the shape of the array, and the second argument is the data type.
# In this case, we're creating a 4-dimensional array with shape (3,5,6,8) and data type np.int64.
print(np.ones([3,5,6,8], dtype=np.int64))

# Empty array creation
# np.empty() creates an array without initializing the entries. The first argument is the shape of the array.
# In this case, we're creating a 4-dimensional array with shape (2,4,6,8).
print(np.empty([2,4,6,8]))

# Create Arrange array with given start, stop, and step
# np.arange() creates an array with evenly spaced values within a given range. The first argument is the start of the range, the second is the end of the range, and the third is the step size.
# In this case, we're creating an array from 1 to 10 with a step size of 2.
# print(np.arange(1,10,2))

# Create linspace array with given start, stop, and number of samples
# np.linspace() creates an array with evenly spaced values within a given range. The first argument is the start of the range, the second is the end of the range, and the third is the number of samples.
# In this case, we're creating an array from 0 to 10 with 20 samples.
# print(np.linspace(0,10,20))

# How to Sort the array elements
# np.sort() sorts an array in ascending order. The first argument is the array to be sorted, and the second argument is the sorting algorithm to use.
# In this case, we're sorting the array using the 'quicksort' algorithm.
arr=[17, 4, 20, 5, 33, 6, 18, 39, 71, 10]
# print(np.sort(arr, kind='quicksort'))

# Argsort array index returns the index of sorted array
# np.argsort() returns the indices that would sort an array. The first argument is the array to be sorted.
print(np.argsort(arr))

# Generate an empty 4 dimensional array and fill elements in it using for loop
# np.empty() creates an array without initializing the entries. The first argument is the shape of the array.
# In this case, we're creating a 4-dimensional array with shape (4,4,4,4).
arr_4d = np.empty((4, 4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                # We're filling each element of the array with the product of its indices.
                arr_4d[i, j, k, l] = i*j*k*l
                print(arr_4d)