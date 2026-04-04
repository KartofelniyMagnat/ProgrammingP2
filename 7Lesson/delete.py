# delete.py
from connect import connect

def delete_by_name(config, name):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))
        conn.commit()
    print("✅ Deleted successfully!")

def delete_by_phone(config, phone):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
        conn.commit()
    print("✅ Deleted successfully!")