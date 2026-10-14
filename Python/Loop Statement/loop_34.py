#34. Check whether a string is palindrome.

s = input("Enter string: ")
is_p = True
n = len(s)
for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        is_p = False; break
print("Palindrome" if is_p else "Not Palindrome")