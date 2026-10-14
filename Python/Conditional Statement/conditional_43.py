#43. Write a program to print month days using match case.

m = int(input("Month (1-12): "))
match m:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Days")
    case 4 | 6 | 9 | 11:
        print("30 Days")
    case 2:
        print("28 or 29 Days")
    case _:
        print("Invalid month")