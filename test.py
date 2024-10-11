"""
age = input("Enter ypur age: ")
int_age = int(age)
print(f"Your age is {int_age + 3}")


role = input("Enter your role: ")
admin_count = 0
if role == "admin":
    print("Hello Admin!")
    admin_count += 1
print(f"There are {admin_count} admin")

"""

grade = int(input("Enter your grade: "))
if grade > 96:
    print("1.0")
elif grade <= 96 and grade >= 94:
    print("1.25")
elif grade <= 93 and grade >= 91:
    print("1.5")
elif grade <= 90 and grade >= 88:
    print("1.75")
elif grade <= 87 and grade >= 85:
    print("2.0")
elif grade <= 84 and grade >= 82:
    print("2.25")
elif grade <= 81 and grade >= 79:
    print("2.5")
elif grade <= 78 and grade >= 76:
    print("2.75")
elif grade <= 75 and grade >= 73:
    print("3.0")
elif grade <= 72 and grade >= 70:
    print("3.25")
elif grade <= 69 and grade >= 67:
    print("3.5")
elif grade <= 66 and grade >= 64:
    print("3.75")
elif grade <= 63 and grade >= 61:
    print("4.0")
elif grade <= 60 and grade >= 58:
    print("4.25")
elif grade <= 57 and grade >= 55:
    print("4.5")
elif grade <= 54 and grade >= 52:
    print("4.75")
elif grade <= 51 and grade >= 0:
    print("5.0")