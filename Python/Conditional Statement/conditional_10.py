#10. Write a program to check whether a number is a single-digit number or not.

num = int(input("Enter integer: "))
if -9 <= num <= 9:
    print("Single-digit number")
else:
    print("Not a single-digit number")