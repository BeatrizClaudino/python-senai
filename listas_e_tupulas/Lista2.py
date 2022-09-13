lista = [1,4,5,10,3,99,11]

#DEFINIR A ORDEM DECRESCENTE É O REVERSE
lista.sort(reverse=True)
print(lista)

#ESSE CÓDIGO PEGA O PRIMEIRO E O ÚLTIMO NÚMERO E O RESTO DESCONSIDERA
primeiro, *resto, ultimo = lista
#print(primeiro)
#print(resto)
#print(ultimo)


lista1 = [2, 4, 9]
lista2 = lista1[:] #ESSA CHAVE COM DOIS PONTOS SEPARA AS LISTAS E A LISTA 2 SE TORNA INDEPENDENTE
lista2[1] = 5
print(lista2)
print(lista1)
