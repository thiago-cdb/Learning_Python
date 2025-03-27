import math 

radius = float(input('Enter the radius of the circle: '))

area =  math.pi * radius ** 2
perimeter = 2 * math.pi * radius

print(f'The area of this circle is {area:.2f}')
print(f'The perimeter of this circle is {perimeter:.2f}')