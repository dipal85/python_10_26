#44. Write a program to check traffic signal actions using match case.

signal = input("Signal color: ").lower()
match signal:
    case "red":
        print("Stop")
    case "yellow" | "amber":
        print("Wait / Slow Down")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal Color")