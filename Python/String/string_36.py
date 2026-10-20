# 36. Remove duplicate characters from a string.

text = input("enter a string:")
chars = "".join(dict.fromkeys(text))
print(chars)