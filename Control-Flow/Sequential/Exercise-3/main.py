grade1 = float(input('Enter the first grade: '))
weight1 = float(input('Enter their weight: '))
grade2 = float(input('Enter the first grade: '))
weight2 = float(input('Enter their weight: '))
grade3 = float(input('Enter the first grade: '))
weight3 = float(input('Enter their weight: '))

average = (grade1 * weight1 + grade2 * weight2 + grade3 * weight3) /  (weight1 + weight2 + weight3)

print(f'The weighted average of grades is {average}')
