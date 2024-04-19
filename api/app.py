from flask import Flask, render_template

app = Flask(__name__)

books = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
    },
    {"title": "1984", "author": "George Orwell", "publication_year": 1949},
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
    },
    {"title": "Pride and Prejudice", "author": "Jane Austen", "publication_year": 1813},
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publication_year": 1951,
    },
]


@app.route("/books")
def home():
    return books
