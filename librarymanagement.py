user=[]
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
        name=input('enter your name')
        address=input('enter your address')
        email=input('enter email id')
        phone=int(input('enter ur phone no'))
        user.append({'name':name,'address':address,'email':email,'phone':phone})
        print(user)
    elif choice==3:
        break
     