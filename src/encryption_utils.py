from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()


def generate_key():
    print(Fernet.generate_key().decode())  # to save in .env


# _generate_key()
# print(os.environ["FERNET_KEY"])


fernet = Fernet(os.environ["FERNET_KEY"])

def encrypt(text: str):
    return fernet.encrypt(text.encode()).decode()


def decrypt(text: str):
    return fernet.decrypt(text.encode()).decode()
