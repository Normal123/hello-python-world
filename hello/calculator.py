a = int(input('Please, enter the number:'))  # reads input values
b = int(input('Please, enter the number:'))
operation = input ('Please, enter the operation (+ - * /):')

if(operation== '+'):
    print (a, '+', b, '=', a+b)

if (operation == '-'):
    print(a, '-', b, '=', a - b)
if (operation == '*'):
    print(a, '*', b, '=', a * b)
if (operation == '/'):
    if b==0:
         print ("Ділення на 0 неможливе")
    else:
         print(a, '/', b, '=', a / b)
if (operation == '//'):
    if b==0:
         print ("Ділення на 0 неможливе")
    else:
         print(a, '//', b, '=', a // b)
if (operation == '%'):
    if b==0:
         print ("Ділення на 0 неможливе")
    else:
         print(a, '%', b, '=', a % b)