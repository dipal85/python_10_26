#23. Find sum of odd digits in a number.

n = abs(int(input("Enter number: ")))
odd_sum = 0
while n > 0:
    d = n % 10
    if d % 2 != 0: odd_sum += d
    n //= 10
print(f"Sum of odd digits: {odd_sum}")