# 1. Write a Python program to convert kilometers to miles?
# 2. Write a Python program to convert Celsius to Fahrenheit?
# 3. Write a Python program to display calendar?
# 4. Write a Python program to solve quadratic equation?
# 5. Write a Python program to swap two variables without temp variable?
# 6. Write a Python program to find the sum of all elements in a list?
# 7. Write a Python program to find the maximum and minimum value in a list?

# Q1 To convert kilometers to miles--------
km=int(input("enter the kilometers"))
miles=km*0.621371
print("after converting:",miles)
# Q2.To convert Celsius to Fahrenheit
C=int(input("enter the Fahrenheit"))
F=C*9/5+32
print("after converting:",F)
# Q3.To display calendar
import calendar
year = 2025
month = 7
print(calendar.month(year, month))
# Q4.to solve quadratic equation
import cmath  
print("Solve the quadratic equation ax^2 + bx + c = 0")
# Input coefficients
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
# Check if it's a quadratic equation
if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    # Calculate the discriminant
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    
    # Calculate the two roots
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    print(f"The roots of the quadratic equation are: {root1} and {root2}")

# Q5swap two variables without temp variable
a = 9
b = 2
a,b =b, a
print(a)  
print(b)
# Q6.to find the sum of all elements in a list
l=[2,4,57,88,5]
p=sum(l)
print(p)
# Q7 To find the maximum and minimum value in a list
l=[2,5,7,9]
max_value=max(l)
print(max_value)
min_value=min(l)
print(min_value)