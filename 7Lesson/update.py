# update.py
from connect import connect

def update_data(config, name, new_name=None, new_phone=None):
    with connect(config) as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute("UPDATE phonebook SET first_name=%s WHERE first_name=%s", (new_name, name))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone=%s WHERE first_name=%s", (new_phone, name))
        conn.commit()
    print("✅ Updated successfully!")