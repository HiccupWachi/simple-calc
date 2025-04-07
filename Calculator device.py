# Basic calculator (+, -, *, /.)

num1 = float(input('Enter the first number:'))
num2 = float(input('Enter the second number:'))
operation = input('Select the operation(+, -, *, /):')

if operation == '+':
    result = num1 + num2 
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
     print('Error:Division by zero is not allowed.')

    result = num1 / num2

print(f'The result is:{result}')    







