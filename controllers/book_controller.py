
from flask import Flask, render_template
from flask import Blueprint
from models.books import Book
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def book():
    books = book_repository.select_all()
    return render_template("/books/index.html", all_books = books)

@book_blueprint.route("/books/new", methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)