from math import pi

def circle_area(r):
	if type(r) not in [int, float]:
		raise TypeError("The radius must be a non-negative real number")
	if r < 0:
		raise ValueError('The radius cannot be negative')
	return pi*(r**2)


radii = [2,0,-3,2+5j,True, "radius"]


for r in radii:
	A = circle_area(r)
	message = f"Area of circles with radius {r} is {A}"
	print(message)