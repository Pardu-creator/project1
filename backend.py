import sqlite3
import hashlib

DB = "users.db"


def connect():
    return sqlite3.connect(DB)


def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


def hash_pass(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register_user(username,password):

    conn=connect()
    cur=conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users VALUES (?,?)",
            (username,hash_pass(password))
        )

        conn.commit()
        conn.close()
        return True

    except:
        conn.close()
        return False


def login_user(username,password):

    conn=connect()
    cur=conn.cursor()

    cur.execute("""
    SELECT *
    FROM users
    WHERE username=?
    AND password=?
    """,(username,hash_pass(password)))

    user=cur.fetchone()

    conn.close()

    return user is not None
