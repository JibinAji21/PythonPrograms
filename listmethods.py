# value adding methods

# 1) append:

# l=[]
# l.append(5)
# l.append(10)
# l.append(20)
# l.append('abc')
# l.append([10,11,12])
# print(l)

# output

# [5, 10, 20, 'abc', [10, 11, 12]]

# 2) extend:


# l=[]
# l.append(5)
# l.append(10)
# l.append(20)
# l.append('abc')
# l.append([10,11,12])
# l.extend([3,4,5])
# print(l)

# output

# [5, 10, 20, 'abc', [10, 11, 12], 3, 4, 5]


# 3) insert:

# l=[]
# l.append(5)
# l.append(10)
# l.append(20)
# l.append('abc')
# l.append([10,11,12])
# l.extend([3,4,5])
# l.insert(2,"hy")
# print(l)

# outout

# [5, 10, 'hy', 20, 'abc', [10, 11, 12], 3, 4, 5]


# value removing methods

# 1) clear

# l=[10,20,30,'abc']
# l.clear()
# print(l)

# output

# []
# empty list all values will be cleared

# 2) pop

# l=[10,20,30,'abc']
# l.pop()
# print(l)

# output

# [10, 20, 30]

# example 2)

# l=[10,20,30,'abc']
# l.pop(2)
# print(l)

# output

# [10, 20, 'abc']


# 3) remove

# l=[10,20,30,'abc']
# l.remove(10)
# print(l)

# output

# [20, 30, 'abc']



# sort


# l=[10,355,5]
# l.sort()
# print(l)

# output

# [5, 10, 355]

# reverse

# l=[10,15,500,300]
# l.reverse()
# print(l)

# output

# [300, 500, 15, 10]


# index

# l=[10,15,'a',20]
# print(l.index('a'))

# output

# 2


# count

# l=[10,11,12,13,14]
# print(l.count(14))

# output

# 1

# copy

# l=[1,2,3,4]
# l1=l.copy()
# print(id(l))
# print(id(l1))
# print('l=',l)
# print('l1',l1)

# output

# l= [1, 2, 3, 4] id= 139875829909248
# l1 [1, 2, 3, 4] id= 139875827813824












