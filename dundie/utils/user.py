from random import sample
from string import ascii_letters, digits


def generate_simple_password(size=8) -> str:
    """Generate a simple random password
    [A_Z][a-z][0-9]
    """
    password = sample(ascii_letters + digits, size)
    return "".join(password)
