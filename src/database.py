import sqlite3

conn = sqlite3.connect("hospital.db")

cursor = conn.cursor()

design = """

create table if not exists users (
    id integer primary key
);

"""

conn.execute(design)

conn.commit()
