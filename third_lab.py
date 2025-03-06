import numpy as np


""" Concatenation """
a = np.array([[1,2,3,7],[9,8,7,5]])
b = np.array([[9,8,7],[1,2,3]])

c = np.concatenate((a,b), axis=1) ### OR   np.concatenate((a,b), axis=0)

# print(c)

""" Reshaping the array =====> you to reshape or reimagine the array that we want to make"""

d = a.reshape((4,2))
print(d)

