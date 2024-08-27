# dictionary methods

# 1) clear() - to clear full dictionary

# d={'name':'anu','age':25,'mark':25}
# d.clear()
# print(d)

# output

# {}

# 2) keys() - to display keys in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.keys())

# output

# dict_keys(['name', 'age', 'mark'])

# 3) values()  -to display values in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.values())

# output

# dict_values(['anu', 25, 25])

# 4) items() - to display items in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.items())

# output

# dict_items([('name', 'anu'), ('age', 25), ('mark', 25)])

# 5) get()- to find values in a dictionary

# d={'name':'anu','age':25,'mark':25}
# print(d.get('name'))

# output

# anu

# 6) pop()- to delete a specific item from a dictionary

# d={'name':'anu','age':25,'mark':25}
# d.pop('name')
# print(d)

# output

# {'age': 25, 'mark': 25}

# 7) popitem- to delete the last item from a dictionary

# d={'name':'anu','age':25,'mark':25}
# d.popitem()
# print(d)

# output

# {'name': 'anu', 'age': 25}

# 8) update()- to update the dictionary

# d={'name':'anu','age':25,'mark':25}
# d.update({'name':'john'})
# print(d)

# output

# {'name': 'john', 'age': 25, 'mark': 25}

# 9) setdefault()-used to create a key with default value

# d={'name':'anu','age':25,'mark':25}
# d.setdefault('place')
# print(d)

# output

# {'name': 'anu', 'age': 25, 'mark': 25, 'place': None}

# 10) fromkeys()-used to create dictionary using list


# d={'name':'anu','age':25,'mark':25}
# l=[1,2,3,4]
# print(d.fromkeys(l))

# output

# {1: None, 2: None, 3: None, 4: None}


# 11) copy()- used to copy items in a dictionary to a new dictionary

# d={'name':'anu','age':25,'mark':25}
# d1=d.copy()
# print(id(d))
# print(id(d1))
# print('d=',d)
# print('d1=',d1)

# output

# d= {'name': 'anu', 'age': 25, 'mark': 25}   id 140527220041152
# d1= {'name': 'anu', 'age': 25, 'mark': 25}  id 140527220041408












