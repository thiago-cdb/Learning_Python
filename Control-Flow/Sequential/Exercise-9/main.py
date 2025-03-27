import math

sphereRadius =  float(input('Enter the sphere radius value: '))

sphereVolume = 4 / 3 * math.pi * sphereRadius ** 3
sphereArea = 4 * math.pi * sphereRadius ** 2

print(f'The sphere volume is {sphereVolume:.2f}')
print(f'The sphere area is {sphereArea:.2f}')
