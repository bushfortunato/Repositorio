from csv_file import config_basket, get_clean_basket

#(V) Imprimir um basket com produtos agregados e quantidade.

bookList = list(config_basket(get_clean_basket('csvfile.csv')))
cont = 0

while cont < len(bookList):
    total = 0
    val = 1
    num = cont + 1
    total = bookList[cont].price
    while num < len(bookList):
        if bookList[cont].isbn == bookList[num].isbn:
            val += 1
            total += bookList[num].price
            bookList.__delitem__(num)
        num += 1
    print('€', total, '(', val, ')', bookList[cont].isbn, ':', bookList[cont].title)
    cont += 1

