#15. Find sum of digits of a number.

n = abs(int(input("Enter number: ")))
digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10
print(f"Sum of digits: {digit_sum}")