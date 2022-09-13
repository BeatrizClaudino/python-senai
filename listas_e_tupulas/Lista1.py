lista = []

#CRIANDO UMA LISTA E PRINTANDO ELA
letras = ['a', 'b', 'c', 'b']
print(letras)

#ADICIONANDO O "D" NO FINAL DA LISTA
letras.append('d')
print(letras)

#ADICIONA O ITEM DESEJADO NA FRENTE DA LISTA
letras.insert(0, '-')
print(letras)

#A FUNÇÃO POP TIRA O ÚLTIMO ELEMENTO DA LISTA
letras.pop()
print(letras)

#REMOVENDO A PRIMEIRA LETRA B QUE ELE ENCONTRAR
letras.remove('b')
print(letras)

#FUNÇÃO DEL É PARA PASSAR UM VALOR E ELE VAI APAGAR
del letras[0]
print(letras)