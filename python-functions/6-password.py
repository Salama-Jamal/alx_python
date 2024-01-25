def validate_password(password):
    # Check the length
    if len(password) < 8:
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for spaces
    if ' ' in password:
        return False
    
    return True