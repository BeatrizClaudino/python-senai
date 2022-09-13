#isso é um dicionário
#cadastro = {'nome': 'joão', 'idade': (21, 39)}

#CRIANDO UM DICIONÁRIO
cadastro = dict(nome = 'João', idade=21)
cadastro = dict(nome = 'João', idade=21)

#Altera o nome dentro do dicionário
cadastro['nome'] = 'Maria'

#Printando
print(cadastro)
print(cadastro['idade'])
print(cadastro['nome'])

                                                    #TESTE DE N° 2

teste = []

#CRIANDO UM WHILE PARA ADICIONAR NOME E IDADE NO DICIONÁRIO
while True:
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    signo = input('Digite o signo: ')

    cadastro = dict (nome=nome, idade=idade, signo=signo)

    teste.append(cadastro)
    print(teste)

                                                    #TESTEDE N° 3
for i in range(2):
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade: '))
    cadastro = dict(nome=nome, idade=idade, signo=signo)
    for chave, valor in cadastro.items():
        print(f'{valor} - {chave}')

                                                    #TESTE N° 4

dicionario = dict(palavra = 'abacaxi', definicao='Fruta cítrica típica do Brasil')
dicionario2 = {'palavra': 'abacaxi', 'definicao': 'Fruta cítrica típica do Brasil'}

listaFrutas = []
listaFrutas.append(dicionario)
listaFrutas.append(dicionario2)
print(listaFrutas)

for x, y in enumerate(listaFrutas):  #ENUMERATE: PERCORRE DOIS VALORES. O X É O INDEX E O Y É O VALOR
    print(x)
    print(y['palavra'])
    if y['palavra'] == 'abacaxi':
        print(y['definicao'])