import sqlite3
from article import Article

DATABASE_DUMP_FILENAME = "db_dump.sql"


def execute_sql_script_from_file(connection: sqlite3.Connection, filename: str):
    # Read SQL script from file
    with open(filename, 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute SQL script
    cursor = connection.cursor()
    cursor.executescript(sql_script)
    cursor.close()


def get_uncomment_articles(connection: sqlite3.Connection) -> list[Article]:
    # Query for get uncomment articles only
    query = """
    SELECT article.id, article.title, article.text 
    FROM article 
    LEFT JOIN comment ON article.id = comment.article_id
    WHERE comment.id is NULL;
    """

    # Execute the query
    cursor = connection.cursor()
    cursor.execute(query)
    article_tuples: list[tuple[int, str, str]] = cursor.fetchall()
    cursor.close()

    # Build list of dataclasses from list of tuples
    result = [Article(*article_tuple) for article_tuple in article_tuples]
    return result


def main():
    with sqlite3.connect(':memory:') as sqlite_connection:
        execute_sql_script_from_file(sqlite_connection, DATABASE_DUMP_FILENAME)
        articles = get_uncomment_articles(sqlite_connection)
    print(*articles, sep="\n")


if __name__ == "__main__":
    main()
