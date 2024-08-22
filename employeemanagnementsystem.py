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
    choice=int(input("enter your choice"))
    if choice==1:
        id=int(input("enter emplyee id"))
        name=input("enter employee name")
        age=int(input("enter employee age"))
        phone=int(input("enter phone number"))
        place=input("enter place")
        position=input("enter position of the employee")
        salary=int(input("enter salary"))
        experience=int(input("year of experience"))
        employee.append([id,name,age,phone,place,position,salary,experience])
    elif choice==2:
         print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<10}{:<10}{:<5}'.format('id','name','age','phone','place','position','salary','experience'))
         print('-'*50)
         for i in employee:
            print('{:<5}{:<8}{:<8}{:<12}{:<12}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
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
            '''
            )
            choice=int(input("enter your choice"))
            if choice==1:
                for i in employee:
                    if id in i:
                        new_age=int(input("enter new age"))
                        i[2]=new_age
                        f=1
                        
                if f==0:
                    print("invalid id")
            elif choice==2:
                for i in employee:
                    if id in i:
                        new_phone_no=int(input("enter new phone no"))
                        i[3]=new_phone_no
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==3:
                for i in employee:
                    if id in i:
                        new_place=input("enter new place")
                        i[4]=new_place
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==4:
                for i in employee:
                    if id in i:
                        new_position=input("enter new employee position")
                        i[5]=new_position
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==5:
                for i in employee:
                    if id in i:
                        new_salary=int(input("enter new salary "))
                        i[6]=new_salary
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==6:
                for i in employee:
                    if id in i:
                        update_experience=int(input("enter experience"))
                        i[7]=update_experience
                        f=1
                if f==0:
                    print("invalid id")
            elif choice==7:
                break
            else:
                print("invalid choice")
                 






             

    

    
