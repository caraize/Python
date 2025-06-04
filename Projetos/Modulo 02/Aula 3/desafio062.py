'''
Melhore o desafio 061 perguntando para o usuario se ele quer mostrar mais alguns termos, o programa encerra quando ele disser que quer mostrar 0 termos
'''
pt=int(input('Digite o primeiro termo da PA: '))
rz=int(input('Digite a razão da PA: '))
t=pt
cont=1
total= 0
mais = 10
while mais != 0:
    total= total+mais
    while cont<=total:
        print(f'{t} > ', end='')
        t=t+rz 
        cont=cont+1
    print('Pausa')
    mais = int(input('Quantos termos você quer a mais ? '))
print(f'FIM\nMostramos {total} termos ao total')

