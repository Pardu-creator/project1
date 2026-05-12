import sqlite3
import hashlib
from datetime import datetime


DB_NAME = "users.db"


# ---------------- CONNECT ----------------
def get_connection():
    return sqlite3.connect(DB_NAME)


# ---------------- CREATE TABLE ----------------
def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TEXT,
        last_login TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


# ---------------- HASH PASSWORD ----------------
def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# ---------------- REGISTER ----------------
def register_user(username,password):

    if not username or len(username)<3:
        return False

    if not password or len(password)<4:
        return False

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    try:

        cursor.execute("""
        INSERT INTO users(
            username,
            password,
            created_at,
            last_login
        )
        VALUES(?,?,?,?)
        """,(
            username,
            hashed,
            str(datetime.now()),
            ""
        ))

        conn.commit()
        conn.close()

        return True

    except sqlite3.IntegrityError:
        conn.close()
        return False


# ---------------- LOGIN ----------------
def login_user(username,password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed = hash_password(password)

    cursor.execute("""
    SELECT *
    FROM users
    WHERE username=?
    AND password=?
    """,(username,hashed))

    user = cursor.fetchone()

    if user:

        cursor.execute("""
        UPDATE users
        SET last_login=?
        WHERE username=?
        """,(
            str(datetime.now()),
            username
        ))

        conn.commit()
        conn.close()

        return True

    conn.close()
    return False


# ---------------- TOTAL USERS ----------------
def total_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    """)

    count = cursor.fetchone()[0]

    conn.close()

    return count


# ---------------- GET USER ----------------
def get_user(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username,
           created_at,
           last_login
    FROM users
    WHERE username=?
    """,(username,))

    user = cursor.fetchone()

    conn.close()

    return user
