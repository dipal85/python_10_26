#27. Write a program to check login status based on username and password.

u = input("Username: ")
p = input("Password: ")
if u == "admin" and p == "pass123":
    print("Login successful")
else:
    print("Invalid credentials")