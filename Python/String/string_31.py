# 31. Remove punctuation marks from a string.

import string

text = input("Enter a sentence:")
clean = text.translate(str.maketrans("","",string.punctuation))
print(clean)