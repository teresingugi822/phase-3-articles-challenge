import sqlite3

CONN = sqlite3.connect('lib/database.db')
CURSOR = CONN.cursor()

def create_tables():
    with open('db/schema.sql') as f:
        CURSOR.executescript(f.read())
    CONN.commit()

if __name__ == '__main__':
    create_tables()
    print("Tables created.")
