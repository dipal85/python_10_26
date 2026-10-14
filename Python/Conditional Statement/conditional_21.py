#21. Write a program to find the smallest of three numbers.

a, b, c = int(input()), int(input()), int(input())
if a <= b and a <= c:
    print(f"Smallest: {a}")
elif b <= a and b <= c:
    print(f"Smallest: {b}")
else:
    print(f"Smallest: {c}")