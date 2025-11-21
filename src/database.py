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
    from encryption_utils import encrypt
    from hash_utils import hash_password
    
    queries = [
        f"""
    INSERT INTO users (username, password, role) VALUES
    ('admin', '{hash_password('admin123')}', 'admin'),
    ('Dr_Bob', '{hash_password('doc123')}', 'doctor'),
    ('Alice_recep', '{hash_password('rec123')}', 'receptionist');
    """,
        f"""
    INSERT INTO patients (name, contact, diagnosis) VALUES
    ('{encrypt('John Doe')}', '{encrypt('123-456-7890')}', 'Flu'),
    ('{encrypt('Jane Smith')}', '{encrypt('987-654-3210')}', 'Diabetes'),
    ('{encrypt('Alice Johnson')}', '{encrypt('555-666-7777')}', 'Hypertension');
    """,
    ]

    conn, cursor = get_conn_and_cursor()
    
    try:
        for query in queries:
            print(query)
            cursor.execute(query)

        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()

# setup()
# insert_fake_data()