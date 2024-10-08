import sqlite3
con=sqlite3.connect('std.db')
try:
    con.execute('create table std_details(roll_no int,name text,age int)')
except:
    print('table exist')

# con.execute("insert into std_details(roll_no,name,age)values(1,'manu',20),(2,'jibin',21),(3,'sam',25)")
# con.commit()


try:
    con.execute('create table mark_dtls(roll_no int,sub text,mark real)')
except:
    print('table exist')

# con.execute("insert into mark_dtls(roll_no,sub,mark)values(1,'python',40),(2,'php',45),(3,'maths',25),(1,'php',52)")
# con.commit()

# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark_dtls.sub,mark_dtls.mark from std_details join mark_dtls on std_details.roll_no=mark_dtls.roll_no")
# for i in data:
#     print(i)

    # output

    # (1, 'manu', 20, 'php', 52.0)
    # (1, 'manu', 20, 'python', 40.0)
    # (2, 'jibin', 21, 'php', 45.0)
    # (3, 'sam', 25, 'maths', 25.0)

# 1) left join:


# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark_dtls.sub,mark_dtls.mark from std_details left join mark_dtls on std_details.roll_no=mark_dtls.roll_no")
# for i in data:
#     print(i)

#     # output

#     (1, 'manu', 20, 'php', 52.0)
#     (1, 'manu', 20, 'python', 40.0)
#     (2, 'jibin', 21, 'php', 45.0)
#     (3, 'sam', 25, 'maths', 25.0)

# 2) Right join:(not supported in this system so we use left join and swap the tables)


# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark_dtls.sub,mark_dtls.mark from mark_dtls left join std_details on std_details.roll_no=mark_dtls.roll_no")
# for i in data:
#     print(i)

# output

# (1, 'manu', 20, 'python', 40.0)
# (2, 'jibin', 21, 'php', 45.0)
# (3, 'sam', 25, 'maths', 25.0)
# (1, 'manu', 20, 'php', 52.0)
# (None, None, None, 'java', 49.0)


# 3) cross join:


# data=con.execute("select std_details.roll_no,std_details.name,std_details.age,mark_dtls.sub,mark_dtls.mark from mark_dtls cross join std_details")
# for i in data:
#     print(i)

    # output

    # (1, 'manu', 20, 'python', 40.0)
    # (2, 'jibin', 21, 'python', 40.0)
    # (3, 'sam', 25, 'python', 40.0)
    # (1, 'manu', 20, 'php', 45.0)
    # (2, 'jibin', 21, 'php', 45.0)
    # (3, 'sam', 25, 'php', 45.0)
    # (1, 'manu', 20, 'maths', 25.0)
    # (2, 'jibin', 21, 'maths', 25.0)
    # (3, 'sam', 25, 'maths', 25.0)
    # (1, 'manu', 20, 'php', 52.0)
    # (2, 'jibin', 21, 'php', 52.0)
    # (3, 'sam', 25, 'php', 52.0)
    # (1, 'manu', 20, 'java', 49.0)
    # (2, 'jibin', 21, 'java', 49.0)
    # (3, 'sam', 25, 'java', 49.0)

    
    

