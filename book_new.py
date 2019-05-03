from book import Book


class Book_new(Book):
    val_descount = 10
    def __init__(self, price, isbn, title, author):
        super().__init__(price, isbn, title, author)


