import re

password_input = input()

def password_validator(password):
    if len(password) not in range(6, 10 + 1):
        return "Password must be between 6 and 10 characters"

    check = bool(re.match("^[A-Za-z0-9]*$", password))
    if not check:
        return "Password must consist only of letters and digits"

    occurrence = 0
    for char in password:
        if char.isdigit():
            occurrence += 1
    if occurrence < 2:
        return "Password must have at least 2 digits"

    return "Password is valid"

print(password_validator(password_input))