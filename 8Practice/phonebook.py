from connect import connect


# ─── SETUP ────────────────────────────────────────────────────────────────────

def setup():
    """Create table and load all DB functions/procedures from SQL files."""
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id         SERIAL PRIMARY KEY,
                    first_name VARCHAR(50) NOT NULL,
                    phone      VARCHAR(20) NOT NULL
                );
            """)
            for sql_file in ('functions.sql', 'procedures.sql'):
                with open(sql_file, 'r') as f:
                    cur.execute(f.read())
    conn.close()
    print("Database ready (table + functions/procedures loaded).")


# ─── WRAPPERS FOR FUNCTIONS ───────────────────────────────────────────────────

def search_contacts(pattern: str):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        rows = cur.fetchall()
    conn.close()
    return rows


def get_contacts_page(limit: int, offset: int):
    conn = connect()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM get_contacts_page(%s, %s)", (limit, offset))
        rows = cur.fetchall()
    conn.close()
    return rows


# ─── WRAPPERS FOR PROCEDURES ──────────────────────────────────────────────────

def upsert_contact(name: str, phone: str):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.close()


def insert_many_contacts(names: list, phones: list):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "CALL insert_many_contacts(%s::varchar[], %s::varchar[])",
                (names, phones)
            )
            cur.execute("SELECT * FROM bulk_insert_errors")
            bad_rows = cur.fetchall()
    conn.close()
    return bad_rows


def delete_contact(name: str = None, phone: str = None):
    conn = connect()
    with conn:
        with conn.cursor() as cur:
            cur.execute("CALL delete_contact(%s, %s)", (name, phone))
    conn.close()


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def print_rows(rows):
    if not rows:
        print("  (no records)")
        return
    print(f"  {'ID':<5} {'Name':<20} {'Phone':<15}")
    print("  " + "-" * 42)
    for row in rows:
        print(f"  {row[0]:<5} {row[1]:<20} {row[2]:<15}")


# ─── MENU ─────────────────────────────────────────────────────────────────────

def menu():
    setup()
    while True:
        print("""
=== PhoneBook (Practice 8) ===
1. Search contacts by pattern
2. Show page of contacts
3. Upsert contact (insert or update)
4. Bulk insert contacts (with validation)
5. Delete contact by name
6. Delete contact by phone
0. Exit
""")
        choice = input("Choose: ").strip()

        if choice == '1':
            pattern = input("  Pattern: ").strip()
            rows = search_contacts(pattern)
            print_rows(rows)

        elif choice == '2':
            try:
                limit  = int(input("  Page size (limit): ").strip())
                offset = int(input("  Offset (0 = first page): ").strip())
            except ValueError:
                print("  Invalid numbers.")
                continue
            rows = get_contacts_page(limit, offset)
            print_rows(rows)

        elif choice == '3':
            name  = input("  Name: ").strip()
            phone = input("  Phone: ").strip()
            upsert_contact(name, phone)
            print(f"  Done — '{name}' upserted.")

        elif choice == '4':
            raw = input("  Enter pairs as  name:phone,name:phone,...\n  > ").strip()
            names, phones = [], []
            for pair in raw.split(','):
                parts = pair.strip().split(':')
                if len(parts) == 2:
                    names.append(parts[0].strip())
                    phones.append(parts[1].strip())
            if not names:
                print("  No valid pairs entered.")
                continue
            bad = insert_many_contacts(names, phones)
            print(f"  Inserted/updated {len(names) - len(bad)} record(s).")
            if bad:
                print("  Invalid entries (not saved):")
                for row in bad:
                    print(f"    name={row[0]!r}  phone={row[1]!r}  reason={row[2]}")

        elif choice == '5':
            name = input("  Name to delete: ").strip()
            delete_contact(name=name)
            print(f"  Deleted contacts with name '{name}'.")

        elif choice == '6':
            phone = input("  Phone to delete: ").strip()
            delete_contact(phone=phone)
            print(f"  Deleted contacts with phone '{phone}'.")

        elif choice == '0':
            print("Bye!")
            break
        else:
            print("  Invalid choice.")


if __name__ == '__main__':
    menu()
