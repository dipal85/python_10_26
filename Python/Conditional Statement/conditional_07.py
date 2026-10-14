#7. Write a program to check whether a character is a vowel or consonant. 

ch = input("Enter character: ").lower()
if ch in "aeiou" and ch.isalpha():
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet letter")