grossSalary = float(input('Enter the gross monthly salary: '))
taxPercentage = float(input('Enter the tax percentage: ')) / 100
socialSecurityDeduction = float(input('Enter the amount for social security: '))
healthInsuranceDeduction = float(input('Enter the amount for health insurance: '))
extraBenefits = float(input('Enter the amount of extra benefits (meal and transport allowancees): '))

totalDeductions = (grossSalary * taxPercentage) + socialSecurityDeduction + healthInsuranceDeduction 
netSalary = grossSalary - totalDeductions + extraBenefits

print(f'the total deductions of your salary is ${totalDeductions}')
print(f'your net salary is ${netSalary}')
