'''Write a Python program to check the validity of passwords input by users.
Validation :

At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters'''

def is_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special_char = False
    special_chars = "$#@"
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
        if has_lowercase and has_uppercase and has_digit and has_special_char:
            return True
    return False

password = input("Enter your password: ")
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. Make sure it meets the required criteria.")
