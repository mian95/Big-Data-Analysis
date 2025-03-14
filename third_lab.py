import numpy as np


""" Concatenation ===> axis 0 for vertical, axis 1 for horizontal"""
a = np.array([[1,2,3,7],[9,8,7,5]])
b = np.array([[9,8,7],[1,2,3]])

print( np.concatenate((a,b), axis=1) ) ### OR   np.concatenate((a,b), axis=0)


"""Size ===> tells the total number of elements in the array"""
print(a.size)

'''Shape tells the dimensions of the array'''
print(a.shape)

'''Reshape allows to change the dimensions of the array'''
print(f"reshaped : { a.reshape(4,2)}")
print(f"reshaped : {a.reshape(2,4)}") 

'''newaxia is used to add a new axis to the array'''
newaxia=a[np.newaxis, np.newaxis]
print(newaxia.shape)

'''Expand array to increase the dimension'''
expand_x=np.expand_dims(a, axis=1)
print(expand_x.shape)
