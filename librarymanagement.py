user=[]
library=[]
def register():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    # print(id)
    email=input('enter email id')
    f1=0
    for i in user:
        if i ['email']==email:
            f1=1
            print('email exist')
            register()
    if f1==0:
        name=input('enter your name')
        address=input('enter your address')
        phone=int(input('enter ur phone no'))
        paasword=input('enter your password')
        user.append({'id':id,'name':name,'address':address,'email':email,'phone':phone,'password':paasword})
        
           
def login():
    uname=input('enter username')
    passw=input('enter your password')
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in user:
        if i['email']==uname and i['password']==passw:
            f=2
            user=i
    return f,user
def add_book():
    if len(library)==0:
        book_id=1
    else:
        book_id=library[-1]['book_id']+1
    book_name=(input("enter book name"))
    book_stock=int(input("enter book stock"))
    book_price=int(input("enter book price"))
    library.append({'book_id':book_id,'book_name':book_name,'book_stock':book_stock,'book_price':book_price})
def view_book():
    print('{:<5}{:<8}{:<8}{:<12}'.format('book_id','book_name','book_stock','book_price'))
    print('-'*50)
    for i in library:
        print('{:<5}{:<8}{:<8}{:<12}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))
# def update_book():


while True:
    print(
        '''
    1.Registration
    2.Login
    3.Exit
    '''
    )
    choice=int(input("enter your choice"))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print(
                    '''
                    1.Add Book
                    2.View Book
                    3.Update Book
                    4.Delete Book
                    5.View Users
                    6.Exit
                    '''
                )
                sub_choice=int(input("enter ur choice"))
                if sub_choice==1:
                    add_book()
                elif sub_choice==2:
                    view_book()
                elif sub_choice==3:




           
        elif f==2:
            print('user login')
        else:
            print('invalid uname or passw')
            
    elif choice==3:
        break
     