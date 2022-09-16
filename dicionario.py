frase = "Esse é um teste para medir meus conhecimentos em python"
dicio = dict()

frase = frase.replace(' ', '')
for i in frase:    #PERCORRENDO A FRASE
    if dicio.__contains__(i):  #SE NO DICIONÁRIO JÁ CONTÉM A LETRA NA POSIÇÃO i
        dicio[i] = dicio[i]+1  #O DICIONÁRIO ADICIONA MAIS 1 NA QUANTIDADE DE LETRAS
    else:
        dicio[i] = 1          #SE A LETRA NÃO EXISTIR NO DICIONARIO, ELE VAI ADICIONAR A LETRA E COLOCAR O VALOR 1

for j in sorted(dicio, key=dicio.get, reverse=True):
    print(f'{j} - {dicio[j]}')


#for i in enumerate(formulario)