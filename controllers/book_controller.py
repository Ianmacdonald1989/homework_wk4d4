
from flask import Flask, render_template
from flask import Blueprint
from repositories import author_repository, book_repository
from models.author import Author

author_blueprint = ("author", __name__)

@author_blueprint.route("/authors")
def author():
    tasks = author_repository.select_all()
    return render_template("/authors/index.html", all_authors = author)