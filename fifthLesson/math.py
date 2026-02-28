import cmath  

PI = cmath.pi

"""
The min() and max() functions can be used to find the lowest or highest value in an iterable:
The abs() function returns the absolute (positive) value of the specified number:
The pow(x, y) function returns the value of x to the power of y (x^y)

When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:

The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

The math.pi constant, returns the value of PI (3.14...):

"""

def degree_to_radian(degree):
    return degree * (PI / 180)


def trapezoid_area(base1, base2, height):
    return ((base1 + base2) / 2) * height

def regular_polygon_area(sides, side_length):
    return (side_length ** 2 * sides) / (4 * cmath.tan(PI / sides).real)

def parallelogram_area(base, height):
    return base * height


degree = 15
print(f"Input degree: {degree}")
print(f"Output radian: {degree_to_radian(degree):.6f}")

print()

height = 5
base1 = 5
base2 = 6
print(f"Height: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {trapezoid_area(base1, base2, height)}")

print()


sides = 4
side_length = 25
print(f"Input number of sides: {sides}")
print(f"Input the length of a side: {side_length}")
print(f"The area of the polygon is: {regular_polygon_area(sides, side_length):.0f}")

print()

base = 5
height = 6
print(f"Length of base: {base}")
print(f"Height of parallelogram: {height}")
print(f"Expected Output: {parallelogram_area(base, height)}")
