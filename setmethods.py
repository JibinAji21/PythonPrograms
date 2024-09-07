                                # set methods


# 1) s.add() - to add a single value to a set

# s={1,2,3,4}
# s.add(6)
# print(s)

# output

# {1, 2, 3, 4, 6}

# 2) s.clear() - to fully  clear a set

# s={1,2,3,4}
# s.clear()
# print(s)

# output

# set()

# 3) s.copy() - to copy a set

# s={1,2,3,4}
# s1=s.copy()
# print('s=',s)
# print('s1=',s1)

# # output

# s= {1, 2, 3, 4}
# s1= {1, 2, 3, 4}

# 4) s.difference() - to find the difference between two sets

# s={10,1,2,3}
# s1={1,10,5,6}
# s.difference(s1)
# print(s)

# output


# 5) s.discard() - to delete a specific value from the set

# s={1,2,3,4}
# s.discard(3)
# print(s)

# # output

# {1, 2, 4}

#  6) s.remove()- to delete a specific value from the set (it shows error)


# s={1,2,3,4}
# s.remove(3)
# print(s)

# # output

# {1, 2, 4}

# 7) s.pop() - to delete a value from the set

# s={1,2,3,4}
# s.pop()
# print(s)

# # output

# {2, 3, 4}

# 8) s.update() - to update values in a set

# s={1,2,3,4,5,6}
# s.update({10})
# print(s)

# # output

# {1, 2, 3, 4, 5, 6, 10}

# 9) s.intersection() - used to display commom values of two sets

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print(s.intersection(s1))

# # output

# {1, 2, 3}

# 10) s.union() 

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print(s.union(s1))

# # output

# {1, 2, 3, 4, 5, 6, 7}

# 11) s.isdisjoint()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print((s.isdisjoint(s1)))

# # output

# False

# 12) s.issubset()

# s={1,2,3,4,5}
# s1={1,2,3}
# print((s1.issubset(s)))

# # output

#    True

# 13) s.issuperset()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print(s.issuperset(s1))

# # output 

# False

# 14) s.symmetric_difference()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# print(s.symmetric_difference(s1))

# # output

# {4, 5, 6, 7}

# 15) s.difference_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.difference_update(s1)
# print("s=",s)

# # output

# s= {4, 5}

# 16) s.intersection_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.intersection_update(s1)
# print("s=",s)

# # output

# s= {1, 2, 3}

# 17) s.symmetric_difference_update()

# s={1,2,3,4,5}
# s1={1,2,3,6,7}
# s.symmetric_difference_update(s1)
# print("s=",s)

# # output

# s= {4, 5, 6, 7}









