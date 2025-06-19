valores=[]
maior=0
menor=0

for cont in range(0,5): #range de 1-5
    valores.append(int(input(f'Digite um valor para posição {cont}:'))) #adicionando valores que o user digitou a lista

    if cont==0:
        maior = valores[cont]
        menor = valores[cont]

    elif valores[cont] > maior:
        maior = valores[cont]

    elif valores[cont] < menor:
        menor = valores[cont]

print(valores)


print(f'\nO maior valor digitado foi: {maior} || Na posição' , end='')
for i, v in enumerate(valores): #i pega o enumerate e v pega o valores
    if v == maior: #se valores for igual o maior, vai printar o enumerate
        print(f' {i}... ', end='')


print(f'\nO menor valor digitado foi: {menor} || Na posição' , end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}... ', end='')


