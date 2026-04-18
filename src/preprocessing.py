import random
import string


def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))


def label_password(password):
    if len(password) < 6:
        return 0  # weak
    elif password.isalpha() or password.isdigit():
        return 0  # weak
    elif len(password) < 10:
        return 1  # medium
    else:
        return 2  # strong


if __name__ == "__main__":
    print(generate_strong_password())
    print(label_password("12345"))
    print(label_password("hello123"))
    print(label_password("XyZ@91#kLm!"))