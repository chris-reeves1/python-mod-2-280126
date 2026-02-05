import sqlite3

def setup_database():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                password TEXT NOT NULL,
                rating TEXT NOT NULL                
            )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()