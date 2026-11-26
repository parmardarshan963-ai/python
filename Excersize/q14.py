"""
write a program to check weather a person's monthly income is greater than the avergae income of three given people.(if condition)
"""

person1 = 10000
person2 = 20000
person3 = 30000

average = (person1 + person2 + person3)/3

income = float(input("Enter YOur Monthly Income : "))
if income==average:
    print("Your Income is Equal to average of 3 person")
elif income>average:
    print("Your Income is greater than 3 peson's average income")
else:
    print("Your Income is Less than 3 peson's average income")