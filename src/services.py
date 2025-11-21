import sqlite3
from database import get_conn_and_cursor
from enum import Enum
import pandas as pd


class ActionsEnum(Enum):
    LOGIN = "LOGIN"


def log_action(user_id: int, role, action, details=None):
    conn, cursor = get_conn_and_cursor()

    try:
        query = "insert into logs (user_id, role, action, details) values (?, ?, ?, ?)"
        cursor.execute(query, (user_id, role, action, details))
        conn.commit()
    except sqlite3.Error as e:
        print("\nSQLITE ERROR:", e)
        conn.rollback()


def login(username: str, password: str):
    conn, cursor = get_conn_and_cursor()
    # todo: hash pw
    query = "select user_id, role from users where username = ? and password = ?"
    cursor.execute(query, (username, password))
    row = cursor.fetchone()

    if row is None:
        return None

    user_id, role = row

    log_action(user_id, role, action=ActionsEnum.LOGIN)
    conn.close()
    return {"user_id": user_id, "role": role}


def get_patients(role: str):
    conn, cursor = get_conn_and_cursor()

    if role == "admin":
        cols = "*"
    elif role == "doctor":
        cols = "anonymized_name, anonymized_contact, patient_id, diagnosis, date_added"
    elif role == "receptionist":
        cols = ""
    else:
        raise ValueError("Invalid role provided")

    query = f"select {cols} from patients"
    df = pd.read_sql_query(con=conn, sql=query)


    conn.close()
    return df
