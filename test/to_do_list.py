import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()

def create_database():
    try:
        conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT")
            )
        print("✅Connection succesful")
        
        conn.autocommit = True
        cursor = conn.cursor()
        
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(os.getenv("DB_NAME"))))
        print(f"✅ Database '{os.getenv("DB_NAME")}' created successfully.")
        
        cursor.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error creating database: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")  

def get_connection():
    return psycopg2.connect(
        dbname = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        host = os.getenv("DB_HOST"),
        port = os.getenv("DB_PORT")

    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists tasks (
            id serial primary key,
            description text not null,
            completed boolean default false            
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Table is ready for use ")

def add_task(description):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (description) VALUES (%s)", (description,))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Task added succesfully")

def remove_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("delete from tasks where id = %s", (task_id, ))
    conn.commit()
    cur.close()
    conn.close()
    print("🗑️ Removed task from to do ")

def completed(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("update tasks set completed = True where id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("🎯 Task complete ")

def view_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("select id, description, completed from tasks order by id;")
    rows = cur.fetchall()
    if not rows:
        print("No tasks yet")
    else:
        print("Task available: ")
        for i in rows:
            status = "✅" if i[2] else "❌"
            print(f"{i[0]}. {i[1]} [{status}]")
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n === To do list ====")
        print("1. Add task")
        print("2. Remove task")
        print("3. Completed task")
        print("4. view task")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == "1" :
            description = input("Enter a description: ")
            add_task(description)
        elif choice == "2":
            task_id = input("Enter task_id to delete: ")
            remove_task(task_id)
        elif choice == "3":
            task_id = input("Enter task id for completed task: ")
            completed( task_id)
        elif choice == "4":
            view_tasks()
        elif choice == "5":
            print("👋 Goodbye")
            break
        else:
            print("Invalid entry, please try again")
if __name__ == "__main__":
    create_database()
    create_table()
    menu()
