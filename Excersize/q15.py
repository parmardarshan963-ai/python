"""
write a program to check weather a student qualifies for a scolership(marks above 85 and attendance above 90%).(if condition)
"""

marks = float(input("Enter Your Marks :"))

if marks>=85:
    attendance = float(input("Enter Your Attendance :"))
    if attendance>=90:
        print("You Are Qualified for Scholorship")
    else:
        print("You Are not Qualified for Scholorship due to less Attendance")
else:
    print("Your Are not Qualified for Scholorship due to less Marks")