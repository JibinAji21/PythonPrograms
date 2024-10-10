# import re
# a='abcd'
# print(re.search('a',a))

# output - # <re.Match object; span=(0, 1), match='a'>

# print(re.search('abcd',a))
# output - <re.Match object; span=(0, 4), match='abcd'>

# print(re.search('s',a))
# output - None

# example 1 :

# if re.search('s',a):
#     print("match")
# else:
#     print('not')

# output - not

# example 2 :

# if re.search('a',a):
#     print("match")
# else:
#     print('not')

# output - match


# using . - represents a single character
# .....................................................

# example:

# 1) print(re.search('a.',a))
# output - <re.Match object; span=(0, 2), match='ab'>

# 2) print(re.search('b.',a))
# output - <re.Match object; span=(1, 3), match='bc'>

# 3) print(re.search('c.',a))
# output - <re.Match object; span=(2, 4), match='cd'>

# 4) print(re.search('d.',a))
# output - None

# using ..
# ..........................................................

# 1) print(re.search('a..',a))
# output - <re.Match object; span=(0, 3), match='abc'>

# 2) print(re.search('b..',a))
# output - <re.Match object; span=(1, 4), match='bcd'>


# using * - represents zero or more occurence
# .................................................................

# example :

# 1) print(re.search('a.*',a))
# output - <re.Match object; span=(0, 4), match='abcd'>

# 2) print(re.search('b.*',a))
# output - <re.Match object; span=(1, 4), match='bcd'>


# 3) print(re.search('c.*',a))
# output - <re.Match object; span=(2, 4), match='cd'>

# 4) print(re.search('d.*',a))
# output - <re.Match object; span=(3, 4), match='d'>


# using + - one or more occurence 
# ....................................................................

# 1) print(re.search('c.+',a))
# output - <re.Match object; span=(2, 4), match='cd'>

# 2) print(re.search('b.+',a))
# output -<re.Match object; span=(1, 4), match='bcd'>

# 3) print(re.search('a.+',a))
# output - <re.Match object; span=(0, 4), match='abcd'>


# using ? - zero or one occurence
# ........................................................................

# 1) print(re.search('a.?',a))
# output - <re.Match object; span=(0, 2), match='ab'>

# 2) print(re.search('b.?',a))
# output - <re.Match object; span=(1, 3), match='bc'>

# 3) print(re.search('c.?',a))
# output - <re.Match object; span=(2, 4), match='cd'>

# 4) print(re.search('d.?',a))
# output - <re.Match object; span=(3, 4), match='d'>


# using [] - represents only one value
# ............................................................


# example 1:


#  print(re.search('[abcd]',a))
# # output - <re.Match object; span=(0, 1), match='a'>

# example 2:

# a='ABCD'

# 1) print(re.search('[a-z]',a))
# output - None

# 2) print(re.search('[A-Z]',a))
# output - <re.Match object; span=(0, 1), match='A'>

# 3) print(re.search('[A-z]',a))
# output - <re.Match object; span=(0, 1), match='A'>


# example 3:

# a='ABCDefg'

# print(re.search('[A-z]',a))
# output - <re.Match object; span=(0, 1), match='A'>

# example 4:

# a='abABCDefg'

# print(re.search('[A-z]',a))
# output - <re.Match object; span=(0, 1), match='a'>

# print(re.search('[A-M]',a))
# output - <re.Match object; span=(2, 3), match='A'>

# print(re.search('[m-z]',a))
# output - None

# example 5:

# a='1234'

# print(re.search('[0-9]',a))
# output - <re.Match object; span=(0, 1), match='1'>

# print(re.search('[6-9]',a))
# output - None


# example 6 :

# a='abc123'

# print(re.search('[a-z][0-9]',a))
# output - <re.Match object; span=(2, 4), match='c1'>



# a='abcd'

# print(re.search('[a-z][0-9]',a))
# output - None


# a='123456'

# # print(re.search('[a-z][0-9]',a))
# # output - None

# print(re.search('[a-z0-9]',a))
# output - <re.Match object; span=(0, 1), match='1'>

# a='abcdef12345'

# # print(re.search('[a-z].*[0-9]',a))
# # output - <re.Match object; span=(0, 11), match='abcdef12345'>

# print(re.search('[a-z0-9]',a))
# output - <re.Match object; span=(0, 1), match='a'>


# a='abcd1'

# print(re.search('[a-z].*[0-9]',a))
# output - <re.Match object; span=(0, 5), match='abcd1'>

# print(re.search('[a-z].+[0-9]',a))
# output - <re.Match object; span=(0, 5), match='abcd1'>

# print(re.search('[a-z].?[0-9]',a))
# output - <re.Match object; span=(2, 5), match='cd1'>

# print(re.search('[a-z].?[0-9].*',a))
# output - <re.Match object; span=(2, 5), match='cd1'>

# print(re.search('[a-z].?[0-9].+',a))
# output - None

# print(re.search('[a-z].?[0-9].?',a))
# output - <re.Match object; span=(2, 5), match='cd1'>









