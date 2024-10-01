# class bank:
#     def __init__(self):
#         self.bal=0
#     def deposit(self,amt):
#         self.bal+=amt
#         print('amount added')
#     def withdraw(self,amt):
#         self.bal-=amt
#         print('amount withdraw')
#     def display(self):
#         print('remaining balace',self.bal)
# user1=bank()
# user1.deposit(25000)
# user1.withdraw(1000)
# user1.display()

# # output user 1

# # amount added
# # amount withdraw
# # remaining balace 24000

# user2=bank()
# user2.deposit(10000)
# user2.withdraw(5000)
# user2.display()

# output user 2

# amount added
# amount withdraw
# remaining balace 5000
# .............................................................................

# sample program using types of arguments


# 1) using positional argument

# class demo:
#     def __init__(self,a):
#         print(a)
# obj=demo(10000)

# 2) using keyword argument

# class demo:
#     def __init__(self,a,b):
#         print(a)
#         print(b)
# obj=demo(a=20,b=35)

# 3 ) using arbitary argument

# class demo:
#     def __init__(self,*a):
#         print(a)
# obj=demo(20,13)

# '''4) Default argument : '''

# class Demo:
#     def __init__(self,name='jibin',amount=2000):
#         print(name,amount)
# obj=Demo('Aswin')
# obj=Demo('Anu',25000)
# obj=Demo(amount=22000)

# output:

# Aswin 2000
# Anu 25000
# jibin 22000

# '''5) Arbitory keyword argument : '''

# class Demo:
#     def __init__(self,**a):
#         print("a=",a)
# obj=Demo(name='jibin',amount=20000)

# output: a= {'name': 'jibin', 'amount': 20000}




