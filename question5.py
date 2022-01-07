num1 = input('Enter 1st number...')
num2 = input('Enter 2nd number...')

try:
    print(float(num1) / float(num2))
except ZeroDivisionError:
    print("can't divide a number by zero")