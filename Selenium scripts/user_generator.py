import random
import string

def generate_username(length=8):
    characters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(characters) for _ in range(length))
    return username

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


formats = [
    "%Y-%m-%d",        # 2024-11-30
    "%d/%m/%Y",        # 30/11/2024
    "%m-%d-%Y",        # 11-30-2024
    "%B %d, %Y",      # November 30, 2024
    "%b %d, %Y",      # Nov 30, 2024
    "%Y/%m/%d",       # 2024/11/30
    "%d %B %Y",       # 30 November 2024
    "%d %b %Y",       # 30 Nov 2024
    "%m/%d/%Y",       # 11/30/2024
    "%Y.%m.%d",       # 2024.11.30
    "%d-%m-%Y",       # 30-11-2024
    "%Y%m%d",         # 20241130
    "%A, %d %B %Y",   # Saturday, 30 November 2024
    "%a, %d %b %Y",   # Sat, 30 Nov 2024
    "%d %m %Y",       # 30 11 2024
]

