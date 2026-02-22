import re

def is_valid_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    # Example for Vietnamese phone numbers
    pattern = r"^(0[3|5|7|8|9])+([0-9]{8})$"
    return bool(re.match(pattern, phone))
