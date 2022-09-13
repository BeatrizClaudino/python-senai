def extrair(frutas):
    nomes_frutas = ''
    for i in frutas:
        nomes_frutas += i + '\n'
    return nomes_frutas

frutas = {'abacaxi': 'Abacaxi é uma fruta da terra',
              'abacate': 'Abacate tem uma barriguinha',
              'limão': 'Limão é azedo'}

while True:
    usuario = input(f'FRUTAS DISPONÍVEIS:\n{extrair(frutas)}'
                    f'Escolha a sua: ').lower().strip()
    if usuario not in frutas:
        print('Hmm, não tenho essa fruta em meu sistema!')

        resposta = input('DESEJA CADASTRAR? [a]SIM e [j]NÃO')

        if resposta == 'a':
             novaDescricao = input('Qual descrição deseja colocar? ')
             frutas[usuario] = novaDescricao
        else:
            print('ENTÃO DIGITE UMA VÁLIDA')
    else:
        print(frutas[usuario])
    print(frutas)