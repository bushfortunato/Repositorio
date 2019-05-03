import csv
import json
from builtins import print, filter
from sqlite3 import adapt
from pip._vendor.pyparsing import empty
from book import Book
from book_new import Book_new
from book_used import Book_used
from book_exclusive import Book_exclusive
from book_basket import Book_basket, cal_descount


bookTypes = ['UsedBook', 'NewBook', 'ExclusiveBook']

# Lista processada sem os descontos
def get_clean_basket(filePath):
    basket_list = []

    with open(filePath, mode='r') as csv_file:
        list_tmp = csv.reader(csv_file, delimiter=',')

        row = 0
        for itemBook in list_tmp:
            if row != 0:
                book = Book(itemBook[0], itemBook[2], itemBook[3], itemBook[4])
                basket = Book_basket(book.price, book.isbn, book.title, book.author, itemBook[1])
                basket_list.append(basket)
            row += 1
    return basket_list  # devolve a lista sem alteracoes nos prices

# Lista processada com os descontos
def config_basket(parm):
    list_tmp = parm
    basket_list = []

    for itemBook in list_tmp: # used books
        if itemBook.type == bookTypes[0]:
            used_book = Book_used(itemBook.price, itemBook.isbn, itemBook.title, itemBook.author)
            basket = Book_basket(cal_descount(used_book.price, used_book.val_descount), itemBook.isbn, used_book.title, used_book.author, itemBook.type)
            basket_list.append(basket)

        if itemBook.type == bookTypes[1]: # new book
            new_book = Book_new(itemBook.price, itemBook.isbn, itemBook.title, itemBook.author)
            basket = Book_basket(cal_descount(new_book.price, new_book.val_descount), new_book.isbn, new_book.title, new_book.author, itemBook.type)
            basket_list.append(basket)

        if itemBook.type == bookTypes[2]: # exclusive book
            exclusive_book = Book_exclusive(itemBook.price, itemBook.isbn, itemBook.title, itemBook.author)
            basket = Book_basket(cal_descount(exclusive_book.price, exclusive_book.val_descount), exclusive_book.isbn, exclusive_book.title, exclusive_book.author, itemBook.type)
            basket_list.append(basket)
    return basket_list


def convert_json(arg):
    lista = []

    for item in arg:
        d = {}
        d["Price"] = item.price
        d["ISBN"] = item.isbn
        d["Title"] = item.title
        d["Author"] = item.author
        lista.append(d)
    return lista
