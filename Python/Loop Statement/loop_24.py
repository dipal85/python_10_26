#24. Count vowels in a string.

s = input("Enter string: ").lower()
v_count = 0
for ch in s:
    if ch in "aeiou": v_count += 1
print(f"Vowel count: {v_count}")