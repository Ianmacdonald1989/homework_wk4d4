import pdb
from models.books import Book
from models.author import Author


import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author = Author("George" "Orwell")
author_repository.save(author)
author_repository.select_all()

book_1 = Book("1984", "Fiction", author)
book_repository.save(book_1)

