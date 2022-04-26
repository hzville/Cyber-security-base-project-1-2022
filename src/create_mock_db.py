import sqlite3

db_name = 'mock-db.db'
con = sqlite3.connect(db_name)
cur = con.cursor()
table = 'users'

def create_db():
    try:
        cur.execute(f'DROP TABLE {table}')
    except:
        print(f'error removing table {table}')

    try:
        cur.execute(f'CREATE TABLE {table} ( id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, balance INTEGER, admin BOOL)')
        cur.execute(f'INSERT INTO {table} (username, password, balance, admin) VALUES ("bob", "bobspassword", 0, True)')
        cur.execute(f'INSERT INTO {table} (username, password, balance, admin) VALUES ("alice", "alicespassword", 0, False)')
        con.commit()
    except:
        print('error creating new database')

    cur.close()
    con.close()

if __name__ == '__main__':
    create_db()
    print('db created')