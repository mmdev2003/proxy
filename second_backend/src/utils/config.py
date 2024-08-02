import os

from dotenv import load_dotenv

load_dotenv()

env = {
    "CRYPTO_KEY": os.environ.get("CRYPTO_KEY"),
    "DB_USER": os.environ.get("POSTGRES_USER"),
    "DB_PASS": os.environ.get("POSTGRES_PASSWORD"),
    "DB_HOST": os.environ.get("POSTGRES_HOST"),
    "DB_PORT": int(os.environ.get("POSTGRES_PORT")),
    "DB_NAME": os.environ.get("POSTGRES_DB"),
    "SECOND_BACKEND": os.environ.get("SECOND_BACKEND"),
    "FIRST_BACKEND": os.environ.get("FIRST_BACKEND")
}


def get(key):
    return env[key]

