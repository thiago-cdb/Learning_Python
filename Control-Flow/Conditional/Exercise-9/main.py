income = float(input('Enter your monthly income: '))
expenses = float(input('Enter your monthly expenses: '))
savings = float(input('Enter your monthly savings: '))

if expenses <= 0.5 * income:
    print('Great job! You\'re saving well!')

elif 0.5 * income < expenses and expenses <= 0.8 * income:
    print('Consider reducing unnecessary expenses.')

else:
    if savings >= 0.2 * income:
        print('You\'re spending a lot, but savings help.')

    else:
       print('Warning! Your expenses are too high!')
       


