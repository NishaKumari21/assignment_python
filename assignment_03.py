# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
# 2. Write a Python Program to Check if a Number is Odd or Even?
# 3. Write a Python Program to Check Leap Year?
# 4. Write a Python Program to Check Prime Number?



# 1. Check if a Number is Positive, Negative or Zero
number=int(input("enter the number:"))
if number==0:
    print("the number is zero")
elif number>0:
    print("the number is positive")
else:
    print("the number is negative")

#Q2. to Check if a Number is Odd or Even
number=int(input("enter the number:"))
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")

#Q3. to Check Leap Year
year=int(input("enter the year:"))
if year%4==0:
    print("the year leap")
else:
    print("the year not leap")

#Q4.to Check Prime Number
num = int(input("Enter a number: "))
if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")