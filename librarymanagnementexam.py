library=[]
while True:
    print(
        '''
        1) Admin
        2) User
        3) Exit
    '''
    )
    choice=int(input("enter ur choice"))
    if choice==1:
        while True:
            print(
                '''
                1) Add Book
                2) Update Book
                3) Remove Book
                4) View All Books
                5) Search Book
                6) Exit
            '''
            )
            sub_choice=int(input("enter your choice"))
            if sub_choice==1:
                Book_id=int(input("enter book id"))
                Book_name=input("enter book name")
                Book_price=int(input("enter book price"))
                Book_stock=int(input("enter book stock"))
                library.append({'Book_id':Book_id,'Book_name':Book_name,'Book_price':Book_price,'Book_stock':Book_stock})
            
            elif sub_choice==2:
                id=int(input("enter book id"))
                f=0
                for i in library:
                    if i['Book_id']==id:
                        f=1
                        name=input("enter book name")
                        price=int(input("enter price"))
                        stock=int(input('enter stock'))
                        
                        i['Book_name']=name
                        i['Book_price']=price
                        i['Book_stock']=stock
                        if f==0:
                            print('invalid book id')

            elif sub_choice==3:
                id=int(input("enter book id"))
                f=0
                for i in library:
                    if i['Book_id']==id:
                        f=1
                        library.remove(i)
            
            elif sub_choice==4:
                print('{:<8}{:<15}{:<15}{:<8}'.format('Book_id','Book_name','Book_stock','Book_price'))
                print('-'*50)
                for i in library:
                    print('{:<8}{:<15}{:<15}{:<8}'.format(i['Book_id'],i['Book_name'],i['Book_stock'],i['Book_price']))
            
            elif sub_choice==5:
                id=int(input("enter book id"))
                f=0
                for i in library:
                    if i['Book_id']==id:
                        f=1
                        print('{:<8}{:<15}{:<15}{:<8}'.format('Book_id','Book_name','Book_stock','Book_price'))
                        print('-'*50)
                        print('{:<8}{:<15}{:<15}{:<8}'.format(i['Book_id'],i['Book_name'],i['Book_stock'],i['Book_price']))
                if f==0:
                    print("invalid Book id")
            
            elif sub_choice==6:
                break

    elif choice==2:
        while True:
            print(
                '''
            1) View Books
            2) Exit
            '''
            )
            sub_choice=int(input("enter ur choice"))
            if sub_choice==1:
                print('{:<8}{:<15}{:<15}{:<8}'.format('Book_id','Book_name','Book_stock','Book_price'))
                print('-'*50)
                for i in library:
                    print('{:<8}{:<15}{:<15}{:<8}'.format(i['Book_id'],i['Book_name'],i['Book_stock'],i['Book_price']))

            elif sub_choice==2:
                break

    elif choice==3:
        break
            

       
                      

            


        # uname=input("enter username")
        # password=input("enter password")
        # f=0
        # user=''
        # if uname=='admin' and password=='admin':
