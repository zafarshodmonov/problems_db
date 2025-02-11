import sqlite3

DB_NAME = "problems.db"

def get_connection():
    """ SQLite bazasiga ulanishni qaytaradi """
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_tables():
    """ Bazada kerakli jadvallarni yaratadi """
    conn = get_connection()
    cursor = conn.cursor()

    # Problems jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Problems (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        URL TEXT NOT NULL
    );
    """)

    # Topics jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Topics (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT UNIQUE NOT NULL
    );
    """)

    # ProblemTopics jadvali
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ProblemTopics (
        Problem_ID INTEGER,
        Topic_ID INTEGER,
        PRIMARY KEY (Problem_ID, Topic_ID),
        FOREIGN KEY (Problem_ID) REFERENCES Problems(ID),
        FOREIGN KEY (Topic_ID) REFERENCES Topics(ID)
    );
    """)

    conn.commit()
    conn.close()
    print("Jadvallar yaratildi.")
