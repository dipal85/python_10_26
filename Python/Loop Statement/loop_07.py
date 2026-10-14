#7. Calculate factorial of a number using for loop.

n = int(input("Enter n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial: ",{fact})