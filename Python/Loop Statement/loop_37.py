#37. Print numbers until user enters a negative number.

while True:
    x = int(input("Enter number: "))
    if x < 0:
        print("Negative detected. Stopped.")
        break
    print(f"Entered: {x}")