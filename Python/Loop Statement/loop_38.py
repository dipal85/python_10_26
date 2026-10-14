#38. Find smallest digit in a number.

n = abs(int(input("Enter number: ")))
min_d = 9
while n > 0:
    d = n % 10
    if d < min_d: min_d = d
    n //= 10
print(f"Smallest digit: {min_d}")