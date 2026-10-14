#22. Write a program to check salary bonus based on years of service.

service = int(input("Years of service: "))
sal = int(input("Salary: "))
if service > 10:
    bonus = sal * 0.15
elif service >= 5:
    bonus = sal * 0.10
else:
    bonus = sal * 0.05
print(f"Bonus amount: {bonus}")