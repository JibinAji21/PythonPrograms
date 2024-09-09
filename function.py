                                    # function
                                # ...................


#       function- function is a block of code
#       def function name (): - to create a function



# def fun1():
#     print("hi")
#     print("hello")
#     print("welcome")
#     print("python")

# print(10+5)
# fun1()
# print(10-5)
# fun1()
# print(10*2)
# fun1()

# output

# 15
# hi
# hello
# welcome
# python
# 5
# hi
# hello
# welcome
# python
# 20
# hi
# hello
# welcome
# python

# .....................................................

# scope of a variable 
# ......................................


#1) local variable - it is created inside a fuction . so works only inside the function.

#2) global variable - it is created outside the function. so it can be used anywhere in the program.



# def fun():
#     a=10   - (local variable)
#     print("a=",a)
#     print("b inside =",b)

# b=20     - (global variable)
# print("b outside=",b)
# fun()

# # output

# b outside= 20
# a= 10
# b inside = 20

# .................................................


# how to create a global variable inside a function (by using a keyword 'global')

# def fun1():
#     global a
#     a=10
#     print('outside a=',a)
# fun1()

# # output

# outside a= 10
# ........................................................................

# return (to return value from a function)

# def fun():
#     return 'welcome',10,20

# a,b,c=fun()
# print(a)
# print(b)
# print(c)

# output

# welcome
# 10
# 20
# ...........................................................................

# local variables can be accessed outside  using return keyword

# def fun1():
#     a=10
#     b=11
#     c=12
#     return a,b,c
# a1,a2,a3=fun1()
# print("a=",a1)
# print("b=",a2)
# print("c=",a3)

# # output

# a= 10
# b= 11
# c= 12






