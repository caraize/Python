valores=[]
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
print(valores)


for c,v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v} ')

print('Final')