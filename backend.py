import sqlite3
import hashlib

DB = "users.db"


def create_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users VALUES (?,?)",
            (username, hash_password(password))
        )
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()


def login_user(username, password):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, hash_password(password))
    )

    user = c.fetchone()

    conn.close()

    return user is not None


create_db()
