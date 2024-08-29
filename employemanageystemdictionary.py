# employee management system using dictionary

import datetime
employee=[]
while True:
    print(
        '''
    1.Registration
    2.View employee list
    3.Update employee list
    4.Delete employee list
    5.Tasks
    6.Search employee
    7.Exit
    '''
    )
    choice=int(input("enter a choice"))
    if choice==1:
        id=int(input("enter emplyee id"))
        name=input("enter employee name")
        age=int(input("enter employee age"))
        phone=int(input("enter phone number"))
        place=input("enter place")
        position=input("enter position of the employee")
        salary=int(input("enter salary"))
        experience=int(input("year of experience"))
        employee.append({'id':id,'name':name,'age':age,'phone':phone,'place':place,'position':position,'salary':salary,'experience':experience})
    elif choice==2:
        print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('id','name','age','phone','place','position','salary','experience'))
        print('-'*80)
        for i in employee:
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['age'],i['phone'],i['place'],i['position'],i['salary'],i['experience']))
    elif choice==3:
        id=int(input("enter employee id"))
        f=0
        while True:
            print(
                '''
            1.Update age
            2.Update phone no
            3.Update place
            4.Update position
            5.Updatr salary
            6.Update experience
            7.Exit
            ''')
            choice=int(input("enter your choice"))
            if choice==1:
                for i in employee:
                    if i['id']==id:
                        new_age=int(input("enter new age"))
                        i['age']==new_age
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==2:
                for i in employee:
                    if i['id']==id:
                        new_phone_no=int(input("enter new phone no"))
                        i['phone']=new_phone_no
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==3:
                for i in employee:
                    if i['id']==id:
                        new_place=input("enter new place")
                        i['place']=new_place
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==4:
                for i in employee:
                    if i['id']==id:
                        new_position=input("enter new employee position")
                        i['position']=new_position
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==5:
                for i in employee:
                    if i['id']==id:
                        new_salary=int(input("enter new salary "))
                        i['salary']=new_salary
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==6:
                for i in employee:
                    if i['id']==id:
                        update_experience=int(input("enter experience"))
                        i['experience']=update_experience
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==7:
                break
            else:
                print("invalid choice")
    elif choice==4:
        id=int(input("enter employee id"))
        f=0
        for i in employee:
            if i['id']==id:
                employee.remove(i)
                f=1
        if f==0:
            print("invalid id")
    elif choice==5:
        id=int(input("enter employee id"))
        f=0
        for i in employee:
            if i['id']==id:
                f=1
                task=input("enter task")
                date=datetime.datetime.now().strftime("%x")
                days=int(input("how many days"))
                i['task']=[task,date,days]
        if f==0:
            print("employee not found")
    elif choice==6:
        id=int(input("enter employee id"))
        f=0
        for i in employee:
            if i['id']==id:
                f=1
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<12}{:<12}'.format('id','name','age','phone','place','position','salary','experience'))
                print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<12}{:<12}{:<12}'.format(i['id'],i['name'],i['age'],i['phone'],i['place'],i['position'],i['salary'],i['experience']))

                print("work details")
                if 'task' in i:
                    print(i['task'])
                else:
                    print("no work available")
        if f==0:
            print("employee not found")
    elif choice==7:
        break
    else:
        print("invalid choice")




