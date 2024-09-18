# Types of arguments

# 1)Positional Argument
# 2)Function With Keyword Argument
# 3)Default Argument
# 4)Arbitray Argument
# 5)Arbitary Keyword Argument


# 1) positional argument example
# ...........................................

# def dtls(name,age):
#     print("name=",name)
#     print("age=",age)

# dtls("anu",20)
# dtls("manu",22)
# dtls(22,"abhi")

# output

# name= anu
# age= 20
# name= manu
# age= 22
# name= 22
# age= abhi
# ................................................

# 2) Function with keyword argument example


# def dtls(name,age):
#     print("name=",name)
#     print("age=",age)

# dtls(age=22,name="jomon")

# # output

# # name= jomon
# # age= 22
# .....................................................

# 3) Default Argument

# def sample(name='abc',age=20):
#     print(name,age)
# sample('manu',)

# # output

# manu 20
# .......................................................

# 4) Arbitary Argument

# def sample(b,*a):
#     print(b,a)
    
# sample(10)
# sample(1,2,3)
# sample(1,2,3,3,2)

# output

# 10 ()
# 1 (2, 3)
# 1 (2, 3, 3, 2)
# ................................................................


# 5) Arbitary Keyword Argument

# def sample(**a):
#     print(a)
# sample(name='anu',age=20)
# sample(name='anu',age=20,name1='anu',age1=20)

# # output

# {'name': 'anu', 'age': 20}
# {'name': 'anu', 'age': 20, 'name1': 'anu', 'age1': 20}


