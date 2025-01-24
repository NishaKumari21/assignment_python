# Q1Write a function that takes a list and a number as arguments. Add the number to the end of
# the list, then remove the first element of the list. The function should then return the updated
# list.
lst = [1, 2, 3, 4, 5] 
number=2
def input_list(lst,number):
    lst = [1, 2, 3, 4, 5]
    lst.append(number)
    rem=lst.pop(lst[0])
    return ("after removing the first element:",lst)
                                              
print(input_list(lst,number))
# Q2Create the function that takes a list of dictionaries and returns the sum of people
# budgets.
def sum_budget(salaries):
    s=sum(salaries.values())
    return ("their sum is:",s)
salaries={"ayush":9990,
          "nisha":7898,
          "rahul":6666,
          "pummy":4787}
print(sum_budget(salaries))
# Q3Create a function that takes a string and returns a string with its letters in alphabetical order.
def alpha_sort(string):
    return sorted(string)
string="hello"
print(alpha_sort(string))
"""Q4Question4
Suppose that you invest $10,000 for 10 years at an interest rate of 6% compounded monthly.
What will be the value of your investment at the end of the 10 year period?
Create a function that accepts the principal p, the term in years t, the interest rate r, and the
number of compounding periods per year n. The function returns the value at the end of term
rounded to the nearest cent."""
def ci(p,t,r,n):
    return round(p*(1+r/n)**(n*t),2)

p= 10000
n = 10
t = 1
r = 0.06
print(ci(p,t,r,n))
# Q5Write a function that takes a list of elements and returns only the integers.
def reint(input_list):
    result = []  
    for i in input_list:
        if type(i) == int:  
         result.append(i)  
    return "These are the integer type elements:", result

input_list = [2, 4, "nisha", "hj", "park"]
print(reint(input_list))



