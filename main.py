from database.db_config import create_tables
from services.problem_service import add_problem_with_topics, get_problems_by_topics

# Jadvallarni yaratish
create_tables()

# Masalalarni qo‘shish
add_problem_with_topics("https://example.com/problem1", ["SELECT", "FROM"])
add_problem_with_topics("https://example.com/problem2", ["WHERE", "JOIN"])
add_problem_with_topics("https://example.com/problem3", ["SELECT", "GROUP BY"])

# Faqat 'SELECT' va 'FROM' mavzulariga oid masalalarni olish
problems = get_problems_by_topics(["SELECT", "FROM"])

print("\n🔹 Tanlangan mavzularga oid masalalar:")
for url in problems:
    print(url)
