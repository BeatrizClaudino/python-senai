lista_usuarios = []
usuario = dict()

def menu():
    while True:
        opcao = int(input('''Escolha a opção desejada:
        [1]Adicionar Usuário
        [2] Listar usuários
        [3] Pesquisar usuário
        [4] Atualizar usuário
        [5] Para sair\n'''))

        if (opcao == 1):
            cadastro()
        elif(opcao == 2):
            listar_cadastro()
        elif(opcao == 3):
            pesquisar_usuario(0)
        elif(opcao == 4):
            atualizar()
        elif(opcao == 5):
            break

def cadastro():
    while True:
        print("Digite apenas informações verdadeiras durante o cadastro!")
        nome = input("Qual é o seu nome? ")
        i = int(input("Qual é a sua idade? "))
        print("_" * 50)
        idade = str(i)
        usuario["nome"] = nome
        usuario["idade"]= idade

        lista_usuarios.append(usuario.copy())

        resposta = int(input("Deseja continuar? [0]Não [1]Sim"))
        print("_" * 50)

        if resposta == 1:
            continue
        else:
            print("*"*30)
            break

def listar_cadastro():
    print(lista_usuarios)

def pesquisar_usuario(y):
    b = input("Digite o nome do usuário que deseja pesquisar: ")
    for i, n in enumerate(lista_usuarios):
        for x in n:
            if n[x].__contains__(b):
                formatado = str(n)  #transformando a lista em string
                formatado = formatado.replace("{","") #formatação para tirar os espaços, virgulas e chaves da lista
                formatado = formatado.replace("}","")
                formatado = formatado.replace("', ","\n")
                formatado = formatado.replace("'","")
                print(formatado)
                if y == 1:        #se y for igual à 1 ele para no primeiro cadastro que bater, depende do nome que o usuário digita para alterar
                    return n[x]
def atualizar():
    alterar = pesquisar_usuario(1)
    atualizacao_usuario = int(input('''Opções para atualização:
    [1] Nome
    [2] Idade'''))

    for i, p in enumerate(lista_usuarios):
        for x in p:
            if p[x].__contains__(alterar):
                if atualizacao_usuario == 1:
                    p["nome"] = input("DIGITE O NOVO NOME:")
                else:
                    p["idade"] = input("DIGITE A NOVA IDADE: ")
    print(lista_usuarios)

if __name__ == '__main__':
    menu()

