surfaceTemp = float(input('Enter the surface temperature of the star (in Kelvins): '))

if surfaceTemp < 5500:
    classification = 'Red Dwarf'

elif surfaceTemp >= 5500 and surfaceTemp < 6000:
    classification = 'Yellow Star'

elif surfaceTemp >= 6000 and surfaceTemp < 7500:
    classification = 'White Star'

elif surfaceTemp >= 7500 and surfaceTemp < 10000:
    classification = 'Blue-White Star'

else:
    classification = 'Blue Giant'

print(f'This star is a {classification}.')
