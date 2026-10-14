#40. Write a program to check whether a password is valid using nested if.

pwd = input("Enter password: ")
if len(pwd) >= 8:
    if any(c.isdigit() for c in pwd):  # syntax gen
        print("Valid Password")
    else:
        print("Invalid: Requires at least 1 digit")
else:
    print("Invalid: Minimum length is 8 chars")