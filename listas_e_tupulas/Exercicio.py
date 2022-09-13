lista = []
n = 0
n1 = 0

for i in range(0, 5):
    lista.append(int(input("Digite um número: ")))
print(f'O maior valor é: {max(lista)} na posição: {lista.index(max(lista))} e o menor valor é: '
      f'{min(lista)} na posição {lista.index(min(lista))}')




