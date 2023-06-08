from db.run_sql import run_sql

from models.books import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(author):
    sql = "INSERT INTO author (description, book_id, completed) VALUES (%s, %s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)
    return authors