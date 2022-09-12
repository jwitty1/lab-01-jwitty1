import math
COVERAGE = 40
print('Enter the length of the room in metres')
length_metres = float(input())
print('Enter the width of the room in metres')
width_metres = float(input())
print('Enter the height of the room in metres')
height_metres = float(input())
print('How many coats of paint would you like to apply')
coats = float(input())
surface_area = 2 * (length_metres * height_metres) + 2 * (width_metres * height_metres) + (length_metres * width_metres)
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed / COVERAGE
rounded_cans_of_paint_required = math.ceil(cans_of_paint_required)
print("The number of paints required for purchase are")
print(rounded_cans_of_paint_required)