#32. Write a program to check whether a student is eligible for an exam (attendance + marks).

att = int(input("Attendance %: "))
mrk = int(input("Internal marks: "))
if att >= 75:
    if mrk >= 40:
        print("Eligible for exam")
    else:
        print("Ineligible: Insufficient marks")
else:
    print("Ineligible: Low attendance")