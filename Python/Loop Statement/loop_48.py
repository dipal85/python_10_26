#48. Check whether number is strong number.

n = int(input("Enter number: "))
temp, s_sum = n, 0
while temp > 0:
    d = temp % 10
    f = 1
    for i in range(1, d + 1): f *= i
    s_sum += f; temp //= 10
print("Strong Number" if s_sum == n else "Not Strong")