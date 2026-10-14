#13. Check whether a number is palindrome.

n = int(input("Enter number: "))
orig, rev = n, 0
while n > 0:
    rev = (rev * 10) + (n % 10)
    n //= 10
print("Palindrome" if orig == rev else "Not Palindrome")