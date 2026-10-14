#39. Write a program to check whether a number is greater than 0 and less than 100.

num = int(input("Enter number: "))
if 0 < num < 100:
    print("Number is between 0 and 100")
else:
    print("Number is not within (0, 100)")