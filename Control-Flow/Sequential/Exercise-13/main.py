import math

initialVelocity = float(input('Enter the initial velocity of projectil (in m/s): '))
launchAngleDegrees = float(input('Enter the launch angle of artillary (in degrees): '))
gravity = 9.81

launchAngleRadians = math.radians(launchAngleDegrees)
maxDistance = initialVelocity ** 2 * math.sin (2 * launchAngleRadians / gravity)

print('\n---------- ARTILLERY CALCULATION ----------\n')
print(f'Initial velocity entered: {initialVelocity:.2f} m/s')
print(f'Launch angle entered: {launchAngleDegrees:.2f}°')
print(f'Maximum distance reached: {maxDistance:.2f} m')



