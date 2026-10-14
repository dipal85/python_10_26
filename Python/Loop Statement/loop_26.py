#26. Print ASCII values of characters in a string.

s = input("Enter string: ")
for ch in s:
    print(f"{ch} -> {ord(ch)}")