from book import Book


class Book_exclusive(Book):
    val_descount = 0

    def __init__(self, price, isbn, title, author):
        super().__init__(price, isbn, title, author)



