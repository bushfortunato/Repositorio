# Project description


A bookstore sells 3 types of books. Used books, new books and exclusive books.
Exclusive books are not discounted. New books are 10% off and 25% used.

### Implementations!
-------------------
  - (I) A program that accepts as the parameter the name of a csv file with the cart.
  - (II) Accept an additional parameter (-displayauthors) that instead of adding to the cart print only the price / price with the discount applied.
 - (V) Print a basket with aggregate products and quantity.
 - (IV) Make a Webservice REST in an MVC framework of your choice, with the endpoints (there is no need to persist data for a database):
                  - Add book to cart
                  - Get Cart


### Prerequisites:
---------------
 - Language: Python
 - Version: Python 3.6.7
 - IDE: PyCharm CE
 - Web FrameWork: Flask
 - OS: Linux Mint 19

### Install PyCharm CE
------------------
- The PyCharm CE is available in the Linux mint / Ubuntu application stores. Search by name and
install.


### Install Flask
--------------------
- Windows Pycharm, you can go to File-> Settings-> Project interpreter, click the green + button (Install),
type in flask, select Flask from the list then click Install Package

### Webservices Rest:
-----------------
##### Endpoints:
- @ app.route ('/ basket_webservice', methods = ['GET'])
- @ app.route ('/ book_store / <int: id>', methods = ['POST'])
- @ app.route ('/ basket_webservice', methods = ['GET'])
   

###### NOTE: To access Webservice, run the file "bonus_III_IV.py"
#
##### Webservice Examples:

| Endpoint | Description |
| ------ | ------ |
|  http://127.0.0.1:5000/store_webservice | View all books |
|  http://127.0.0.1:5000/3 | Add index book 3 to cart |
|  http://127.0.0.1:5000/basket_webservice | View cart |
