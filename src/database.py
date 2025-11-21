import sqlite3


def get_conn_and_cursor():
    conn = sqlite3.connect("hospital.db")
    return conn, conn.cursor()


def setup():
    conn, cursor = get_conn_and_cursor()

    design = [
        """
    create table if not exists users (
        user_id integer primary key autoincrement,
        username text not null unique check (length(username) >= 3 and length(username) <= 20),
        password text not null,
        role text not null check (role in ('doctor', 'receptionist', 'admin'))
    );
    """,
        """
    create table if not exists logs (
        log_id integer primary key autoincrement,
        action text not null,
        role text not null check (role in ('doctor', 'receptionist', 'admin')),
        timestamp text default current_timestamp,
        user_id integer references users(user_id),
        details text
    );
    """,
        """
    create table if not exists patients (
        patient_id integer primary key autoincrement,
        name text not null,
        contact text not null,
        diagnosis text,
        anonymized_name text,
        anonymized_contact text,
        date_added text default current_timestamp
    );
    """,
    ]

    cursor.execute("pragma foreign_keys = ON;")

    for query in design:
        cursor.execute(query)

    conn.commit()
    conn.close()


def insert_fake_data():
    queries = [
        """
    INSERT INTO users (username, password, role) VALUES
    ('admin', 'admin123', 'admin'),
    ('Dr_Bob', 'doc123', 'doctor'),
    ('Alice_recep', 'rec123', 'receptionist');
    """,
        """
    INSERT INTO patients (name, contact, diagnosis, anonymized_name, anonymized_contact) VALUES
    ('John Doe', '123-456-7890', 'Flu', 'ANON_1001', 'XXX-XXX-7890'),
    ('Jane Smith', '987-654-3210', 'Diabetes', 'ANON_1002', 'XXX-XXX-3210'),
    ('Alice Johnson', '555-666-7777', 'Hypertension', 'ANON_1003', 'XXX-XXX-7777');
    """,
    ]

    conn, cursor = get_conn_and_cursor()
    for query in queries:
        cursor.execute(query)

    conn.commit()
    conn.close()
