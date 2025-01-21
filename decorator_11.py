# decorator are usef to add more functionality and features to the existing function

# here decorator means no matter in which order we pass the function argmnets but we want the answer same and everytime the b should be greater ie denominator
# def div(a,b):
#     if a<b:
#         a,b=b,a
#     print(a/b)
# div(2,4)
# 2.0
# we can do likhe this also but we can use decorator and make this work properly like this without doing anything inside code

def div(a,b):
   return a/b
def smart_div(func):
    def inner(a,b):
     if a<b:
        a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
print(div1(2,4))
# 2.0
# 0.5
print(div(2,4))
