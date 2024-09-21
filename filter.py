# 1)even numbers of a list(normal method)

# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     if i%2==0:
#         print(i)

# 2) using filter function()

# l=[1,2,3,4,5,6,7,8]
# data=filter(lambda x:x%2==0,l)
# print(list(data))

# output

# [2, 4, 6, 8]

# 3) single line method()

# l=[1,2,3,4,5,6,7,8]
# print(list(filter(lambda x:x%2==0,l)))

# # output

# [2, 4, 6, 8]

# 4) even number using user defined function

# l=[1,2,3,4,5,6,7,8]
# def fun(x):
#     return x%2==0
# print(list(filter(fun,l)))

# # output

# [2, 4, 6, 8]



# 5)using filter method in string

# l=['apple','orange','kiwi']
# print(list(filter(lambda x:'a' in x,l)))

# # output

# ['apple', 'orange']

# 6) using user defined function

# l=['apple','orange','kiwi']

# def fun(x):
#     return 'a' in x
# print(list(filter(fun,l)))

# # output

# ['apple', 'orange']

#7) odd numbers using filter function

# l=[1,2,3,4,5,6,7,8]
# data=filter(lambda x:x%2==1,l)
# print(list(data))

# # output

# [1, 3, 5, 7]

# 8) odd numbers using user defined function

# l=[1,2,3,4,5,6,7,8]
# def fun(x):
#     return x%2==1
# print(list(filter(fun,l)))

# # output

# [1, 3, 5, 7]



