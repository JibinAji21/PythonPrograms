# # student management using list

# student=[]
# while True:
#     print(
#         '''
#     1.Add
#     2.View
#     3.Update
#     4.Delete
#     5.Exit
#     '''
#     )
#     choice=int(input("enter your choice"))
#     if choice==1:
#         name=input("enter name")
#         age=int(input("enter age"))
#         mark=int(input("enter mark"))
#         student.append([name,age,mark])
#     elif choice==2:
#         print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
#         print('-'*25)
#         for i in student:
#             print('{:<10}{:<8}{:<8}'.format(i[0],i[1],i[2]))
#     elif choice==3:
#         name=input("enter name")
#         f=0
#         for i in student:
#             if name in i:
#                 new_mark=int(input("enter new mark"))
#                 i[2]=new_mark
#                 f=1
#         if f==0:
#             print("name not in list")
#     elif choice==4:
#         name=input("enter name")
#         f=0
#         for i in student:
#             if name in i:
#                 student.remove(i)
#                 f=1
#             print("name not in list")
#     elif choice==5:
#         break
#     else:
#         print("invalid choice")
        

            