lista = [28, 34, 55, 41, 9, 71]
lista2 = [9, 31, 44, 74, 28, 56]


lista_1 = set(lista)
lista_2 = set(lista2)

print(lista_1-lista_2)
print(lista_2 - lista_1)
print(lista_1 & lista_2)
print(lista_1^lista_2)