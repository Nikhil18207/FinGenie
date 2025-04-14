# utils/helpers.py

from dotenv import load_dotenv
import os

load_dotenv()

def get_env_var(key):
    return os.getenv(key)
