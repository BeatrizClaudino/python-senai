lista = []
print("WELCOME MY PROGRAM\t")

while True:
    numero = int(input("Coloque seus números: "))
    lista.append(numero)
    resposta = int(input("Deseja continuar [1] SIM [2] NÃO"))
    if (resposta == 1):
        continue
    else:
        break
if 5 in lista:
    print("O valor 5 foi digitado")
else:
    print("O número 5 não foi digitado")
print(len(lista))
print(sorted(reverse=True))
