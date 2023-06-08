from db.run_sql import run_sql

from models.books import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(books):
    sql = "INSERT INTO books (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [books.title, books.genre, books.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    books.id = id
    return books

def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], author, row['id'])
        books.append(book)
    return books