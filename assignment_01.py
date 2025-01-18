# 1. Write a Python program to print Hello Python;?
# 2. Write a Python program to do arithmetical operations addition and division.?
# 3. Write a Python program to find the area of a triangle?
# 4. Write a Python program to swap two variables?
# 5. Write a Python program to generate a random number?
# -----------------------------------------
print("hello python!")

# 2. Arithmetic Operations
first=int(input("enter the first variable"))
second=int(input("enter the second the second variable"))
a=input("choose the operation:add,divide")
if a=="add":
    print("addition is:",first+second)
else:
    print("division is:",first/second)
#Q3Area of a triangle
base=int(input("enter the base value:"))
height=int(input("enter the height of the trainge"))
area=1/2*base*height
print("area is:",area)

 #Q4  To swap two variables
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
a=b
c=a
b=c

print("a:",a)
print("b:",b)
#Q5 To  generate a random number
import random
print("random number is:",random.randint(1,100))