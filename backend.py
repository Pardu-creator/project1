import sqlite3
import hashlib
from datetime import datetime

conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    created_at TEXT,
    last_login TEXT
)
""")

conn.commit()


def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register_user(username,password):

    if len(username)<3:
        return False

    if len(password)<4:
        return False

    hashed=hash_password(password)

    try:
        cursor.execute("""
        INSERT INTO users(
        username,password,
        created_at,last_login
        )
        VALUES(?,?,?,?)
        """,(
            username,
            hashed,
            str(datetime.now()),
            ""
        ))

        conn.commit()
        return True

    except:
        return False


def login_user(username,password):

    hashed=hash_password(password)

    cursor.execute("""
    SELECT * FROM users
    WHERE username=?
    AND password=?
    """,(username,hashed))

    user=cursor.fetchone()

    if user:

        cursor.execute("""
        UPDATE users
        SET last_login=?
        WHERE username=?
        """,(str(datetime.now()),username))

        conn.commit()

        return True

    return False


def total_users():

    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    """)

    return cursor.fetchone()[0]
