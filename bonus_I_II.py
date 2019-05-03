from csv_file import get_clean_basket, config_basket

#(I) Um programa que aceite como parametro o nome de um ficheiro csv com o carrinho.
#(II) Aceitar um parametro adicional (-displayauthors) que em vez de adicionar ao carrinho imprima apenas o
#preço/preço com o desconto aplicado.


inputFilePath = input('Insira o caminho csv file: ')
inputCommand = input('Insira o parametro de consulta: ')

print('')

if inputCommand == '-displayauthors':
    list_not_processed = list(get_clean_basket(inputFilePath))
    list_processed = list(config_basket(get_clean_basket(inputFilePath)))

    for a, b in zip(list_not_processed, list_processed):
        print(f'€ {a.price}/{b.price}:   \t{a.title} - \t{a.author} ')
else:
    print('Entrada invalida')

#Parametros:
# ../dataFile/csvfile.csv
# -displayauthors
