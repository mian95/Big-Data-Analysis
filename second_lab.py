import numpy as np

# Create a zeros
"""create a zeros array with given shape and datatype"""
zeros = np.zeros([2,3,4,6], dtype=np.int64)
# print(zeros)


"""create ones array with given datatype"""
print(np.ones([3,5,6,8], dtype=np.int64))

"""Empty array creation"""
print(np.empty([2,4,6,8]))


"""create Arrange array =====> with given start, stop and step"""
# print(np.arange(1,10,2))

"""create linspace array =====> with given start, stop and number of samples"""
# print(np.linspace(0,10,20))


"""How to Sort the array elements"""
arr=[17, 4, 20, 5, 33, 6, 18, 39, 71, 10]
# print(np.sort(arr, kind='quicksort'))

"""argsort array index =====> return the index of sorted array"""
print(np.argsort(arr))


""" Generate an empty 4 dimensional array fill elements in it using for loop """

arr_4d = np.empty((4, 4, 4, 4))
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                arr_4d[i, j, k, l] = i*j*k*l
                print(arr_4d)