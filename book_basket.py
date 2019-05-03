from book import Book


class Book_basket(Book):

    def __init__(self, price, isbn, title, author, type):
        super().__init__(price, isbn, title, author)
        self.type = type


def cal_descount(price, val_desc):
    result = float(price) - (float(price) * float(val_desc))/100
    return result
