#37. Write a program to check whether a number lies between 10 and 50.

num = int(input("Enter number: "))
if 10 <= num <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is outside [10, 50]")