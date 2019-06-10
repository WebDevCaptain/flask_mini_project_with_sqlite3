from context_manager_db import DatabaseConnection
database_file = 'data.db'


def get_all_posts():
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM postsdb")
        posts = {row[0]: {'id': row[0], 'title': row[1], 'content': row[2]} for row in cursor.fetchall()}
    return posts


def _save_to_database(post):
    id = post['id']
    title = post['title']
    content = post['content']
    with DatabaseConnection(database_file) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO postsdb VALUES(?,?,?)", (id, title, content))




