programRepeater = 'y'

while programRepeater == 'y':
    numberChose = int(input('Enter a number of your choice: '))

    for number in range (10):
        result = numberChose * number
        print(f'{numberChose} x {number} = {result}')
        
    programRepeater = input('Do you want to use the program again? (y/n:)').strip().lower()

print('Program terminated.')
