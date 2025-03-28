import random

userChoice = input('Enter your choice between:\nROCK\nPAPER\nSCISSORS\n:').upper()

options = ['ROCK','PAPER','SCISSORS']
computerChoice = random.choice(options)
result = ''

if userChoice not in options:
    result = 'INVALID USER CHOICE' 

elif (userChoice == 'ROCK' and computerChoice == 'SCISSORS') or \
     (userChoice == 'PAPER' and computerChoice == 'ROCK') or \
     (userChoice == 'SCISSORS' and computerChoice == 'PAPER'):
      
    result = 'USER WINS'

elif userChoice == computerChoice:
    result = 'DRAW'

else: 
    result = 'COMPUTER WINS'
    
print(f'User chose: {userChoice} \nComputer chose: {computerChoice}\nResult: {result}')