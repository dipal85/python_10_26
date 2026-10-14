#47. Find product of digits of a number.

n = abs(int(input("Enter number: ")))
prod = 1 if n > 0 else 0
while n > 0:
    prod *= (n % 10)
    n //= 10
print(f"Product of digits: {prod}")