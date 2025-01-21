# generator 
def topten():
 n=1
    # yield 5
    # yield 2
    # yield 3
    # yield 4
 while n<=10:
  sq=n*n
  yield sq
  n +=1
#   here n =3 and square =9 whichis less than 10 but it we take n=4 then squre will be 16 will not satisfy the condition so it break at 3
  print("n:",n)
values=topten()
print(values)

print(values.__next__())
print(values.__next__())
print(values.__next__())