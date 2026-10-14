#43. Calculate sum of cubes of first n numbers.

n = int(input("Enter n: "))
cube_sum = 0
for i in range(1, n + 1):
    cube_sum += i ** 3
print(f"Sum of cubes: {cube_sum}")