''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from time import sleep
from random import randint #importo biblioteca
jogos = []
lista=[]

print('-=-' *30)
print('MEGA SENA')
print('-=-' *30)

quant = int(input('Quantos jogos você deseja ?  '))
total = 1

while total <= quant:
    cont= 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >=6:
            break
    lista.sort
    jogos.append(lista[:])
    lista.clear()
    total+= 1
print(f'sorteando {quant} jogos')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('Boa sorte!!!!')


#jogador = (randint(0, 60)), (randint(0, 60)),(randint(0, 60)),(randint(0, 60)),(randint(0, 60)), (randint(0, 60)), #executo a biblioteca


