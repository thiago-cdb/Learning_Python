weight = float(input('Enter your weight (in lbs): '))
height = float(input('Enter your height: (in  inches): '))

bmi = 703 * weight / height ** 2

print(f'Your IBM is {bmi:.2f}%')