import random
import string

def generate_password(length=12):
    return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

print(generate_password())
