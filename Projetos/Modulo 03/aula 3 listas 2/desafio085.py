'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
totais = []
temp = []
impares = []
pares = []

for cont in range (1,8):
    temp.append(int(input(f'Digite o {cont}° valor: ')))
    totais.append(temp[:])
    temp.clear()

for p in totais:
    if p[0] % 2 == 0:
        pares.append(p)   
    else:
        impares.append(p)
            

pares.sort()
impares.sort()
print(f'Os numeros ao todo são {totais}')
print(f'Os pares: {pares}')
print(f'Os impares: {impares}')
