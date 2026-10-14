#16. Write a program to find the greatest of three numbers

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a >= b and a >= c:
    print(f"Greatest: {a}")
elif b >= a and b >= c:
    print(f"Greatest: {b}")
else:
    print(f"Greatest: {c}")