# import sqlite3
# con=sqlite3.connect('employee.db')
# try:
#     con.execute("create table emp(id int,name text,age int,place text,post text,phone int)")
# except:
#     print("table already exist")

#     while True:
#         print(
#             '''
#             1.Add Employee
#             2.View Employee
#             3.Update Employee
#             4.Delete Employee
#             5.Search Employee
#             6.Exit
#         '''
#         )
#         choice=int(input("enter your choice"))
#         if choice==1:
#             id=int(input("enter employee id"))
#             name=input("enter employee name")
#             age=int(input("enter employee age"))
#             place=(input("enter employee place"))
#             post=input("enter employee post")
#             phone=int(input("enter employee phone no"))
#             con.execute('insert into emp(id,name,age,place,post,phone)values(?,?,?,?,?,?)',(id,name,age,place,post,phone))
#             con.commit()
#         elif choice==2:
#             data=con.execute("select * from emp")
#             for i in data:
#                 print('{:<15}{:<15}{:<15}{:<15}{:15}{:15}'.format('id','name','age','place','post','phone'))
#                 print('-'*70)
#                 for i in data:
#                     print('{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
#         elif choice==3:
#             while True:
#                 print(
#                     '''
#                     1.Update Employee Name
#                     2.Update Employee Age
#                     3.Update Employee place
#                     4.Update Employee Post
#                     5.Update Employee Phone no
#                     6.Exit
#                 '''
#                 )
#                 sub_choice=int(input("enter your choice"))
#                 if sub_choice==1:
#                     name=input("enter current name")
#                     new_name=input("enter new name")
#                     con.execute("update emp set name =? where name=?",(new_name,name))
#                     con.commit()
#                 elif sub_choice==2:
#                     age=input("enter current age")
#                     new_age=input("enter new age")
#                     con.execute("update emp set age =? where age=?",(new_age,age))
#                     con.commit()
#                 elif sub_choice==3:
#                     place=input("enter current place")
#                     new_place=input("enter new place")
#                     con.execute("update emp set place =? where place=?",(new_place,place))
#                     con.commit()
#                 elif sub_choice==4:
#                     post=input("enter current post")
#                     new_post=input("enter new post")
#                     con.execute("update emp set post =? where post=?",(new_post,post))
#                     con.commit()
#                 elif sub_choice==5:
#                     phone=input("enter current phone")
#                     new_phone=input("enter new phone")
#                     con.execute("update emp set phone =? where phone=?",(new_phone,phone))
#                     con.commit()
#                 elif sub_choice==6:
#                     break
#         elif choice==4:
#             user=int(input("enter id to delete"))
#             con.execute("delete from emp where id =?",(user,))
#             con.commit()
#         elif choice==5:
#              user=int(input("enter id"))
#              data=con.execute("select * from emp where id=?",(user,))
#              for i in data:
#                  print(i)
#         elif choice==6:
#             break
            



                    

                

                




