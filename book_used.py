from book import Book


class Book_used(Book):
    val_descount = 25

    def __init__(self, price, isbn, title, author):
        super().__init__(price, isbn, title, author)

