programRepeater = 'y'

while programRepeater == 'y':
    numberChose = input('Enter a number of you choice: ').strip()

    algarismList = list(numberChose)
    numberLen = len(algarismList)
    algarismSum = sum(int(algarism) ** numberLen for algarism in (algarismList))

    print(f'{numberChose} is a Armstrong number!') if algarismSum == int(numberChose) else print(f'{numberChose} is not a Armstrong number.')

    programRepeater = input('Do you want to use the program again? (y/n): ').strip().lower()

print('Program terminated.')