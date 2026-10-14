#14. Write a program to check whether a given character is uppercase or lowercase.

ch = input("Enter single char: ")
if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
else:
    print("Not an alphabetic letter")