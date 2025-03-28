userInput = input('Enter a number, word or phrase: ')
cleanedInput = userInput.upper()
inputReplace = cleanedInput.replace(' ','')

invertedCheck = inputReplace[::-1]
originalInput = userInput[::-1]

if inputReplace == invertedCheck:
    result = 'is a palindrome!'

else:
    result = 'is not a palindrome'

print(f'{userInput} {result}\nEntered value: {userInput}\nInverted value: {originalInput}')


