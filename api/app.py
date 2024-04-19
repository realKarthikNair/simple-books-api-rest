from flask import Flask, jsonify

app = Flask(__name__)
books = [
    {"title": "Book 1", "author": "Author 1", "publication_year": 2020},
    {"title": "Book 2", "author": "Author 2", "publication_year": 2021},
    {"title": "Book 3", "author": "Author 3", "publication_year": 2022},
]


@app.route("/books", methods=["GET"])
def home():
    return render_template(("books.html"), books=books)