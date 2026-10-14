#6. Write a program to compare two numbers and print the greater one.

a = int(input("First: "))
b = int(input("Second: "))
if a > b:
    print(f"Greater: {a}")
elif b > a:
    print(f"Greater: {b}")
else:
    print("Both are equal")