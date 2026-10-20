# 21. Find the length of a string without using len().

text = input("Enter a String:")
count = sum(1 for _ in text)
print(count)