import sqlite3
import create_mock_db

db_name = create_mock_db.db_name
table = create_mock_db.table
conn = sqlite3.connect(db_name, check_same_thread=False)
cur = conn.cursor()

def select_all_users():
    cur.execute(f'SELECT * FROM {table}')

def select_username(username):
    cur.execute(f'SELECT * FROM {table} WHERE username="{username}"')
    return cur.fetchall()

def create_new_account(username, password):
    cur.execute(f"INSERT INTO {table} (username, password, balance, admin) VALUES ('" + {username} + "', '" + {password} + "', 0, False)")
    conn.commit()

def change_password(username, password):
    cur.execute(f'UPDATE {table} SET password="{password}" WHERE username="{username}"')
    conn.commit()