'''Faça um programa que mostre a tabuada de varios numeros, um de cada vez para cada valor digitado pelo usuario. O programa sera interrompido se o valor digitado for negativo
'''
from time import sleep


while True:
    n=int(input('Qual numero deseja ver a tabuada ?'))
    if n< 0:
        break
    for cont in range(0,10):
        cont=cont+1
        resu= n*cont
        print(f'{n} x {cont} = {resu}')
print('Impossivel para negativos')
sleep(1)
print('Encerrando...')