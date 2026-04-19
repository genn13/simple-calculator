while True:
    
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        op = input('Enter an operation(+, -, *, /):')

        if op == '+':
            print(f'{num1} + {num2} = {num1+num2}')
        elif op == '-':
            print(f'{num1} - {num2} = {num1-num2}')
        elif op == '*':
            print(f'{num1} * {num2} = {num1*num2}')
        elif op == '/':
            if num2==0:
                print("You can't divide by zero")
            else:
                print(f'{num1} / {num2} = {num1/num2}')
        else:
            print('Unknown operation')
        choice = input('Do you want to continue?(Y/N)').lower()
        if choice == 'n':
            break
        
    except ValueError:
        print('Please enter valid numbers')
    