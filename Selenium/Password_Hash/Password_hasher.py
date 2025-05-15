import base64
import hashlib
import string
import random
import bcrypt

# def generate_password():
#     length = random.randint(8, 16)  # Random password length between 8 and 16
#
#     if length < 8:
#         raise ValueError("Password length should be at least 8 characters")
#
#     # Ensure password includes at least one lowercase, one uppercase, one digit, and one special character
#     chars = {
#         'lower': random.choice(string.ascii_lowercase),
#         'upper': random.choice(string.ascii_uppercase),
#         'digit': random.choice(string.digits),
#         # 'special': random.choice('!@#$%^&*()-_=+[]{};:,.<>?')
#     }
#
#     # Fill the rest with random characters from all categories
#     all_chars = string.ascii_letters + string.digits #+ '!@#$%^&*()-_=+[]{};:,.<>?'
#     rest = [random.choice(all_chars) for _ in range(length - 8)]
#
#     # Combine all characters and shuffle
#     password = list(chars.values()) + rest
#     random.shuffle(password)
#     return ''.join(password)

def generate_password():
    length = random.randint(8, 16)  # desired total length

    # Define your mandatory categories (add/remove as you like)
    mandatory = {
        'lower':  random.choice(string.ascii_lowercase),
        'upper':  random.choice(string.ascii_uppercase),
        'digit':  random.choice(string.digits),
        # 'special':random.choice('!@#$%^&*()-_=+[]{};:,.<>?')
    }

    if length < len(mandatory):
        raise ValueError(
            f"Password length must be at least {len(mandatory)}"
        )

    all_chars = string.ascii_letters + string.digits# + '!@#$%^&*()-_=+[]{};:,.<>?'
    # Fill the rest to hit the exact desired length
    rest = [
        random.choice(all_chars)
        for _ in range(length - len(mandatory))
    ]

    # Combine and shuffle
    password_chars = list(mandatory.values()) + rest
    random.shuffle(password_chars)
    return ''.join(password_chars)

#
# def hash_password_base64(password):
#     # Hash the password using SHA-256
#     sha256_hash = hashlib.sha256(password.encode()).digest()
#     # Encode the hash in Base64
#     base64_encoded = base64.b64encode(sha256_hash).decode()
#     return base64_encoded
#
# plain_password = generate_password()
# hashed_password = hash_password_base64(plain_password)
#
#
# print("Generated password:", plain_password)
# print("Base64 SHA-256 hash:", hashed_password)



def hash_password_bcrypt(password: str) -> str:

    # Generate a salt and hash
    salt = bcrypt.gensalt(10)  # The Backend uses 10 rounds salting when sending the password to the database.
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

plain_password = generate_password()
bcrypt_hash = hash_password_bcrypt(plain_password)

print("Generated password:", plain_password)
print("Bcrypt hash:", bcrypt_hash)

# def check_password(password: str, hashed: str) -> bool:
#     return bcrypt.checkpw(password.encode(), hashed.encode())
#
# assert check_password(plain_password, bcrypt_hash)
# print(f'Plain: {plain_password}, Bcrypt: {bcrypt_hash}')


# def verify_bcrypt_password(password: str, hashed: str, expected_rounds: int = None):
#
#     # Check password validity
#     is_valid = bcrypt.checkpw(password.encode(), hashed.encode())
#
#     actual_rounds = None
#     try:
#         parts = hashed.split('$')
#         if len(parts) >= 3:
#             actual_rounds = int(parts[2])
#     except ValueError:
#         actual_rounds = None
#
#     # Display results
#     print(f"\nPassword matches hash: {is_valid}")
#     if expected_rounds is not None:
#         if actual_rounds is None:
#             print("Could not determine the number of rounds from the hash.")
#         else:
#             rounds_check = (actual_rounds == expected_rounds)
#             print(f"Hash uses expected rounds ({expected_rounds}): {rounds_check} (actual rounds: {actual_rounds})")

# verify_bcrypt_password(input("Password: "), input("Hash: "), int(input("Rounds: ")))



def verify_bcrypt_password(password: str, hashed: str) -> None:

    bcrypt_rounds = 10

    # 1) Check password validity
    is_valid = bcrypt.checkpw(password.encode(), hashed.encode())

    # 2) Extract actual rounds from the hash ($2b$10$...)
    actual_rounds = None
    parts = hashed.split('$')
    if len(parts) >= 3:
        try:
            actual_rounds = int(parts[2])
        except ValueError:
            pass

    # 3) Display results
    print(f"\nPassword matches hash: {is_valid}")
    if actual_rounds is None:
        print("Could not determine the number of rounds from the hash.")
    else:
        rounds_check = (actual_rounds == bcrypt_rounds)
        # print(
        #     f"Hash uses default rounds ({bcrypt_rounds}): "
        #     f"{rounds_check} (actual rounds: {actual_rounds})"
        # )

# verify_bcrypt_password(input("Password: "), input("Hash: "))
verify_bcrypt_password(plain_password, bcrypt_hash)
