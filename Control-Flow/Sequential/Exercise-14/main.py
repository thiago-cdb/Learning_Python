ax = float(input('Enter the x coordinate of the first point: '))
ay = float(input('Enter the y coordinate of the first point: '))
bx = float(input('Enter the x coordinate of the second point: '))
by = float(input('Enter the y coordinate of the second point: '))

distance = ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
print(f'The distance between the points is {distance:.2f}')