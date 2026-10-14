#24. Write a program to check exam results (Distinction, First Class, Pass, Fail).

pct = int(input("Percentage: "))
if pct >= 75:
    print("Distinction")
elif pct >= 60:
    print("First Class")
elif pct >= 40:
    print("Pass")
else:
    print("Fail")