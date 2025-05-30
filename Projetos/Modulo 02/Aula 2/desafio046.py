#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0 com uma pausa de 1 segundo
from time import sleep
print('CONTAGEM REGRESSIVA INICIANDO...')
for c in range (10, 0-1, -1):
    sleep(1)
    print(c)