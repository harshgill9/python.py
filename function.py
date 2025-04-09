# def printmyname():
#     print("amit")
# printmyname()

# def printmyname(full_name):
#     print(full_name)
# printmyname("full_name")

# def sum(a,b):
#     print(a+b)
# sum(2,5)

# def greet(name,message = "Hello"):
#     print(message +","+ name)
# greet("Harsh")
# greet("Harsh","Best of luck")


# def sum(a,b=10):
#     return a+b
#     # print(a*b)
#     # print(a+b)
# xyz=sum(2)
# print(xyz)


# def total_number(*params):
#     print(sum(params))
# total_number(1,2,3,4,5)

# y=50
# def local_scope():
#     print(y)
# local_scope()
# print(y)


# def local_scope():
#     y=50
#     print(y)
    
# local_scope()
# print(y)


count=0
def increment():
    global count
    count+=1
increment()  
print(count)
increment() 
print(count)
