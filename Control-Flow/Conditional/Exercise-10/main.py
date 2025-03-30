timeInArmy = int(input('Enter your time, in years, in the army: '))
missionsAmount = int(input('Enter your number of missions he was assigned to: '))


if timeInArmy > 5 and missionsAmount > 10:
    print('You have been promoted.')

else: 
    print(f'You only have {timeInArmy} year(s) in army and {missionsAmount} mission(s) assigned. You need more than 5 years in the army and more than 10 missions. ')