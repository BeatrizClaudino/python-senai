import random
from boneco import *

def add_novapalavra():
    new_word = input('Digite a nova palavra: ')
    arquivo = open("palavras.txt", "a")
    arquivo.write("\n" + new_word)
def add_dica():
    new_dica = input('Digite a dica: ')
    arquivo = open("dicas.txt", "a")
    arquivo.write("\n" + new_dica)

def quadrados(lista_index, palavra_escondida):
    for i in range(len(lista_index)):
        palavra_escondida.append('▬')
        print(palavra_escondida[i], "", end="")
    return palavra_escondida

def inicio():
    lista_palavras = []
    dicas = []

    arquivo = open("palavras.txt", "r")
    for i in arquivo:
        lista_palavras = [i.rstrip("\n") for i in arquivo]

    with open("dicas.txt", "r") as arquivo:
        for a in arquivo:
            dicas = [a.rstrip("\n") for a in arquivo]

    a = random.randint(0, len(lista_palavras)-1)
    lista_index = lista_palavras[a]
    dicas_index = dicas[a]
    print(dicas_index)
    tentativas = []
    palavra_escondida = []
    chances = 6
    palavra_escondida = quadrados(lista_index, palavra_escondida)

    while True:
        try:
            letra = input(" \nDigite uma letra: ").lower().strip()
            if letra.isnumeric():
                print("NÚMEROS NÃO SÃO ACEITOS AQUI! ")
                continue
            if len(letra)>1:
                print("DIGITE UMA LETRA POR VEZ!")
                continue
            if letra in tentativas :
                print("VOCÊ JÁ DIGITOU ESSA LETRA! DIGITE OUTRA: ")
                continue
            print(40*"-")
            if lista_index.__contains__(letra):
                for l, pos in enumerate(lista_index):
                    if lista_index[l] == letra:
                        palavra_escondida[l] = letra
                for i in range(len(lista_index)):
                    print(palavra_escondida[i], "", end="")
            else:
                tentativas.append(letra)
                print('Letras incorretas: ', *tentativas)

                chances = chances - 1
                if chances == 5:
                    boneco()
                    quadrados(lista_index, palavra_escondida)
                    print(f'você tem {chances} chances')
                if chances == 4:
                    boneco2()
                    quadrados(lista_index, palavra_escondida)
                    print(f'você tem {chances} chances')
                if chances == 3:
                    boneco3()
                    quadrados(lista_index, palavra_escondida)
                    print(f'você tem {chances} chances')
                if chances == 2:
                    boneco4()
                    quadrados(lista_index, palavra_escondida)
                    print(f'você tem {chances} chances')
                if chances == 1:
                    boneco5()
                    quadrados(lista_index, palavra_escondida)
                    print(f'você tem {chances} chances')
                if chances <= 0:
                    print("Você morreu de morte morrida! ")
                    break
        except:
            print("ERRO")

        ganhou = True #conceito flag
        for i in range(len(lista_index)):
            if lista_index[i] != palavra_escondida[i]:
                ganhou = False

        if ganhou:
            print('\nParabéns você ganhou')
            input_usuario = input("Quer continuar o game? [1]SIM [2]NÃO").lower()
            if input_usuario == "1":
                r = input("Quer criar a sua própria palavra e dica?: [1]SIM [2]NÃO")
                if r == '1':
                    add_novapalavra()
                    add_dica()
                    inicio()
                else:
                    inicio()
            else:
                break


if __name__ == '__main__':
    inicio()




