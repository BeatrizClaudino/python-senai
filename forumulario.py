dicionario = dict()
lista = []

def formulario():
    while True:
        pergunta = input('Digite o nome do campo desejado: ')
        if pergunta == '':
            break
        dicionario[pergunta] = ''
    print('Adicionando dados...')

    lista.append(dicionario.copy())

    for i, valor in enumerate(dicionario):
        dicionario[valor] = input(f'Por favor digite o {valor}: ')

    resposta = input('Digite enter para continuar ou qualquer letra pra sair: ')

    if resposta == '':
        formulario()
    else:
        print(f'O resultado é: {dicionario}')






    #para mostrar todas as chaves do dicionário
if __name__ == '__main__':
    formulario()