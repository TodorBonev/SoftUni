from math import pi

figure = input()
area = 0

if figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

elif figure == "circle":
    radius = float(input())
    area = pi * radius * radius
    print(f"{area:.3f}")

elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2
    print(f"{area:.3f}")