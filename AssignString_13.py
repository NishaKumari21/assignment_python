'''1. Write a Python program to find words which are greater than given length k?
2. Write a Python program for removing i-th character from a string?
3. Write a Python program to split and join a string?
4. Write a Python to check if a given string is binary string or not?
5. Write a Python program to find uncommon words from two Strings?
6. Write a Python to find all duplicate characters in string?
7. Write a Python Program to check if a string contains any special character?'''
# Q1to find words which are greater than given length k
string="this is a cat which fightsppp with dog always."
k=5
p=(len(string))
print("length or the string:",p)
words=string.split(' ')
for i in words:
    print(i)
    print(len(i))
    if(len(i)>k):
        print("word greater than length k:",i)
        # ----------------------------------
# Q2 for removing i-th character from a string
string="myself nisha ,i want to become data scientist"
i=input("enter the string you want to remove")
print("element to be removed:",i)
p=[string.find(i)]
print( f"{i} is found at {p}")
string=string.replace(i,"")
print("after removing element:",string)
#3program to split and join a string
s1="this is 1st string"
s2="this is 2nd string"
s3=s1 + " " +s2
print(s3)
#  or use join 
s4= " ".join([s1, s2])
print(s4)
split_s=s4.split(" ")
print(split_s)
# Q4to check if a given string is binary string or not
string = "10101010"
s2 = "345678"
if all(char == '0' or char == '1' for char in string):  # Check if all characters are '0' or '1'
    print("binary string")
else:
    print("not binary string")
# Q5to find uncommon words from two Strings
s1 = "this is cat"
s2 = "this is a dog"

def check(s1, s2):
    w1 = s1.split()
    w2 = s2.split()
    print("after splitting s1:",w1)
    print("after splitting s2:",w2)
    # Find uncommon words by using set operations
    # here we converted w1 and w2 to set because set stored the unique value only and
    # symmetric_differemce:This is a set operation that returns elements that are unique to each set (i.e., elements that are in either set but not in both
    uncommon_words = set(w1).symmetric_difference(set(w2))
    # Return the uncommon words as a list
    return list(uncommon_words)

print(check(s1, s2))
# Q6 find all duplicate characters in string
s="this is  great to see you all here because it is raining this day"
d=s.split(" ")
print(d)
for i in d:
    print(i)
    if s.count(i)>1:
      print(f"{i}: is duplicate")
#   Q7to check if a string contains any special character
import string
p=string.punctuation
print("punctuation are:",p)
s="amazing to see you all @xyz here!"
for i in s:
    print(i)
    if i in p:
        print(f"{i} is a special character")