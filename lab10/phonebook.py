import psycopg2
import csv

conn = psycopg2.connect(
    host="localhost",
    database="testdb",
    user="postgres",
    password="12345",
    port="5432"
)

cur = conn.cursor()

def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()

def insert_manual():
    name = input("Name: ")
    phone = input("Phone: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()

def update_data():
    name = input("Enter name to update: ")
    new_phone = input("New phone: ")
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()

def query_data():
    filter_value = input("Name filter (e.g. A%): ")
    cur.execute("SELECT * FROM PhoneBook WHERE name LIKE %s", (filter_value,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data():
    value = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()

def menu():
    create_table()

    while True:
        print("\nPhoneBook Menu:")
        print("1 - Insert manually")
        print("2 - Upload from CSV")
        print("3 - Update data")
        print("4 - Query data")
        print("5 - Delete data")
        print("0 - Exit")

        choice = input("Choice: ")

        if choice == '1':
            insert_manual()
        elif choice == '2':
            insert_from_csv("C:\\Users\\Acer\\Desktop\\pp2_lab\\lab10\\contacts.csv")
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '0':
            break
        else:
            print("Invalid choice.")

menu()

cur.close()
conn.close()
