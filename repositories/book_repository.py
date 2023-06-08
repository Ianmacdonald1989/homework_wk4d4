from db.run_sql import run_sql

from models.author import Author
from models.books import Book


def save(books):
    sql = "INSERT INTO users (title_first_name, title_last_name) VALUES (%s, %s) RETURNING *"
    values = [books.title_first_name, books.title_last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    books.id = id
    return books