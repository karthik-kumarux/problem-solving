def check_password_validity(password):
    
    if len(password) < 6 or len(password) > 12:
        return "Password length must be between 6 and 12 characters."
    
    
    lower = upper = digit = special = False
    
    
    special_chars = {'$', '#', '@', '!', '%', '^', '&', '*', '_'}
    
    
    for char in password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            digit = True
        elif char in special_chars:
            special = True

    
    if not lower:
        return "Password must contain at least one lowercase letter."
    if not upper:
        return "Password must contain at least one uppercase letter."
    if not digit:
        return "Password must contain at least one digit."
    if not special:
        return "Password must contain at least one special character from [$#@!%^&*_]."
    
    
    return True

def validate_passwords(passwords):
    valid_passwords = []
    for password in passwords.split(','):
        password = password.strip()  
        result = check_password_validity(password)
        if result == True:
            valid_passwords.append(password)
        else:
            print(f"Invalid password '{password}': {result}")
    

    return ','.join(valid_passwords)


passwords = input('Enter your passwords (comma-separated): ')
output = validate_passwords(passwords)
print("Valid passwords:", output)
