#17. Write a program to check grade based on marks (A, B, C, Fail).

m = int(input("Enter marks: "))
if m >= 80:
    print("Grade: A")
elif m >= 60:
    print("Grade: B")
elif m >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")