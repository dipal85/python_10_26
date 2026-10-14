#26. Write a program to check month names based on month number.

m = int(input("Month (1-12): "))
if m == 1: 
    print("Jan")
elif m == 2: 
    print("Feb")
elif m == 3: 
    print("Mar")
elif m == 4: 
    print("Apr")
elif m == 5: 
    print("May")
elif m == 6: 
    print("Jun")
elif m >= 7 and m <= 12:
    print(["Jul","Aug","Sep","Oct","Nov","Dec"][m-7])
else: 
    print("Invalid Month")