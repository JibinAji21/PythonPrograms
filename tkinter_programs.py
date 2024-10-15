import sqlite3
import tkinter

# win=tkinter.Tk()
# win.title("batch11")
# win.maxsize(500,500)
# win.minsize(250,250)
# win.configure(bg="red")

# def save():
#     l2.config(text=e1.get())

# l1=tkinter.Label(win,text="welcome to the show",bg="black",fg="red")
# l1.pack()

# e1=tkinter.Entry(win)
# e1.pack()

# b1=tkinter.Button(win,text="save",bg="black",activebackground="black",fg="red",activeforeground="blue",padx=10,pady=6,command=save)
# b1.pack()

# l2=tkinter.Label(win)
# l2.pack()


# win.mainloop()

# example work tkinter:

win=tkinter.Tk()
win.title("login page")
win.maxsize(500,500)
win.minsize(500,500)
win.configure(bg="skyblue")

def reg_form():
    win1=tkinter.Tk()
    win1.title("Registration form")
    win1.maxsize(500,500)
    win1.minsize(500,500)
    win1.configure(bg="skyblue")
    def reg():
        con=sqlite3.connect("tki.db")
        # con.execute("create table user(uname text, password text)")
        con.execute('insert into user(uname,password)values(?,?)',(e1.get(),e2.get()))
        con.commit()
        win1.destroy()
        # print(e1.get(),e2.get())   #----> to display output in terminal

    l1=tkinter.Label(win1,text="Registration",bg="skyblue",fg="black")
    l1.place(x=150,y=10)
    l2=tkinter.Label(win1,text="Username",bg="skyblue",fg="black")
    l2.place(x=80,y=40)
    e1=tkinter.Entry(win1)
    e1.place(x=200,y=40)
    l3=tkinter.Label(win1,text="password",bg="skyblue",fg="black")
    l3.place(x=80,y=70)
    e2=tkinter.Entry(win1)
    e2.place(x=200,y=70)
    b2=tkinter.Button(win1,text="register",bg="black",activebackground="black",fg="white",activeforeground="blue",padx=10,pady=6,command=reg)
    b2.place(x=250,y=100)

    win1.mainloop()

def home():
    win2=tkinter.Tk()
    l1=tkinter.Label(win2,text="Homepage")
    l1.pack()
    b1=tkinter.Button(win2,text="signout",command=win2.quit)
    b1.pack()
    win2.mainloop()

def login():
    con=sqlite3.connect("tki.db")
    data=con.execute("select * from user where uname=? and password =?",(e1.get(),e2.get()))
    f=0
    for i in  data:
        f=1
        home()
    if f==0:
        l4.config(text="inavlid uname or password")

l1=tkinter.Label(win,text="Welcome",bg="skyblue",fg="black")
l1.place(x=150,y=10)
l2=tkinter.Label(win,text="Username",bg="skyblue",fg="black")
l2.place(x=80,y=40)
e1=tkinter.Entry(win)
e1.place(x=200,y=40)
l3=tkinter.Label(win,text="password",bg="skyblue",fg="black")
l3.place(x=80,y=70)
e2=tkinter.Entry(win)
e2.place(x=200,y=70)
l4=tkinter.Label(win)
l4.place(x=150,y=30)
b1=tkinter.Button(win,text="Sign in",bg="black",activebackground="black",fg="white",activeforeground="blue",padx=10,pady=4,command=login)
b1.place(x=150,y=100)
b2=tkinter.Button(win,text="Sign up",bg="black",activebackground="black",fg="white",activeforeground="blue",padx=10,pady=4,command=reg_form)
b2.place(x=250,y=100)


win.mainloop()

