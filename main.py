import requests

api_url = "http://127.0.0.1:5000/books"
response = requests.get(api_url)

if response.status_code == 200:
    book_data = response.json()
    for book in book_data:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication Year: {book['publication_year']}")
        print()
else:
    print("Failed to fetch data from API")
