"""
write a program to check weather a number is a 3-digit number and it's last digit is 7.(if condition)
"""

number = int(input("Enter Any 3 digit number :"))

if number >= 100 and number <= 999:
    if number%10==7:
        print("Valid Number")
    else:
        print("Last Digit Should be 7")
else:
    print("Number Should be 3 digit")