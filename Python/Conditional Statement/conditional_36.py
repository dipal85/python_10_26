#36. Write a program to check whether a person is eligible for a driving license.

age = int(input("Age: "))
med_pass = input("Medical pass? (y/n): ").lower()
if age >= 18 and med_pass == "y":
    print("Eligible for driving license")
else:
    print("Not eligible for license")