# 27. Check whether a word exists in a sentence.

text = input("Enter a Sentence:")
deal = input("Enter word to check:")

words = text.lower().split()
print(deal.lower() in words)