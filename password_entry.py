# Hi this is Nicholas
min_length = 10
password = input("Please enter a password with {} characters".format(min_length))
while len(password) < min_length:
    password = input("Enter password of at least {} characters: ".format(min_length))
print('*' * len(password))
