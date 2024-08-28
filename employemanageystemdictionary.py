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

