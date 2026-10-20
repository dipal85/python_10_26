# 34. Find the ASCII value of each character in a string.

text = input("Enter a string:")
order = {ch: ord(ch) for ch in text}
print(order)