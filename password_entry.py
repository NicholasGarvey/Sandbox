# Hi this is Nicholas
password = input("Please enter a password")
count_lower = 0
count_upper = 0
for char in password:
    if char.islower():
        count_lower += 1
    elif char.isupper():
        count_upper += 1
if count_lower >= 10 or count_upper >= 10:
    for char in password:
        print("*", end='')
