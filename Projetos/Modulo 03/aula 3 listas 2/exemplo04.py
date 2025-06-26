galera= []
dado = []
totalmaior = totalmenor = 0
for cont in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #aqui ele adiciona os dados da lista dado na galera, ou seja, nome e idade separado, pois lemos os dois
    dado.clear() # e aqui ele limpa a coluna dado, ou seja a cada loop ele limpa ela e a cada loop ele adiciona separado nome e idade no comando anterior
    
for p in galera: #para cada p em galera
    if p[1] >=18: #se (p[1] = idade) for maior que 18, ou seja, os dados do galera vira o p do laço
        print(f'{p[0]} é maior de idade')
        totalmaior+=1
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor +=1

print(f'Existem {totalmaior} pessoas maiores de idade')
print(f'Existem {totalmenor} pessoas menores de idade')