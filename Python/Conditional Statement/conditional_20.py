#20. Write a program to check ticket price based on age.

age = int(input("Enter age: "))
if age < 5:
    print("Ticket: Free (Rs.0)")
elif age <= 12:
    print("Ticket: Child (Rs.10)")
elif age <= 60:
    print("Ticket: Adult (Rs.20)")
else:
    print("Ticket: Senior (Rs.12)")