"""Question 1:
Please write a program using generator to print the numbers which can be divisible by 5 and
7 between 0 and n in comma separated form while n is input by console.
Example:
If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70

Question 2:
Please write a program using generator to print the even numbers between 0 and n in comma
separated form while n is input by console.
Example:
If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10



Question 4:
Assuming that we have some email addresses in the &quot;username@companyname.com&quot; format,
please write program to print the user name of a given email address. Both user names and
company names are composed of letters only.
Example:
If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john

Question 5:
Define a class named Shape and its subclass Square. The Square class has an init function
which takes a length as argument. Both classes have a area function which can print the area
of the shape where Shape&#39;s area is 0 by default."""
# Q1.
n=int(input("eneter the n:"))
def divisible_5_7(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i
print("number divisible by 5 and 7:")
for num in divisible_5_7(n):
 print(num)
# Q2
num=int(input("enter the range:"))
def even(num):
   for i in range(num+1):
      if i%2==0:
         yield i
print("number which are even are:")
for n in even(num):
   print(n)
# Q3
email=input("enter your email addrress:")
def em(email):
   username=email.split('@')
#    ['nisha', 'gmail.com'] then we will choose [0] index to get username i.e nisha
   return username
print("the username from email adress is:")
print(em(email))
# Q4
class shape:
 def __init__(self):
  pass
 def area(self):
  return 0
class square(shape):
 def __init__(self,length):
    super().__init__
    self.length=length
 def area(self):
  return self.length**2
 
obj_shape=shape()
print("Area of Shape: ",obj_shape.area())
obj_square=square(5)
print("Area of Square: ",obj_square.area())
