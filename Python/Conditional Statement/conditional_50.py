balance = 50000.0
opt = int(input("1:Bal 2:Withdraw 3:Deposit > "))
match opt:
    case 1:
        print(f"Current Balance: ₹{balance}")
    case 2:
        amt = float(input("Amount: "))
        if 0 < amt <= balance:
            print(f"Remaining: ₹{balance - amt}")
        else:
            print("Insufficient or invalid amount")
    case 3:
        dep = float(input("Deposit: "))
        print(f"New Balance: ₹{balance + dep}")
    case _:
        print("Invalid selection")