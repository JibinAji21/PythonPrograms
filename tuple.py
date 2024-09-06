# tuple..............
# t=(1,2,3,'abc',5.8)

# empty tuple............
# t=()

# iterating a tuple.............................

# t=(1,2,3,'abc',5.8)
# for i in t:
#     print(i)

# output

# 1
# 2
# 3
# abc
# 5.8

# checking a value is present on the tuple.....................

# t=(1,2,3,'abc',5.8)
# if 2 in t:
#     print('true')
# else:
#     print('false')

# output 1

# true

# t=(1,2,3,'abc',5.8)
# if 9 in t:
#     print('true')
# else:
#     print('false')

# output 2

# false

# index position................

# t=(1,2,3,'abc',5.8)
# print(t[2])

# output 
    # 3

# features of tuple................

# 1) it is still considered as a tuple we skip the round brackets...............

# t=1,2,3,4
# print(t)

# # output
# (1, 2, 3, 4)

# 2) it is a tuple because coma is used......................

# t1=10,

# 3) this is an interger data type because coma is not used.................................

# t2=(10)

# 4) single value tuple...............................

# t2=(10,)

# 5)updating values on a list inside a tuple (we can edit the values on list bcoz list is mutable )

# t=(1,2,[10,11])
# print(t[2])
# t[2].append(12)
# print(t)

# # output
# (1, 2, [10, 11, 12])

# 6)we cant update values on atuple inside a list(becoz tuple is inmutable)

# l=[1,2,(10,11)]

# ................................................................................................................................
  
# updating valuses in tuple using type casting

# t=(1,2,3,4)
# l=list(t)  ..... converting tuple to list [1, 2, 3, 4]
# l.pop().....doing operation [1, 2, 3]
# t=tuple(l)......converts back to tuple (1, 2, 3)
# print(t)

# output

# (1, 2, 3)

# converting dictionary to list 

# d={'name':'anu'}
# l=list(d)
# print(l)

# output

# ['name']








