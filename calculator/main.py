import numbers
import add as z
import sub as y
from mul import *
from div import div
import mod as x
while True:
    print(
        '''
        1.Addition
        2.Substraction
        3.Multiplication
        4.Division
        5.Modulus
        6.Exit
        '''
    )
    choice=int(input('enter ur choice'))
    if choice==1:
        a,b=numbers.num()
        z.add(a,b)
    elif choice==2:
        a,b=numbers.num()
        y.sub(a,b)
    elif choice==3:
        a,b=numbers.num()
        mul(a,b)
    elif choice==4:
        a,b=numbers.num()
        div(a,b)
    elif choice==5:
        a,b=numbers.num()
        x.mod(a,b)
    elif choice==6:
        break
