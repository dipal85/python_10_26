#31. Write a program to check whether a number is positive and even using nested if.

num = int(input("Enter integer: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Not a positive number")