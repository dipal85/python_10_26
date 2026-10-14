#23. Write a program to calculate electricity bill based on units consumed.

u = int(input("Units consumed: "))
if u <= 100:
    bill = u * 1.50
elif u <= 300:
    bill = (100 * 1.50) + ((u - 100) * 2.50)
else:
    bill = (100 * 1.50) + (200 * 2.50) + ((u - 300) * 4.00)
print(f"Total Bill: ₹{bill}")