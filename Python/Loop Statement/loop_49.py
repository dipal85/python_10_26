#49. Display menu-driven program using while loop.

while True:
    print("\n[1] Square  [2] Cube  [3] Factorial  [4] Exit")
    ch = input("Enter choice (1-4): ")
    if ch == "1":
        x = float(input("Number: ")); print(f"Square: {x * x}")
    elif ch == "2":
        x = float(input("Number: ")); print(f"Cube: {x ** 3}")
    elif ch == "3":
        n = int(input("Integer: ")); f = 1
        for k in range(1, n + 1): f *= k
        print(f"Factorial: {f}")
    elif ch == "4":
        print("Exiting system. Goodbye!"); break
    else:
        print("Invalid selection. Please try again.")