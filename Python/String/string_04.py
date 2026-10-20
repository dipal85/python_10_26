# 4. Count the number of vowels in a string.

text = input("Enter a String:")
vowels="aeiouAEIOU"
count=0

for char in text:
    if char in vowels:
        count += 1

print("number of vowels:",count)