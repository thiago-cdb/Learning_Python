programRepeater = 'y'

while programRepeater.lower() == 'y':
    initialNumber = int(input('Enter the first number of range: '))
    finalNumber = int(input('Enter the last number of range: '))

    step = 1 if initialNumber <= finalNumber else -1

    for number in range(initialNumber, finalNumber + step, step):
        result = 'even' if number % 2 == 0 else 'odd'
        print(f'{number} is {result}')

    programRepeater = input("Do you want to use the program again? (y/n): ").strip().lower()
    
print('Program terminated.')
    

    


    
    

