a="welcome"
print(a)
print(a[0])
print(a[4])
print(a[-2])
print(a[1:3])
print(a[-5:-1])
print(a[:5])
print(a[-1:])

print(a[:])
print(a[::2])
print(a[::-1])

#methods of string

print(a.capitalize())
print(a.center(15))
print(a.count('e'))
print(a.endswith('c'))
print(a.endswith('e'))

print(a.find('e'))
print(a.find('l'))
print(a.find('n'))

print(a.index('e'))
#print(a.index('f'))

print(a.isdigit())
b="12345"
print(b.isdigit())

print(a.islower())
c="WELCOME"
print(c.islower())
print(c.isupper())
print(a.upper())
print(c.lower())

d="          happy to see            "
print(d.split())

print(d.strip())
print(d.lstrip())
print(d.rstrip())

print("{:<10}{:<8}{:<8}" .format ("name", "age", "mark"))
print("{:<10}{:<8}{:<8}" .format("anu", "22", "45"))
print("{:<10}{:<8}{:<8}" .format("sam", "22", "42"))


