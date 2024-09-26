                            # ecxeption handling

# keywords in exception handling

# 1)try
# 2)except
# 3)else
# 4)finally


# examples
# .............................

# error
# ....................

# print('welcome')
# a='welcome'
# b=20
# print(a+b) - TypeError: can only concatenate str (not "int") to str



# handling this error using exception handling
# ..............................................................


# print('welcome')
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print('an error')


    # output

    # welcome
    # an error



# else and finally keyword
# ...................................


# print('welcome')
# a='welcome'
# b=20
# try:
#     print(a+b)
# except:
#     print('an error')
# else:
#     print('else')
# finally:
#     print('program ends')
# print('sample print')

# output

# welcome
# an error
# program ends
# sample print


# exception handling in a choice based programs example:



# while True:
#     print(
#         '''
#     1)add
#     2)sub
#     3)exit
#     '''
#     )
#     while True:
#         try:
#             choice=int(input("enter a choice"))
#             break
#         except:
#             print('enter choice again')
#     if choice==1:
#         print('add')
#     elif choice==2:
#         print('sub')
#     elif choice==3:
#         break



# sum of a list (exception handling)

# l=[1,2,3,4,5,6.5,'abc']
# s=0
# for i in l:
#     try:
#         s+=i
#     except:
#         pass
# print(s)

# # output

# 21.5


# sum of a list without exception handling


# l=[1,2,3,4,5,6.5,'abc']
# s=0
# for i in l:
#     # print(type(i))
#     if type(i)==int or type(i)==float:
#         s+=i
# print(s)

# # output

# 21.5
    


            


      