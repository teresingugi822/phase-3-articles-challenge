from db.create_tables import CONN, CURSOR

def seed_data():
    CURSOR.execute("INSERT OR IGNORE INTO authors (name) VALUES ('Jane Doe'), ('Mark Twain')")
    CURSOR.execute("INSERT OR IGNORE INTO magazines (name, category) VALUES ('Tech Weekly', 'Technology'), ('Writers Digest', 'Literature')")
    CURSOR.execute("""
        INSERT OR IGNORE INTO articles (title, content, author_id, magazine_id)
        VALUES 
            ('Tech Tips', 'Content for tech tips', 1, 1),
            ('Storytelling', 'Content for storytelling', 2, 2)
    """)
    CONN.commit()
    print("Database seeded.")

if __name__ == '__main__':
    seed_data()
