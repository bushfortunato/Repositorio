from csv_file import config_basket, get_clean_basket
#Faz um programa que leia esse csv e devolva o
#preço final junto com a lista de livros no formato abaixo (atenção ao alinhamento à esquerda):

l = config_basket(get_clean_basket('csvfile.csv'))
val = 0

print(' ')
for item in l:
    print(f'€ {float(item.price)}    \t{item.isbn}:   \t{item.title}  | \t{item.author}')
    val += item.price
print('€ {:.2f}'.format(val) + ' - Total')
