from time import sleep
from random import randint #importo biblioteca
jogos = []
lista=[]

print('-=-' *30)
print('MEGA SENA')
print('-=-' *30)

jogador = int(input('Quantos jogos você deseja ?  '))

total = 1
while total <= jogador:
    cont= 0
    while True:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
            cont+=1
        if cont >=6:
            break
    jogos.sort
    lista.append(jogos[:])
    jogos.clear()
    print(f'Jogos:  {jogos}')



#jogador = (randint(0, 60)), (randint(0, 60)),(randint(0, 60)),(randint(0, 60)),(randint(0, 60)), (randint(0, 60)), #executo a biblioteca


