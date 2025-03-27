number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
number3 = float(input('Enter the third number: '))

if number1 > number2 and number1 > number3 :
    print(f'The first number {number1} is the greatest')

elif number2 > number1 and number2 > number3:
    print(f'The second number {number2} is the greatest')

elif number3 > number1 and number3 > number2:
    print(f'The third number {number3} is the greatest')

elif number1 == number2 == number3: 
    print(f'All numbers are equal')

elif number1 == number2:
    print('The first and the second numbers are equal')

elif number1 == number3:
    print('The first and third numbers are equal')

else:
    print('The seconds and the third numbers are equal')