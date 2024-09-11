emp=[]

def login():
    uname=input("enter username")
    passw=input("enter password")
    f=0
    if uname=='admin' and passw =='admin':
        f=1
        return f
def add_emp():
    id=int(input("enter ur id"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print("id exist")
            add_emp()
    if f1==0:
        name=str(input("enter ur name"))
        age=int(input("enter ur age"))
        salary=int(input("enter ur salary"))
        place=str(input("enter ur place"))
        dob=input('date of birth')
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob})
def edit_emp():
    id=int(input("enter ur id"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            name=str(input("enter ur name"))
            age=int(input("enter ur age"))
            salary=int(input("enter ur salary"))
            place=str(input("enter ur place"))
            dob=input('date of birth')
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['dob']=dob
    if f1==0:
        print('invalid ')
def delete_emp():
    id=int(input("enter ur id"))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            emp.remove(i)
    if f1==0:
        print('invalid id')
def display_emp():
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format('id','name','age','salary','place','dob'))
            print('-'*80)
            for i in emp:
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))

while True:
    print(
        '''
    1.login
    2.exit
    
    '''
    )    
    ch=int(input("enter ur choice"))
    if ch==1:
        f=login()
        if f==1:
            while True:
                print(
                    '''
                    1.Add emp
                    2.Update emp
                    3.Delete
                    4.Display
                    5.Logout
                '''
                )
                sub_ch=int(input("enter ur choice"))
                if sub_ch==1:
                    add_emp()
                elif sub_ch==2:
                    edit_emp()
                elif sub_ch==3:
                    delete_emp()
                elif sub_ch==4:
                    display_emp()
                elif sub_ch==5:
                    break
        elif f==0:
            print('invalid uname or passw')
                    
                    




