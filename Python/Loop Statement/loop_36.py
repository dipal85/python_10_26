#36. Find sum of numbers entered by user until 0 is entered.

acc = 0
while True:
    val = float(input("Enter val (0 to end): "))
    if val == 0: break
    acc += val
print(f"Total sum: {acc}")