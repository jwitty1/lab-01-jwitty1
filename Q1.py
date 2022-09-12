PI = 3.14159
print('Enter the radius of the sphere')
radius = float(input())
double_radius = 2 * radius
surface_area = 4 * PI * radius ** 2
print('The surface area of the sphere is ')
print(surface_area)
volume = (4/3) * PI * radius ** 3
print('The volume of the sphere is')
print(volume)
double_surface_area = 4 * PI * double_radius ** 2
double_volume = (4/3) * PI * double_radius ** 2
surface_area_factor = double_surface_area / surface_area
volume_factor = double_volume / volume
print("When you double the radius the surface area increases by a factor of ")
print(surface_area_factor)
print("When you double the radius the volume increases by a factor of")
print(volume_factor)
