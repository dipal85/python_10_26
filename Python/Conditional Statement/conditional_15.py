#15. Write a program to check whether a number is divisible by both 3 and 7 or not.

num = int(input("Enter integer: "))
if num % 3 == 0 and num % 7 == 0:
    print("Divisible by both 3 and 7")
else:
    print("Not divisible by both 3 and 7")