num = [5, 6, 8, 9, 2]
num2 = [1, 2, 7, 9, 5]

for i in range(len(num)):
    variavel = num[i]
    for j in range(len(num2)):
        variavel2 = num2[j]
        if(variavel == variavel2):
            print(f'O número presente nas duas listas é: {variavel}')