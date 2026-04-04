# insert.py
import csv
from connect import connect

def insert_from_console(config):
    with connect(config) as conn:
        with conn.cursor() as cur:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
    print("✅ Added successfully!")

def insert_from_csv(config, file_path):
    with connect(config) as conn:
        with conn.cursor() as cur:
            with open(file_path, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
        conn.commit()
    print("✅ CSV data uploaded!")