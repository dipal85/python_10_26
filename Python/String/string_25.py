# 25. Extract only alphabets from a string.

text = input("Enter a string:")
alpha = "".join(ch for ch in text if ch.isalpha())
print(alpha)