lista = []
listaImpar = []
listaPar = []

while True:
    num = int(input("Digite valores numéricos: "))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(lista)
    elif num % 2 == 1:
        listaImpar.append(lista)

    resposta = input("Digite C para continuar e S para sair").upper().strip()
    if resposta == 'S':
       break

print(listaImpar)
print(listaPar)