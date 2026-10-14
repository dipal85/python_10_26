#39. Count total words in a string.

s = input("Enter text: ").strip()
words = 0
in_w = False
for ch in s:
    if ch != " " and not in_w:
        words += 1; in_w = True
    elif ch == " ": in_w = False
print(f"Total words: {words}")