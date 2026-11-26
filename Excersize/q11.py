"""
    11.write a program to check weather a password length is at least 8 characters.(if condition)
"""

password = input("Enter Password :")

if len(password)>=8:
    print("Valid Password.")
else:
    print("Use at least 8 character password.")