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
    u=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in user:
        if i['email']==uname and i['password']==passw:
            f=2
            u=i
    return f,u
def add_book():
    if len(library)==0:
        book_id=1
    else:
        book_id=library[-1]['book_id']+1
    book_name=(input("enter book name"))
    book_stock=int(input("enter book stock"))
    book_price=int(input("enter book price"))
    library.append({'book_id':book_id,'book_name':book_name,'book_stock':book_stock,'book_price':book_price,'books':[]})
def view_book():
    print('{:<5}{:<8}{:<8}{:<12}'.format('book_id','book_name','book_stock','book_price'))
    print('-'*50)
    for i in library:
        print('{:<5}{:<8}{:<8}{:<12}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))
def update_book():
    id=int(input("enter book id"))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
            name=input("enter book name")
            stock=int(input('enter stock'))
            price=int(input("enter price"))
            i['book_name']=name
            i['book_stock']=stock
            i['book_price']=price
            
    if f==0:
        print('invalid id')
def delete_book():
    id=int(input('enter book id'))
    f1=0
    for i in library:
        if i['book_id']==id:
            f1=1
            library.remove(i)
    if f1==0:
        print("invalid book_id")
def view_user():
    print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format('id','name','email','phone','address'))
    print('-'*80)
    for i in user:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}'.format(i['id'],i['name'],i['email'],i['phone'],i['address']))
def view_profile(user):
    print('{:<5}{:<8}{:8}{:12}{:12}'.format('id','name','email','phone','address'))
    print('-'*70)
    print('{:<5}{:<8}{:8}{:12}{:12}'.format(user['id'],user['name'],user['email'],user['phone'],user['address']))
def view_books():
    print('{:<5}{:<8}{:<8}{:<12}'.format('book_id','book_name','book_stock','book_price'))
    print('-'*50)
    for i in library:
        print('{:<5}{:<8}{:<8}{:<12}'.format(i['book_id'],i['book_name'],i['book_stock'],i['book_price']))
def take_book(u):
    id=int(input("enter book id"))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
            if i['book_stock']>0:
                user['books'].append(i['book_id'])
                i['book_stock']-=1
            else:
                print("out of stock")
def return_book(user):
    id=int(input("enter book id"))
    f=0
    for i in library:
        if i['book_id']==id:
            f=1
def books_in_hand(user):
    print(user['books'])


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
        f,u=login()
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
                    update_book()
                elif sub_choice==4:
                    delete_book()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break


           
        elif f==2:
            while True:
                print(
                    '''
                    1.View Profile
                    2.View Book
                    3.Take Book
                    4.Return Book
                    5.Books in Hand
                    6.Exit
                    '''
                )
                sub_choice=int(input("enter your choice"))
                if sub_choice==1:
                    view_profile(u)
                elif sub_choice==2:
                    view_books()
                elif sub_choice==3:
                    take_book(u)
                elif sub_choice==4:
                    return_book()
                elif sub_choice==5:
                    books_in_hand()
                elif sub_choice==6:
                    break
                
                

        else:
            print('invalid uname or passw')
            
    elif choice==3:
        break
     