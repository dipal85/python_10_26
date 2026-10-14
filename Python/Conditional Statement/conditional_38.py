#38. Write a program to check whether a student passed all subjects.

s1 = int(input("Subject 1 marks: "))
s2 = int(input("Subject 2 marks: "))
s3 = int(input("Subject 3 marks: "))
if s1 >= 40 and s2 >= 40 and s3 >= 40:
    print("Passed all subjects")
else:
    print("Failed in one or more subjects")