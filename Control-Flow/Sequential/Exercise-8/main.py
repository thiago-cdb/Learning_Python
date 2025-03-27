import math

iCapital = float(input('Enter the initial capital (in dollars): '))
interest = float(input('Enter the interest (percent per months): ')) / 100
finalAmount = float(input('Enter the final Amount (in dollars): '))

time = math.log(finalAmount / iCapital) / math.log(1 + interest) 

print(f'The necessary time to reach that amount is {time:.2f} months')