lista = []


tupla = (1, 2, 3) #É UMA TUPLA E POR ISSO NÃO PODE SER ALTERADA
print(tupla)

numeros = [22, 51, 44, 15] #LISTA
primeiro = set(numeros)
segundo = {15,44} #SET

print(primeiro | segundo) #OBTER TODOS OS NÚMEROS SEM REPETIÇÃO, IGNORA OS REPETIDO
print(primeiro & segundo)#TRAZER OS NÚMEROS QUE ESTÃO PRESENTES NAS DUAS LISTAS
print(primeiro - segundo)
print(segundo - primeiro)
print(primeiro^segundo)#TRAZER OS ELEMENTOS QUE NÃO SE REPETEM