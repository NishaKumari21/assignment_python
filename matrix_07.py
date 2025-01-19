from numpy import *
arr1=array([

    [2,3,4,8,6,7],
    [5,6,7,8,9,5]
])
# converting 2 dimensional to 1 dimensional array by using flatten
arr2=arr1.flatten()
print("one dimensional array from 2 dimensional array:",arr2)
print("array in matrix:",arr1)
print("the type of 2 dimentional arrays:",arr1.dtype)
print("the type of 2 dimentional arrays:",arr1.shape)
print("the type of 2 dimentional arrays:",arr1.size)
# 2 dimensional arrays
arr3=arr2.reshape(3,4)
print(arr3)
print(arr3.shape)
print(arr3.dtype)
#3 dimensional arrays:
arr4=arr2.reshape(2,2,3)
# 2 array inside array4 amd 2 row and 3 column
print(arr4)
print(arr4.dtype)
# MATRICES
# semi column means [1 2 3]
m=matrix('1 2 3;6 4 5; 1 5 6')
print("matrix looks like:",m)
print("diagonal of matrix:",diagonal(m))
print("minium of matrix:",m.min())
print("maximun of matrix:",m.max())
# question----------------------------
'''1. Write a Python Program to Add Two Matrices?
2. Write a Python Program to Multiply Two Matrices?
3. Write a Python Program to Transpose a Matrix?
4. Write a Python Program to Sort Words in Alphabetic Order?
# 5. Write a Python Program to Remove Punctuation From a String?'''
# 1. Write a Python Program to Add Two Matrices and muplication too?

m1=matrix('1 4 5; 3 5 12; 4 6 3')
m2=matrix('2 14 5; 4 6 10; 4 3 3')
m3=m1+m2
m4=m1*m2
print("after addition:",m3)
print("after multiplication:",m4)
#2o Transpose a Matrix
# transpose means to convert rows to column and columns to row and make a matrix
trans=matrix('1 4 5; 3 5 12; 4 6 3')
transpose = trans.T  
# Use the `.T` attribute to transpose
print("Transposed Matrix:")
print(transpose)
# 4. Write a Python Program to Sort Words in Alphabetic Order?
sentence="this is my friend isha"
words=sentence.split()
y=words.sort()
print(y)
# Q5# 5. Write a Python Program to Remove Punctuation From a String?
s="this is @gtreahk"
print(s.remove("@"))
