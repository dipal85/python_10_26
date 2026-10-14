#30. Write a program to check the type of number (single, double, or three digit).

n = abs(int(input("Number: ")))
if n < 10:
    print("Single-digit number")
elif n < 100:
    print("Double-digit number")
elif n < 1000:
    print("Three-digit number")
else:
    print("More than 3 digits")