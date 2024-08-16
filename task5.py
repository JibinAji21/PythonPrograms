#basic calculator

while True:
    print('''
1.Addition
2.Substraction
3.Multiplication
4.Division
5.modulus
6.Floordivision
7.Exponent
8.Exit''')
    choice=int(input("Enter Your Choice"))
    if choice==1:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a+b)
    elif choice==2:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a-b)
    elif choice==3:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a*b)
    elif choice==4:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a/b)
    elif choice==5:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a%b)
    elif choice==6:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a//b)
    elif choice==7:
        a=int(input("enter first number"))
        b=int(input("enter second number"))
        print(a**b)
    elif choice==8:
        break

    