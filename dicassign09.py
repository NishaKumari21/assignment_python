'''1. Write a Python program to Extract Unique values dictionary values?
2. Write a Python program to find the sum of all items in a dictionary?
3. Write a Python program to Merging two Dictionaries?
4. Write a Python program to convert key-values list to flat dictionary?
5. Write a Python program to insertion at the beginning in OrderedDict?
6. Write a Python program to check order of character in string using OrderedDict()?
7. Write a Python program to sort Python Dictionaries by Key or Value?'''
# Q1to Extract Unique values dictionary values
dic={"name":"nisha",
     "age":19,
     "course":"data science",
     "color":"pink"}
print(dic)
# index value
print(dic.get(1,'found'))
print(dic.get(4,'not found'))
print(dic.values())
# Q3to Merging two Dictionaries
d2={"class":1,
    "good":"looking",
    "grade":90}
merged_dict = {**dic, **d2}
print("first option:",merged_dict)
# Using the | Operator
m2_dic=dic|d2
print("another option to merge dic:",m2_dic)
# Using update function
dic.update(d2)
print("by using update function we can merge :",dic)

# Q4to convert key-values list to flat dictionary

key_values=[("name","nisha"),("age",19),("course","data science"),("color","pink")]
flat_dict=dict(key_values)
print("converted dictionary:",flat_dict)

# Q5to insertion at the beginning in OrderedDict
print(dic)
dic['ff']="dd"
print("to add at any end:",dic)
# _____________________________________________________________
d3 = {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
d3['fruits'].insert(0, 'orange')  
print(d3)

# Q6to check order of character in string using OrderedDict()
from collections import OrderedDict

def check_order_of_characters(string):
    # Create an OrderedDict to keep the order of characters
    ordered_dict = OrderedDict.fromkeys(string)
    return list(ordered_dict.keys())
string = "nisha is amazing"
print("Order of characters:", check_order_of_characters(string))


# Q7sort Python Dictionaries by Key or Value
dictionary = {'zpple': 10, 'banana': 5, 'cherry': 7, 'date': 3}
# Sorting by key
sorted_by_key = dict(sorted(dictionary.items()))  
print("Sorted by key:", sorted_by_key)
# converting 2 list into dictionary
l1_keys=[1,2,3,4]
l2_values=["n","p","l","o"]
d=dict(zip(l1_keys,l2_values))
print(d)
# to delete element
del d[4]
print(d)



