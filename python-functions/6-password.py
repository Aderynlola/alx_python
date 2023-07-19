def validate_password(password):
    if len(password) < 8:
        return False

    uppercase = False
    lowercase = False
    digit = False

    for char in password:
        if char.isupper():
            uppercase = True
        elif char.islower():
            lowercase = True
        elif char.isdigit():
            digit = True

    if not (uppercase and lowercase and digit):
        return False

    if ' ' in password:
        return False

    return True
