# f=open('PythonPrograms/filehandling/demo.txt','a')
# f.write('welcome to all')
# f.write('hope you all are fine')
# print(f.read())
# a=f.read(5)
# f.seek(0)
# b=f.read()
# print(f.tell())
# print(a)
# print('_'*20)
# print(b)
# a=f.readline(5)
# b=f.readline()
# c=f.readlines()
# # print(a)
# # print(b)
# print(c)

#reverse of a string 

# d=f.readlines()
# f.seek(0)
# for i in range(len(d)):
#     a=f.readline().strip()
#     # print(a)
#     print(a[::-1])

# f.write('bad time\n')
# f.write('aaaaaaaaaaaaaaa')


# f=open('PythonPrograms/filehandling/demo.txt','r')
# d=f.readlines()
# f.seek(0)
# letter=0
# for i in range(len(d)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             letter+=1
# print(letter)

# output :13




# f=open('PythonPrograms/filehandling/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 cap+=1
#             letter+=1
# print('total no of letter',letter)
# print('total capital letters',cap)
# print('total small letters',letter-cap)

# # output

# total no of letter 13
# total capital letters 1
# total small letters 12



# f=open('PythonPrograms/filehandling/demo.txt','r')
# l=f.readlines()
# f.seek(0)
# letter=0
# cap=0
# words=0
# for i in range(len(l)):
#     a=f.readline().strip()
#     s=a.split(' ')
#     for i in s:
#         if i!='':
#             words+=1
#     for i in a:
#         if i !=' ':
#             if i.isupper():
#                 cap+=1
#                 letter+=1
# print('total no of letter',letter)
# print('total capital letters',cap)
# print('total small letters',letter-cap)
# print(words)

  

    
        
