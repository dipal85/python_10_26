#25. Write a program to check whether a triangle is equilateral, isosceles, or scalene.

x = int(input("Side 1: "))
y = int(input("Side 2: "))
z = int(input("Side 3: "))
if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene triangle")