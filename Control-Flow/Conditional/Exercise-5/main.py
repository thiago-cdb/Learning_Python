weight = float(input('Enter your weight (in lbs): '))
height = float(input('Enter your height (in inches): '))

bmi = (weight / height ** 2) * 703

if bmi < 18.5:
    print(f'You are underweight with BMI in {bmi:.2f}')

elif 18.5 <= bmi < 25:
    print(f'You have a normal weight with BMI in {bmi:.2f}')

elif 25 <= bmi < 30:
    print(f'You are overweight with BMI in {bmi:.2f}') 

else: 
    print(f'You are obese (BMI in {bmi:.2f})')


