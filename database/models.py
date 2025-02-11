from database.db_config import get_connection

def add_problem(url):
    """ Yangi masala qo‘shadi """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Problems (URL) VALUES (?)", (url,))
    conn.commit()
    problem_id = cursor.lastrowid
    conn.close()
    return problem_id

def add_topic(name):
    """ Yangi mavzu qo‘shadi """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO Topics (NAME) VALUES (?)", (name,))
    conn.commit()
    cursor.execute("SELECT ID FROM Topics WHERE NAME = ?", (name,))
    topic_id = cursor.fetchone()[0]
    conn.close()
    return topic_id

def link_problem_topic(problem_id, topic_id):
    """ Masalani mavzuga bog‘laydi """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO ProblemTopics (Problem_ID, Topic_ID) VALUES (?, ?)", (problem_id, topic_id))
    conn.commit()
    conn.close()
