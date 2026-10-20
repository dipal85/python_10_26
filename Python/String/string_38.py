# 38. Find the shortest word in a sentence.

text = input("Enter the sentence:")
words = text.split()
short = min(words, key=len) if words else ""
print(short)