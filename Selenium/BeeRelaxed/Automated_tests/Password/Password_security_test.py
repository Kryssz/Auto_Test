import string
import random
import bcrypt


def generate_password():
    length = random.randint(8, 16)  # desired total length

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
    rest = [
        random.choice(all_chars)
        for _ in range(length - len(mandatory))
    ]

    password_chars = list(mandatory.values()) + rest
    random.shuffle(password_chars)
    return ''.join(password_chars)


def hash_password_bcrypt(password: str) -> str:

    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def verify_bcrypt_password(password: str, hashed: str) -> None:

    is_valid = bcrypt.checkpw(password.encode(), hashed.encode())

    actual_rounds = None
    parts = hashed.split('$')
    if len(parts) >= 3:
        try:
            actual_rounds = int(parts[2])
        except ValueError:
            pass

    print(f"\nPassword matches hash: {is_valid}")

