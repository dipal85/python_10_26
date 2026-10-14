#32. Calculate power of a number without using pow().

base = float(input("Base: "))
exp = int(input("Exponent: "))
result = 1.0
for _ in range(abs(exp)):
    result *= base
if exp < 0: result = 1 / result
print(f"Result: {result}")