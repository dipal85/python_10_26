status = input("Status (P/F/A/W): ").upper()
match status:
    case "P":
        print("Status: Passed Exam")
    case "F":
        print("Status: Failed Exam")
    case "A":
        print("Status: Absent")
    case "W":
        print("Status: Result Withheld")
    case _:
        print("Invalid status code")