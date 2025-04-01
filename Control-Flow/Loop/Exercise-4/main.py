programRepeater = 'y'

while programRepeater == 'y':
    numberChose = int(input('Enter a number of your choice: '))

    divisors = 0

    for numberTest in range(2, numberChose + 1):
        for number in range(1 , numberTest + 1):
            if numberTest % number == 0:
                divisors += 1
    
        if divisors == 2:
            print(f'number {numberTest} is prime.')

        divisors = 0
        
    programRepeater = input('Do you want to use the program again? (y/n): ')

print('Program terminated.')


