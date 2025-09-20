books = [
    {
    "title": "pere",
    "author": "gabi nitzan",
    "already_read": True,
    },
    {
    "title": "lord of the ring",
    "author": "IDK",
    "already_read": False,
    }
]

def is_book_read (books, book_number):
    if book_number >= len(books):
        print (f"there is no book number {book_number}")
    else:
        book  = books[book_number]
        if book["already_read"]:
            print (f"the book {book["title"]} is read")
        else: print (f"the book {book["title"]} is not yet read")

is_book_read(books, 2)