import mysql.connector
con=mysql.connector.connect(host='localhost',user='batch11',password='batch11',database='batch11datas')
con.autocommit=True
cur=con.cursor()
# cur.execute('create database batch11datas')   - used tocreate database
# cur.execute('create table student (roll_no int,name text,age int)')   - used to create table in a database
# # cur.execute('insert into student (roll_no,name,age) values(1,"sam",22)')  - used to inserting values in a database
# roll_no=int(input("enter roll_no :"))
# name=input("enter student name :")
# age=int(input("enter student age :"))
# cur.execute('insert into student (roll_no,name,age) values(%s,%s,%s)',(roll_no,name,age))

# cur.execute("select * from student") #- to display details
# data=cur.fetchall()
# for i in data:
#     print(i)

# cur.execute("update student set name='jobin' where name='sam'") -  used to update a value in database

old_name=input("enter old name")
new_name=input("enter new name")
cur.execute("update student set name =%s where name=%s",(new_name,old_name))




