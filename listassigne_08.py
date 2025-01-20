'''1.Write a Python program to find sum of elements in list?
2. Write a Python program to Multiply all numbers in the list?
3. Write a Python program to find smallest number in a list?
4. Write a Python program to find largest number in a list?
5. Write a Python program to find second largest number in a list?
6. Write a Python program to find N largest elements from a list?
7. Write a Python program to print even numbers in a list?
8. Write a Python program to print odd numbers in a List?
9. Write a Python program to Remove empty List from List?
10. Write a Python program to Cloning or Copying a list?
11. Write a Python program to Count occurrences of an element in a list?'''
# Q1find sum of elements in list
l=[3,4,5,67,7]
print(sum(l))
# Q2.to Multiply all numbers in the list
l=[3,41,5,6,7]
for i in l:
    print(i)
print("multiplication:",l)
# Q3to find smallest number in a list
l=[4,5,6,72,3]
print(min(l))
#Q4to find largest number in a list
m=max(l)
print(m)
# Q5to find second largest number in a list
a=sorted(l)
print("sorted list:",a)
print("second maxiumn number is:",a[-2])
#Q6to find N largest elements from a list
print(l.count(m))
# Q7to print even numbers in a list
l=[3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
    
        print("even elements are:",i)
# Q8to print odd numbers in a List
l=[3,45,7,78,2,4]
for i in l:
    if i%2!=0:
        print("odd numbers are:",i)
# Q9to Remove empty List from List
l=[[2,3,4],['j','k','l'],[]]
for i in l:
    print(i)
    if i==[]:
        print("empty list is:",i)
        l.remove(i)
        print("after removing empty list:",l)
# # Q10to Cloning or Copying a list
l=[4,5,6,'j',"nisha"]     
print("list 1 is :",l) 
l2=l.copy()
print("copied list is:",l2)
# Q11to Count occurrences of an element in a list
l=[2,2,3,33,2,4]
print("count of 2:",l.count(2))
