#22. Find sum of even digits in a number.

n = abs(int(input("Enter number: ")))
even_sum = 0
while n > 0:
    d = n % 10
    if d % 2 == 0: even_sum += d
    n //= 10
print(f"Sum of even digits: {even_sum}")