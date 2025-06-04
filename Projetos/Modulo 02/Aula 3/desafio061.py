'''Refaça o desafio 051 lendo o primeiro termo e a razao de uma PA mostrando os 10 primeiros termos da progressao usando while
'''
pt=int(input('Digite o primeiro termo da PA: '))
rz=int(input('Digite a razão da PA: '))
t=pt
cont=1
while cont<=10:
    print(f'{t} > ', end='')
    t=t+rz #aqui sempre colocar a nova variavel criada pois ela sempre vai se atualizando, o pt nao se atualiza, pois ja é um numero determinado
    cont=cont+1
print(t)

