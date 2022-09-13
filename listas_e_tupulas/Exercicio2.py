lista = []

while True:
    numero = int(input("Digite um número: "))
    resposta = int(input("Deseja continuar? [1]SIM [2]NÃO "))
    if numero not in lista:
        lista.append(numero)
    else:
        pass
    if resposta ==1:
        continue
    else:
        break
lista.sort()
print(lista)
