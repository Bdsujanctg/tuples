import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password too short! Try something longer 💬"

    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    
    all_chars = lower + upper + digits
    password_chars += random.choices(all_chars, k=length - 3)

    
    random.shuffle(password_chars)

    
    return ''.join(password_chars)


print("Your new random password is:", generate_password(12))
