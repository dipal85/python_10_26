#11. Count number of digits in a number.

n = abs(int(input("Enter number: ")))
count = 1 if n == 0 else 0
while n > 0:
    count += 1
    n //= 10
print(f"Total digits: {count}")