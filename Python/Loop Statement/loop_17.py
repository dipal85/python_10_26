#17. Find largest digit in a number.

n = abs(int(input("Enter number: ")))
max_d = 0
while n > 0:
    d = n % 10
    if d > max_d: max_d = d
    n //= 10
print(f"Largest digit: {max_d}")