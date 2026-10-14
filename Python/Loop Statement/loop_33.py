#33. Print reverse of a string.

s = input("Enter string: ")
rev_str = ""
for ch in s:
    rev_str = ch + rev_str
print(f"Reversed: {rev_str}")