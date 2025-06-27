totais = [[],[]]
num=0

for c in range (1,8):
    num = int(input(f'Digite o {c}° valor: '))
    if num %2 ==0:
        totais[0].append(num)
    else:
        totais[1].append(num)

print('-=-'*20)
totais[0].sort()
totais[1].sort()
print(f'Totais: {totais}')
print(f'Pares: {totais[0]}')
print(f'Impares: {totais[1]}')