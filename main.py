import requests, sqlite3, json

api_url = "https://simple-books-api-rest-realkarthiknairs-projects.vercel.app/books"
response = requests.get(api_url)

if response.status_code == 200:
    book_data = response.json()
else:
    print("Failed to fetch data from API")

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        publication_year INTEGER
    )
    """
)

for book in book_data:
    cursor.execute(
        """
        INSERT INTO books (title, author, publication_year) VALUES (?, ?, ?)
        """,
        (book["title"], book["author"], book["publication_year"]),
    )

conn.commit()

cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

print(json.dumps(books, indent=2))
