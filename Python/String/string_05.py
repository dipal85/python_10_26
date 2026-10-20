# 5. Count the number of consonants in a string.

text = input("enter a string:")
vowels= "aeiouAEIOU"
count = 0

for char in text:
    if char.isalpha() and char not in vowels:
        count +=1

print("Number of consonants:",count)