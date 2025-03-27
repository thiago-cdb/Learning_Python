import math

iCapital = float(input('Enter the initial capital (in dollars): '))
interest = float(input('Enter the interest (percent per months): ')) / 100
time = float(input('Enter the time (in months): '))

finalAmount = iCapital * (interest + time + 1)
profit = finalAmount - iCapital

print(f'The final amout of your deposit is {finalAmount}$')
print(f'The profit of your deposit is {profit}$')