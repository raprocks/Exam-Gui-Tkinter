import sqlite3
from typing import List
import bcrypt

# create tables


def create_tables(con: sqlite3.Connection):
    SQL_SCRIPT = """
        CREATE TABLE IF NOT EXISTS subjects(
            sub_id int AUTO INCREMENT,
            name varchar(20) NOT NULL,
            questions_file_path varchar(200) NOT NULL,
            PRIMARY KEY (sub_id)
        );
        CREATE TABLE IF NOT EXISTS users(
            username varchar(20) NOT NULL,
            password_hash varchar(100) NOT NULL,
            is_admin bool NOT NULL
        );
        CREATE TABLE IF NOT EXISTS results(
            rec_id int AUTO INCREMENT,
            username varchar(20) NOT NULL,
            subject varchar(20) NOT NULL,
            result int NOT NULL,
            PRIMARY KEY (rec_id)
        );
    """
    con.executescript(SQL_SCRIPT)
    add_user(con, "admin", "admin", True)

# utils


def gen_password_hash(password: str) -> bytes:
    password_bytes = password.encode("utf-8")
    pass_salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password=password_bytes, salt=pass_salt)
    return hashed_pass


def check_pass(password: str, pass_hash: bytes) -> bool:
    password_bytes = password.encode('utf-8')
    pass_check = bcrypt.checkpw(password_bytes, pass_hash)
    return pass_check


# user funcs
"""
add delete verify
"""


def add_user(con: sqlite3.Connection, username: str, password: str, admin: bool):
    pass_hash = gen_password_hash(password)
    con.execute("INSERT INTO users VALUES (?,?,?)",
                (username, pass_hash, admin))
    con.commit()


def remove_user(con: sqlite3.Connection, username: str):
    con.execute("DELETE FROM users WHERE username=?", (username,))
    con.commit()


def check_user(con: sqlite3.Connection, username: str, password: str) -> bool:
    user = con.execute("SELECT * FROM users WHERE username=?", (
        username,)).fetchone()
    if user:
        res = check_pass(password, user[1])
        if res:
            return True
    return False


def get_user(con: sqlite3.Connection, username: str) -> List:
    user = con.execute("SELECT * FROM users WHERE username=?", (
        username,)).fetchone()
    return user


# subject
'''
get add update
'''


def get_subjects(con: sqlite3.Connection) -> List:
    subjects = con.execute("SELECT * FROM subjects").fetchall()
    return subjects


def add_subject(con: sqlite3.Connection, sub_name: str, fpath: str):
    con.execute(
        "INSERT INTO subjects (name, questions_file_path) VALUES (?,?)", (sub_name, fpath))
    con.commit()
# result


def save_result(con: sqlite3.Connection, user: str, subject: str, result: int):
    con.execute(
        "INSERT INTO results (username, subject, result) VALUES (?,?,?)", (user, subject, result))
    con.commit()


def get_results(con: sqlite3.Connection):
    results = con.execute("SELECT * FROM results").fetchall()
    return results


if __name__ == "__main__":
    print("Check Hashed Passwords Here")
    password = input("Enter a Password to hash : ")
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    pass_hash = bcrypt.hashpw(password_bytes, salt)
    print("Password's Hash is", pass_hash)
    print("Enter Another Password to check if the earlier one is same as this one")
    new_pass = input("New Password : ")
    new_pass_bytes = new_pass.encode('utf-8')
    new_pass_hash = bcrypt.hashpw(new_pass_bytes, salt)
    print("New Password's hash is", new_pass_hash)
    print("Checking if both passwords are same without equating them. This uses bcrypt to do the same")
    if bcrypt.checkpw(new_pass_hash, pass_hash):
        print("Password matches")
    else:
        print("Password does not match")
