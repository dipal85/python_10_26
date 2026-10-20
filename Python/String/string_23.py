# 23. Check whether a string is a palindrome.

text = input("Enter a string:")
clean = "".join(ch.lower() for ch in text if ch.isalnum())
down= clean ==clean[::-1]

print("is palidrome",down)