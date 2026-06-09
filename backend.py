import json
import os
import hashlib

USER_FILE = "users.json"


def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    username = username.strip()

    if username == "" or password == "":
        return False

    users = load_users()

    if username in users:
        return False

    users[username] = hash_password(password)
    save_users(users)

    return True


def login_user(username, password):
    username = username.strip()

    if username == "" or password == "":
        return False

    users = load_users()

    if username not in users:
        return False

    return users[username] == hash_password(password)
