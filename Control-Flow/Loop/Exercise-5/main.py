programRepeater = 'y' 

while programRepeater == 'y':
    divisor = int(input('Enter the divisor: '))
    start = int(input('Enter the fisrt number in the range: '))
    final = int(input('Enter the last number in the range: '))

    divisiblesList = []

    for number in range(start, final + 1):
        if number % divisor == 0:
            print(f'Number {number} is divisible by {divisor}.')
            divisiblesList.append(number)

    if not divisiblesList:
        print(f'The range {start}, {final} has no numbers divisible by {divisor}.')

    programRepeater = input('Do you want run the program again? y/n: ').lower().strip()

print('Program terminated.')