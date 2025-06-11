#023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('digite um numero até 9999 aqui: '))

u= n//1 % 10
d= n//10 %10
c= n//100 %10
m= n//1000 %10

print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

#print(f'Unidade: {n[3]} \nDezena: {n [2]} \nCentena: {n [1]} \nMilhar: {n[0]}') esse só funciona se digitar os 4 numeros