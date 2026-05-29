books = [
    {"id": 1, "title": "Python Basics"},
    {"id": 2, "title": "Data Science"},
    {"id": 3, "title": "Machine Learning"}
]

search = input("Enter book title to search: ").lower()

found = False

for book in books:
    if search in book["title"].lower():
        print("Book Found:")
        print(f"ID: {book['id']}")
        print(f"Title: {book['title']}")
        found = True

if not found:
    print("Book not found")



Enter book title to search:  amigo
Book not found



