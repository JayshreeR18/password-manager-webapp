import json
import os
from pathlib import Path

USERS_FILE = "users.json"

PASSWORDS_FILE = Path("passwords.json")


def load_passwords():
    if not PASSWORDS_FILE.exists():
        return {}
    with open(PASSWORDS_FILE, "r") as f:
        return json.load(f)
    
def save_password(username, website, login, encrypted_password):
    data = load_passwords()
    if username not in data:
        data[username] = []
    data[username].append({
        "website": website,
        "username": login,
        "password": encrypted_password
    })
    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=2)


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_user(username: str, hashed_password: str) -> bool:
    users = load_users()
    
    if username in users:
        return False  # user already exists

    users[username] = hashed_password

    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)
    
    return True  # user successfully added
