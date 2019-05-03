from csv_file import *
from flask import Flask, flash, url_for, session, logging, redirect, render_template, jsonify, json
from book import Book

#(IV) Fazer um Webservice REST numa framework MVC à escolha, com os endpoints (não é necessário persistir dados para um base de dados):
                 #Adicionar livro ao carrinho
                 #Obter o carrinho

app = Flask(__name__)
bookList = config_basket(get_clean_basket('csvfile.csv'))
shoppingCart = []


#Rota padrao
@app.route('/', methods=['GET'])
def books():
    return render_template('book_store.html', books=bookList)

#Rota para visualizar o carrinho
@app.route('/shopping_cart', methods=['GET'])
def shopping_cart():
    return render_template('/shopping_cart.html', cart=shoppingCart)

#Rota para adicionar item no carrinho
@app.route('/book_store/<int:id>', methods=['POST'])
def book(id):
    indice = int(id)
    liv = Book(bookList[indice].price, bookList[indice].isbn, bookList[indice].title, bookList[indice].author)
    shoppingCart.append(liv)
    return redirect('/')

#Rota para visualizar loja (Json)
@app.route('/store_webservice', methods=['GET'])
def shopping_cart_json():
    l = convert_json(bookList)
    value = json.dumps(l, ensure_ascii=False, indent=len(l))
    return value

#Rota para visualizar carrinho (Json)
@app.route('/basket_webservice', methods=['GET'])
def book_store_json():
    l = convert_json(shoppingCart)
    value = json.dumps(l, ensure_ascii=False, indent=len(l))
    return value


if __name__ == "__main__":\
    app.run(debug=True, use_reloader=True)