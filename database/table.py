# Database sqlite3
# ........................................

import sqlite3

con=sqlite3.connect('student.db')

try:
    con.execute('create table std(roll_no int,name text,age int,mark real)')
except:
    print('table exist')

con.execute("insert into std(roll_no,name,age,mark)values(1,'manu',20,100),(2,'jibin',21,95)")
con.commit()