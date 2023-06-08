import pdb
from models.author import Author
from models.books import books

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book1 = Book("George" "Orwell")
book_repository.save(book1)
book_repository.select_all()