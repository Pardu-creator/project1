import sqlite3
import hashlib

DB = "users.db"


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def create_db():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


create_db()


def register_user(username,password):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users VALUES (?,?)",
            (
                username,
                hash_password(password)
            )
        )

        conn.commit()
        conn.close()
        return True

    except:
        conn.close()
        return False


def login_user(username,password):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM users
    WHERE username=?
    AND password=?
    """,(
        username,
        hash_password(password)
    ))

    user = cur.fetchone()

    conn.close()

    if user:
        return True

    return False
