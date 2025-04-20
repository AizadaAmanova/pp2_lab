import psycopg2
import csv
import sys

DSN = {
    'host':     'localhost',
    'database': 'phonebook2',
    'user':     'postgres',
    'password': '12345'
}

def search_contacts(cur):
    pattern = input("Enter search pattern (name or phone): ").strip()
    cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
    rows = cur.fetchall()
    if not rows:
        print("No matches found.\n")
    else:
        print("\nID | Name                 | Phone")
        print("---+----------------------+---------------")
        for _id, name, phone in rows:
            print(f"{_id:2d} | {name:20s} | {phone}")
    print()

def upsert_contact(cur, conn):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print("Contact inserted or updated successfully.\n")

def batch_insert_from_csv(cur, conn):
    path = input("Enter CSV file path: ").strip()
    try:
        with open(path, newline='', encoding='latin1') as f:
            reader = csv.DictReader(f)
            inputs = [(r['name'], r['phone']) for r in reader]
    except Exception as e:
        print("Failed to read CSV:", e)
        return

    if not inputs:
        print("CSV is empty or missing headers.\n")
        return

    names = [pair[0] for pair in inputs]
    phones = [pair[1] for pair in inputs]

    cur.callproc("insert_many_users", (names, phones))
    bad_data = cur.fetchone()[0]
    conn.commit()

    if bad_data:
        print("Invalid entries (not inserted):")
        for entry in bad_data:
            print(" -", entry)
    else:
        print("All contacts inserted successfully.")
    print()

def paginate_contacts(cur):
    try:
        limit = int(input("Enter limit: ").strip() or 5)
        offset = int(input("Enter offset: ").strip() or 0)
    except ValueError:
        print("Please enter valid integers.\n")
        return

    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    if not rows:
        print("No records found.\n")
    else:
        print(f"\nShowing {limit} rows starting from offset {offset}:")
        print("ID | Name                 | Phone")
        print("---+----------------------+---------------")
        for _id, name, phone in rows:
            print(f"{_id:2d} | {name:20s} | {phone}")
    print()

def delete_contact(cur, conn):
    identifier = input("Enter name or phone to delete: ").strip()
    if not identifier:
        print("No input provided.\n")
        return
    cur.execute("CALL delete_user(%s)", (identifier,))
    conn.commit()
    print("Contact deleted (if existed).\n")

def main():
    try:
        conn = psycopg2.connect(**DSN)
    except Exception as e:
        print("Could not connect to database:", e)
        sys.exit(1)

    cur = conn.cursor()

    while True:
        print("""
======== PHONEBOOK CLI ========
1. Search contacts
2. Insert or update contact
3. Insert many from CSV
4. Paginated view
5. Delete contact
0. Exit
""")
        choice = input("Choose option: ").strip()
        if choice == "1":
            search_contacts(cur)
        elif choice == "2":
            upsert_contact(cur, conn)
        elif choice == "3":
            batch_insert_from_csv(cur, conn)
        elif choice == "4":
            paginate_contacts(cur)
        elif choice == "5":
            delete_contact(cur, conn)
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")

    cur.close()
    conn.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()
