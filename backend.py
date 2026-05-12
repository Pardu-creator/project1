import sqlite3
import hashlib
import os

DB_NAME = "users.db"


# Create database
def create_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Register
def register_user(username, password):

    if not username or not password:
        return False

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users (username,password) VALUES (?,?)",
            (
                username,
                hash_password(password)
            )
        )

        conn.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        conn.close()


# Login
def login_user(username, password):

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (
            username,
            hash_password(password)
        )
    )

    user = c.fetchone()

    conn.close()

    return user is not None


# Initialize DB
create_db()
