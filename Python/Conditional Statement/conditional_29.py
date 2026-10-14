#29. Write a program to check blood donation eligibility based on age and weight.

age = int(input("Age: "))
wt = float(input("Weight (kg): "))
if 18 <= age <= 65 and wt >= 50:
    print("Eligible to donate blood")
else:
    print("Ineligible to donate blood")