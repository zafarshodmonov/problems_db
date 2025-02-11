from database.models import add_problem, link_problem_topic

def add_problem_with_topics(url, topics):
    """ Masala qo‘shib, bir nechta mavzuga bog‘lash """
    from services.topic_service import get_or_create_topic

    problem_id = add_problem(url)
    for topic in topics:
        topic_id = get_or_create_topic(topic)
        link_problem_topic(problem_id, topic_id)
    print(f"Masala qo'shildi: {url}, Mavzular: {topics}")

def get_problems_by_topics(topics):
    """ Berilgan mavzularga oid masalalar ro‘yxatini qaytaradi """
    from database.db_config import get_connection

    conn = get_connection()
    cursor = conn.cursor()
    query = """
    SELECT DISTINCT P.URL 
    FROM Problems P
    JOIN ProblemTopics PT ON P.ID = PT.Problem_ID
    JOIN Topics T ON PT.Topic_ID = T.ID
    WHERE T.NAME IN ({})
    """.format(",".join(["?"] * len(topics)))  # Dynamic parameterization

    cursor.execute(query, topics)
    result = [row[0] for row in cursor.fetchall()]
    conn.close()
    return result
