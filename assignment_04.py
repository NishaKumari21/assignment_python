# 1. Write a Python Program to Find the Factorial of a Number?
# 2. Write a Python Program to Display the multiplication Table?
# 3. Write a Python Program to Print the Fibonacci sequence?
# 4. Write a Python Program to Check Armstrong Number?
# 5. Write a Python Program to Find Armstrong Number in an Interval?

# Q1.Find the Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

    # Q2.Display the multiplication Table
n=int(input("enter a number"))
for i in range(1,11):
    print(f"{i}*{n}:",i*n)
# Q3.Print the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
# Q4.to Check Armstrong Number
n = int(input("Enter a number: "))
num_digits = len(str(n))
sum_digits = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum_digits += digit ** num_digits
    temp //= 10
if sum_digits == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
                  