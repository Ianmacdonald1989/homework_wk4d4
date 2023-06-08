from db.run_sql import run_sql

from models.books import Books
from models.author import Author
import repositories.user_repository as user_repository


def save(author):
    sql = "INSERT INTO author (description, book_id, completed) VALUES (%s, %s, %s) RETURNING *"
    values = [author.genre, author.book.id, author.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author