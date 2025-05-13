import base64
import hashlib
import string
import random

def generate_password():
    length = random.randint(8, 16)  # Random password length between 8 and 16

    if length < 8:
        raise ValueError("Password length should be at least 8 characters")

    # Ensure password includes at least one lowercase, one uppercase, one digit, and one special character
    chars = {
        'lower': random.choice(string.ascii_lowercase),
        'upper': random.choice(string.ascii_uppercase),
        'digit': random.choice(string.digits),
        # 'special': random.choice('!@#$%^&*()-_=+[]{};:,.<>?')
    }

    # Fill the rest with random characters from all categories
    all_chars = string.ascii_letters + string.digits #+ '!@#$%^&*()-_=+[]{};:,.<>?'
    rest = [random.choice(all_chars) for _ in range(length - 8)]

    # Combine all characters and shuffle
    password = list(chars.values()) + rest
    random.shuffle(password)
    return ''.join(password)



def hash_password_base64(password):
    # Hash the password using SHA-256
    sha256_hash = hashlib.sha256(password.encode()).digest()
    # Encode the hash in Base64
    base64_encoded = base64.b64encode(sha256_hash).decode()
    return base64_encoded

plain_password = generate_password()
hashed_password = hash_password_base64(plain_password)


print("Generated password:", plain_password)
print("Base64 SHA-256 hash:", hashed_password)
