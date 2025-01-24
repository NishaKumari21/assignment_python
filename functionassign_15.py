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


