#33. Write a program to check whether a person can apply for a loan.

sal = float(input("Monthly salary: "))
cibil = int(input("Credit score: "))
if sal >= 25000:
    if cibil >= 700:
        print("Eligible for Loan")
    else:
        print("Denied: Low credit score")
else:
    print("Denied: Insufficient salary")