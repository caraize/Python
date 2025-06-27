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
