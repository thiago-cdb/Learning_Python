salary = float(input('Enter your salary (in $): '))
sales = float(input('Enter your sales values (amount in $): '))
years = int(input('Enter your years is this company: '))

commissionPercentage = 0


if years >= 10:

    if sales < 500:
        commissionPercentage = 5

    elif 500 <= sales < 2000:
        commissionPercentage = 10

    else:
        commissionPercentage = 15

elif 5 <= years < 10: 

    if sales < 1000:
        commissionPercentage = 0

    elif 1000 <= sales < 3000:
        commissionPercentage = 10

    else:
        commissionPercentage = 15

else:
    commissionPercentage = 0

commission = sales * commissionPercentage / 100
total = salary + commission

print(f'The total for you to receive is ${total:.2f}')



