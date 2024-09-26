# studentmanagementsystem using dictionary

std=[]
while True:
    print(
        '''
    1)add
    2)view
    3)update
    4)delete
    5)exit
    '''
    )
    while True:
        try:
            choice=int(input("enter a choice"))
            break
        except:
            print('enter choice again')
    if choice==1:
        name=str(input('enter student name'))
        age=int(input('enter student age'))
        mark=int(input("enter student marks"))
        std.append({'name':name,'age':age,'mark':mark})
        print(std)
    elif choice==2:
        print('{:<10}{:<8}{:<8}'.format('name','age','mark'))
        print('-'*25)
        for i in std:
            print('{:<10}{:<8}{:<8}'.format(i['name'],i['age'],i['mark']))
    elif choice==3:
        name=input("enter student name")
        f=0
        for i in std:
            if i['name']==name:
                new_mark=int(input("enter new mark"))
                i['mark']=new_mark
                f=1
        if f==0:
            print("name not in list")
    elif choice==4:
        name=input("enter name")
        f=0
        for i in std:
            if i ['name']==name:
                std.remove(i)
                f=1
        if f==0:
            print("name not in list")
    elif choice==5:
        break
    else:
        print("invalid choice")
            

             
