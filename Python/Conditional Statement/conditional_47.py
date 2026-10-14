#47. Write a program to check user role (admin, user, guest) using match case.

role = input("Role (admin/user/guest): ").lower()
match role:
    case "admin":
        print("Access: Full Root Permissions")
    case "user":
        print("Access: Standard Member Privileges")
    case "guest":
        print("Access: Read-Only Access")
    case _:
        print("Access Denied: Unknown role")