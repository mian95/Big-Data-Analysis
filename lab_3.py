import numpy as np


""" Concatenation ===> axis 0 for vertical, axis 1 for horizontal
    np.concatenate() is used to join two or more arrays along a specified axis.
    The 'axis' argument specifies the axis along which the arrays will be joined.
    For example, if 'axis=0', the arrays will be stacked vertically (row-wise).
    If 'axis=1', the arrays will be stacked horizontally (column-wise).
    Other possible values for 'axis' depend on the dimensionality of the arrays.
    For 1D arrays, 'axis' can be 0. For 2D arrays, 'axis' can be 0 or 1.
    For 3D arrays, 'axis' can be 0, 1, or 2, and so on.
"""
a = np.array([[1,2,3,7],[9,8,7,5]])
b = np.array([[9,8,7],[1,2,3]])

print( np.concatenate((a,b), axis=1) ) ### OR   np.concatenate((a,b), axis=0)


"""Size ===> tells the total number of elements in the array
    The 'size' attribute returns the total number of elements in the array.
    It is a property of the array object and does not require any arguments.
"""
print(a.size)

'''Shape tells the dimensions of the array
    The 'shape' attribute returns a tuple representing the dimensions of the array.
    It is a property of the array object and does not require any arguments.
    For example, a 2D array with 2 rows and 4 columns would have a shape of (2, 4).
'''
print(a.shape)

'''Reshape allows to change the dimensions of the array
    The 'reshape' method changes the shape of an array without changing its data.
    It requires a tuple of integers representing the new dimensions.
    For example, reshaping a 2D array with 8 elements from (2, 4) to (4, 2) or (1, 8).
    Note that the total number of elements must remain the same.
'''
print(f"reshaped : { a.reshape(4,2)}")
print(f"reshaped : {a.reshape(2,4)}") 

'''newaxia is used to add a new axis to the array
    Indexing with 'np.newaxis' or 'None' adds a new axis to the array.
    This is useful for increasing the dimensionality of an array for broadcasting or other operations.
    For example, adding a new axis to a 2D array would make it a 3D array.
'''
newaxia=a[np.newaxis, np.newaxis]
print(newaxia.shape)

'''Expand array to increase the dimension
    The 'expand_dims' function adds a new axis to the array at a specified position.
    It requires the array and the axis position as arguments.
    For example, adding a new axis at position 1 to a 2D array would make it a 3D array.
    The 'axis' argument can be any integer from 0 to the current number of dimensions.
'''
expand_x=np.expand_dims(a, axis=1)
print(expand_x.shape)
