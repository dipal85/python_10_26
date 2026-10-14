#28. Check whether a number is Armstrong.

n = int(input("Enter number: "))
p = len(str(n))
temp, arm_sum = n, 0
while temp > 0:
    arm_sum += (temp % 10) ** p
    temp //= 10
print("Armstrong" if arm_sum == n else "Not Armstrong")