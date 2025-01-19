# 1. Write a Python Program to find sum of array?
# 2. Write a Python Program to find largest element in an array?
# 3. Write a Python Program for array rotation?
# 4. Write a Python Program to Split the array and add the first part to the end?
# 5. Write a Python Program to check if given array is Monotonic?
# Q1.To print of array:
from array import *
v=array('i',[2,34,-56,38,2])
# i =signed int
print("information of buffer:",v.buffer_info())
# size of the array:buffer.info()
a=v.reverse()
print("reverse:",a)
print("tpecode of array:",v.typecode)
# typecode--type of value used eg signed int,unsigned int,bytes etc.
print("no of time varaible present:",v.count(2))
# to print one by one value:
for i in v:
    print(i)
# length of array:
print("length:",len(v))
#----------------------------------------------------------------
# append of array:
print(v.append(9))
print(v)
#----------------------------------------------------------------
#Q2 largest element in array:
print("largest element in array:",max(v))
#----------------------------------------------------------------
# Q1sum of elements in array:
print("sum of elements in array:",sum(v))
#----------------------------------------------------------------
#Q3array rotation:
# print("roatation in array:",rotate(v))
# ---------------------------------------------------------------
# monotonic means kisi ek direction mei increase krna ya decrease krna 
# Q5Function to check if a list is monotonic
def is_monotonic(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)

print(is_monotonic([2, 38, -56, 34, 2, 9]))  # True (Increasing)
print(is_monotonic([2, 38, -56, 34, 2, 9]))  # True (Decreasing)
print(is_monotonic([2, 38, -56, 34, 2, 9]))  # False (Not monotonic)
#Q4 splitting array by diving the array into first half and second half .Then adding first half to the second half:
def split(self,x,y):
    self.x=x
    self.y=y
    return self.x,self.y
arr=[2,34,5,67,4]
x=(arr[0:2])
y=(arr[2:5])
print(x)
print(y)
print("after adding first half to the second half array:",y+x)