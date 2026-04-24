import csv
from connect import connect


# ─── CREATE TABLE ────────────────────────────────────────────────────────────

def create_table():
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    phone VARCHAR(20) NOT NULL
                );
            """)
    conn.close()
    print("Table 'phonebook' is ready.")


# ─── INSERT ──────────────────────────────────────────────────────────────────

def insert_from_csv(file_path):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            with open(file_path, newline='') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) == 2:
                        cur.execute(
                            "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                            (row[0].strip(), row[1].strip())
                        )
    conn.close()
    print("Contacts loaded from CSV.")


def insert_from_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
                (name, phone)
            )
    conn.close()
    print(f"Contact '{name}' added.")


# ─── UPDATE ──────────────────────────────────────────────────────────────────

def update_contact(old_name, new_name=None, new_phone=None):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute(
                    "UPDATE phonebook SET first_name=%s WHERE first_name=%s",
                    (new_name, old_name)
                )
            if new_phone:
                cur.execute(
                    "UPDATE phonebook SET phone=%s WHERE first_name=%s",
                    (new_phone, old_name)
                )
    conn.close()
    print(f"Contact '{old_name}' updated.")


# ─── QUERY ───────────────────────────────────────────────────────────────────

def query_all():
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("SELECT id, first_name, phone FROM phonebook ORDER BY id")
        rows = cur.fetchall()
    conn.close()
    if rows:
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    else:
        print("PhoneBook is empty.")


def query_by_name(name):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE first_name ILIKE %s",
            (f"%{name}%",)
        )
        rows = cur.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    else:
        print("No contacts found.")


def query_by_phone_prefix(prefix):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, first_name, phone FROM phonebook WHERE phone LIKE %s",
            (f"{prefix}%",)
        )
        rows = cur.fetchall()
    conn.close()
    if rows:
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15}")
    else:
        print("No contacts found.")


# ─── DELETE ──────────────────────────────────────────────────────────────────

def delete_by_name(name):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE first_name=%s", (name,))
    conn.close()
    print(f"Contact '{name}' deleted.")


def delete_by_phone(phone):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    conn.close()
    print(f"Contact with phone '{phone}' deleted.")


# ─── MENU ────────────────────────────────────────────────────────────────────

def menu():
    create_table()
    while True:
        print("""
=== PhoneBook ===
1. Show all contacts
2. Search by name
3. Search by phone prefix
4. Add from console
5. Load from CSV
6. Update contact
7. Delete by name
8. Delete by phone
0. Exit
""")
        choice = input("Choose: ").strip()

        if choice == '1':
            query_all()
        elif choice == '2':
            name = input("Enter name to search: ").strip()
            query_by_name(name)
        elif choice == '3':
            prefix = input("Enter phone prefix: ").strip()
            query_by_phone_prefix(prefix)
        elif choice == '4':
            insert_from_console()
        elif choice == '5':
            insert_from_csv('contacts.csv')
        elif choice == '6':
            old = input("Enter current name: ").strip()
            new_name = input("New name (leave blank to skip): ").strip() or None
            new_phone = input("New phone (leave blank to skip): ").strip() or None
            update_contact(old, new_name, new_phone)
        elif choice == '7':
            name = input("Enter name to delete: ").strip()
            delete_by_name(name)
        elif choice == '8':
            phone = input("Enter phone to delete: ").strip()
            delete_by_phone(phone)
        elif choice == '0':
            print("Bye!")
            break
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    menu()
