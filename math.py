#Import necessary modules
from operator import add
from operator import truediv
from operator import sub
from operator import mul

#Ask for the User's name
name = str(input('Enter your name: '))
print('\n\n')

#Check if it's too long and then slice  it and then Welcome the user
if (len(name) > 15):
    print(f'** Welcome dear {name[0:10]}...... **')
else:
    print(f'** Welcome dear {name} **')

#Create a function that will do the math
def mathematics():
    #Ask the user want they want to do and store it in a variable called task
    task = str(input('** Do you want to div mult add sub or divmod ** \n'))
    
    #Evaluate the input
    if (task == 'div'):
        a = int(input('Enter first number: '))
        b = int(input('Enter second number: '))
        if(b == 0):
            print('ZeroDivisionError')
        else:
            print(f'Expression: {a} / {b}')
            print('The quotient is {}'.format(truediv(a,b)))
            del a
            del b
    elif (task == 'mult'):
        d = int(input('Enter first number: '))
        e = int(input('Enter second number: '))
        print(f'Expression: {d} * {e}')
        print('The product is {}'.format(mul(d,e)))
        del d
        del e
    elif (task == 'add'):
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print(f'Expression: {x} + {y}')
        print('The sum is {}'.format(add(x,y)))
        del x
        del y
    elif (task == 'sub'):
        p = int(input('Enter first number: '))
        q= int(input('Enter second number: '))
        print(f'Expression: {p} - {q}')
        print('The remainder is {}'.format(sub(p,q)))
        del p
        del q
    elif (task == 'divmod'):
        j = int(input('Enter first number: '))
        k = int(input('Enter second number: '))
        print(f'Expression: {j} % {k}')
        ans = list(divmod(j,k))
        print(f'The answer is {ans[0]} remainder {ans[1]}')
        del j
        del k
        del ans
    else:
        print('Unknown Operand')

#Call the function
mathematics()
