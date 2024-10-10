# Database sqlite3
# ........................................

# import sqlite3

# con=sqlite3.connect('student.db')

# try:
#     con.execute('create table std(roll_no int,name text,age int,mark real)')
# except:
#     print('table exist')

# con.execute("insert into std(roll_no,name,age,mark)values(1,'manu',20,100),(2,'jibin',21,95)")
# # con.commit()

# roll=int(input("enter roll_no"))
# name=input("enter name")
# age=int(input("enter age"))
# mark=float(input("enter mark"))
# con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
# con.commit()
# .......................................................................................


# limit=int(input('enter students limit'))
# for i in range(limit):
#     roll=int(input("enter roll_no"))
#     name=input("enter name")
#     age=int(input("enter age"))
#     mark=float(input("enter mark"))
#     con.execute('insert into std(roll_no,name,age,mark)values(?,?,?,?)',(roll,name,age,mark))
#     con.commit()
# .................................................................


# to display items in a table:

# data=con.execute("select * from std")
# for i in data:
#     print(i)

    # output


# (1, 'manu', 20, 100.0)
# (1, 'manu', 20, 100.0)
# (2, 'jibin', 21, 95.0)
# (7, 'samuel', 19, 86.0)
# (10, 'sunil', 22, 99.0)
# (11, 'krishnan', 21, 100.0)
# .................................................................................


# to display a specific field in a table:(name,age,mark,roll_no)


# data=con.execute("select name from std")
# for i in data:
#     print(i)

    # output

    # ('manu',)
    # ('manu',)
    # ('jibin',)
    # ('samuel',)
    # ('sunil',)
    # ('krishnan',
# ...................................................................................



# data=con.execute("select * from std")
# for i in data:
#     print('{:<15}{:<15}{:<15}{:<15}'.format('roll_no','name','age','mark'))
#     print('-'*70)
#     for i in data:
#         print('{:<15}{:<15}{:<15}{:<15}'.format(i[0],i[1],i[2],i[3]))

# output

# roll_no        name           age            mark           
# ----------------------------------------------------------------------
# 1              manu           20             100.0          
# 2              jibin          21             95.0           
# 7              samuel         19             86.0           
# 10             sunil          22             99.0           
# 11             krishnan       21             100.0      

# ......................................................................................................

# example 1:

# data=con.execute("select * from std where name='samuel'")
# for i in data:
#     print(i)

# # output

# (7, 'samuel', 19, 86.0)
  
# example 2:

# data=con.execute("select * from std where roll_no='1'")
# for i in data:
#     print(i)

#     # output

#     (1, 'manu', 20, 100.0)
# ..........................................................................

# method -1


# user=int(input("enter student roll_no"))
# data=con.execute("select * from std where roll_no='1'")
# for i in data:
#     if i[0]==user:
#         print(i)

# method - 2


# user=int(input("enter student roll_no"))
# data=con.execute("select * from std where roll_no=?",(user,))
# for i in data:
#     print(i)

# # output

# enter student roll_no1
# (1, 'manu', 20, 100.0)
# (1, 'manu', 20, 100.0)
# .........................................................................

# to update a value in database:

# con.execute("update std set name ='jinsha' where name='manu'")
# con.commit()


# name=input("enter name")
# new_name=input("enter new name")
# con.execute("update std set name =? where name=?",(new_name,name))
# con.commit()
# .................................................................................


# to delete a value from database:

# con.execute("delete from std where roll_no=1")
# con.commit() 


# user=int(input("enter roll_no to delete"))
# con.execute("delete from std where roll_no=?",(user,))
# con.commit() 
# .......................................................................................


# like(used to display values using first letter,second letter,......,last letter)

# 1)first letter

# data=con.execute("select * from std where name like 'b%'")
# for i in data:
#     print(i)

# # output

# (7, 'bindu', 19, 86.0)

# 2) second letter

# data=con.execute("select * from std where name like '_u%'")
# for i in data:
#     print(i)

#     # output

#     (10, 'sunil', 22, 99.0)

# 3) last letter

# data=con.execute("select * from std where name like '%u'")
# for i in data:
#     print(i)

# # output

# (7, 'bindu', 19, 86.0)
# ...................................................................................................

# order by:(used to display table in assending order)
# desc - is a keyword to convert ascending to decenting order


# 1) ascenting order

# data=con.execute("select * from std order by name")
# for i in data:
#     print(i)

    # output

    # (7, 'bindu', 19, 86.0)
    # (11, 'krishnan', 21, 100.0)
    # (10, 'sunil', 22, 99.0)

# 2) decenting order

# data=con.execute("select * from std order by name desc")
# for i in data:
#     print(i)

# # output

# (10, 'sunil', 22, 99.0)
# (11, 'krishnan', 21, 100.0)
# (7, 'bindu', 19, 86.0
# .....................................................................................

# group by:

# agregate functions in sqlite 3:

# 1) min
# 2) max
# 3) count
# 4) sum
# 5) avg

# 1) maximum mark:

# data=con.execute("select name,max(mark) from std group by name")
# for i in data:
#     print(i)

    # output

# ('bindu', 88.0)
# ('krishnan', 100.0)
# ('sunil', 99.0)








