productionCost = float(input('Enter the production cost (in dollars): '))
taxPercentage = float(input('Enter the tax percentage: ')) / 100
transportCost = float(input('Enter the transportation cost (in dollars): '))
storageCost = float(input('Enter the storage cost (in dollars): '))
discountPercentage = float(input('Enter the promotional discount percentage for customer: ')) / 100
profitPercentage = float(input('Enter the desired profit percentage: ')) / 100

totalCost =  productionCost + transportCost + storageCost
priceWithTax = totalCost * (1 + taxPercentage)
finalPrice = priceWithTax * (1 + profitPercentage)
discountFinalPrice = finalPrice * (1 - discountPercentage)

print('\n----------PRICE BREAKDOWN----------\n')
print(f'the total cost is ${totalCost:.2f}')
print(f'the price with taxes is ${priceWithTax:.2f}')
print(f'the price with the profit margin is ${finalPrice:.2f}')
print(f'the price with promotional discount is ${discountFinalPrice:.2f}')