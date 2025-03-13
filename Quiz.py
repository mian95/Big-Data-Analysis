import numpy as np

#Task === 1
arr = np.arange(10, 21)
print("#1 ==> Original Array:", arr)

""" Extract elements (example: first 3 elements)"""
ex = arr[:3]
print("#2 ==> Extracted first 3 elements", ex)

"""Modify the last element"""
arr[-1] = 100
print("#3 ===> Modified Array:", arr)

"""Task === 2"""
#4
arr2= np.arange(1,11)
evenCopy = arr2[arr2 % 2 == 0]
print("Even numbers in the array:", evenCopy)
#5
evenCopy[0] = 200
print("Original Is not Change ?", arr2[0] != 200)


"""Task === 3"""
#6
arr3 = np.arange(1, 10).reshape(3,3)
print("3-D array", arr3)
#7
print("#7 ==> 2nd and 3rd column",arr3[:,1:3])
#8
print("#8 ==> 2nd column",arr3[:,1:2].reshape(1,3))


"""Task === 4"""
arr4 = np.random.randint(0, 51, size=(4, 2))
print("#9 ===> ",arr4)
print("Shape:", arr4.shape)  
print("Size:", arr4.size)    
print("Dimensions:", arr4.ndim)  

"""Task === 5"""
arr5 = np.zeros(5, dtype=int)  
print(arr5)
arr6 = np.eye(3) 
print(arr6)
arr7 = np.linspace(0, 100, 10)  
print(arr7)

"""Task === 6"""
arr8 = np.array([0,2,5,1,7])
print("descending order,:", np.sort(arr8)[::-1])
arr9 = np.array([0,2,5,1,7])
arr10 = np.array([4,5,6])
print('Concatenated Array', np.concatenate((arr9,arr10), axis=0) )