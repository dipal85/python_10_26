#5. Write a program to check whether a given year is a leap year or not.

yr = int(input("Enter year: "))
if (yr % 400 == 0) or (yr % 4 == 0 and yr % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")