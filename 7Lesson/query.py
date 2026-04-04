# query.py
from connect import connect

def query_all(config):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook")
            rows = cur.fetchall()
            for row in rows:
                print(row)

def query_by_name(config, name):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE first_name=%s", (name,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

def query_by_phone(config, phone):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE phone=%s", (phone,))
            rows = cur.fetchall()
            for row in rows:
                print(row)