import numpy as np
arr=np.array([1,2,3,4,5])
print("Array elements :",arr)

#creating 1-D array:
arr1=np.array([1,2,3])
print(arr1)
print("Array at index 0: ",arr1[0])
print("Array at index 1: ",arr1[1])
print("Array at index 2: ",arr1[2])

arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print("2nd element on 1st row : ",arr2[0,1])
print("5th element on 2nd row : ",arr2[1,4])

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print(arr3[0,1,2])
print(arr3[1,1,2])