'''
47. Write a program to check user role (admin, user, guest) using match case.
'''
role = input("Enter role (admin/user/guest): ").lower()

match role:
    case "admin":
        print("Full access: can manage users and settings")
    case "user":
        print("Standard access: can use the application")
    case "guest":
        print("Limited access: view only")
    case _:
        print("Unknown role")
