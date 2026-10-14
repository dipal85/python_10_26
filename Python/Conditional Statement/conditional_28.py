#28. Write a program to calculate discounts based on total shopping amount.

amt = int(input("Total bill: "))
if amt >= 5000:
    disc = amt * 0.20
elif amt >= 2000:
    disc = amt * 0.10
else:
    disc = 0.0
print(f"Payable: {amt - disc}")