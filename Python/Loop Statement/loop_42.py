#42. Calculate sum of squares of first n numbers.

n = int(input("Enter n: "))
sq_sum = 0
for i in range(1, n + 1):
    sq_sum += i * i
print(f"Sum of squares: {sq_sum}")