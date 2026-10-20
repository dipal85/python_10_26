# 37. Find the longest word in a sentence.

text = input("Enter a Sentence:")
words = text.split()
long = max(words, key=len) if words else ""
print("longest word",long)