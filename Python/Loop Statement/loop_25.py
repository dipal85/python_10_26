#25. Count consonants in a string.

s = input("Enter string: ").lower()
c_count = 0
for ch in s:
    if ch.isalpha() and ch not in "aeiou":
        c_count += 1
print(f"Consonant count: {c_count}")