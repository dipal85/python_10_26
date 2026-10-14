#12. Reverse a number using while loop.

n = int(input("Enter number: "))
temp = abs(n)
rev = 0
while temp > 0:
    rev = (rev * 10) + (temp % 10)
    temp //= 10
print(f"Reversed: {-rev if n < 0 else rev}")