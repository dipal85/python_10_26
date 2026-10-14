#46. Write a program to print grade description using match case.

grade = input("Grade (A/B/C/D/F): ").upper()
match grade:
    case "A": 
        print("Excellent performance")
    case "B": 
        print("Good performance")
    case "C": 
        print("Satisfactory performance")
    case "D": 
        print("Needs Improvement")
    case "F": 
        print("Failed")
    case _: 
        print("Invalid Grade Code")
