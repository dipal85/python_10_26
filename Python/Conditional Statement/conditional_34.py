#34. Write a program to check whether a year is a leap year and century year.

yr = int(input("Year: "))
if yr % 100 == 0:
    if yr % 400 == 0:
        print("Century Leap Year")
    else:
        print("Century Year (Not Leap)")
else:
    print("Not a Century Year")