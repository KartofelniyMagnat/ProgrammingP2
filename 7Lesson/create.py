# create.py
from connect import connect

def create_table(config):
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    phone VARCHAR(20)
                );
            """)
        conn.commit()
        print("✅ Table created successfully!")
