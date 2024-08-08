#operators
#1)arithmatic operators

#addition
print(10+5)
print("sam"+"sunu")

#substraction

print(10-5)

#multiplication

print(2*10)
print("sun"*5)

#modulus

print(10%2)
#division

print(10/2)

#floor division

print(10//5)

#exponent

print(10**3)
print(2**2)

#2)assignment operators

#=

a=10
print(a)

#+=

a=10
a+=5
print(a)

#-=

a=10
a-=5
print(a)

#*=

a=10
a*=3
print(a)

#/=

a=10
a/=5
print(a)

#%=

a=10
a%=5
print(a)

#//=

a=10
a//=5
print(a)

#**=

a=10
a**=5
print(a)

#3)comparison operators

#==
print(20==20)
print(10==5)

#!=
print(10!=9)
print(10!=10)

#>
print(10>9)
print(10>11)

#<list=[10,30,50]
print(10<9)
print(9<10)

#>=
print(10>=10)
print(9>=10)

#<=
print(10<=10)
print(11<=10)

#4)logical operators

#and
print(10==10 and 5==5)
print(10==10 and 10==11)
print(10==11 and 10==10)
print(10==11 and 21==10)

#or

print(10==10 or 20==20)
print(10==10 or 20<=10)
print(10==12 or 20==20)
print(10==12 or 10==20)

#not

print(not(10==10))
print(not(10==11))

#5)Membership operator

#in
print("e" in "welcome")
print("e" in "wlcom")
list=[10,30,50]
print(10 in list)

#not in
print("f" not in "finish")
print("g" not in "finish")
list=[10,30,25]
print(25 not in list)

#6) Identity operator

#is
a=10
b=10
print(a is b)
print(id(a))
print(id(b))

a=5
b=10
print(a is b)
print(id(a))
print(id(b))

list=[10,20,30]
list1=[10,20,30]
print(list is list1)
print(id(list))
print(id(list1))

#is not
a=10
b=10
print(a is not b)
print(id(a))
print(id(b))

a=5
b=10
print(a is not b)

list=[11,12,13]
list1=[11,12,13]
print(list is not list1)







