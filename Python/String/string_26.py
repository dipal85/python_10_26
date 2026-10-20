# 26. Find the first and last occurrence of a character.

text = input("Enter the string:")
char = input("Enter Character:")

first=text.find(char)
end=text.rfind(char)

print(f"first: {first} last: {end}")