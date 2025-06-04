'''crie um programa que leia varios numeros inteiros pelo teclado, o programa so vai parar quando o usuario digitar o valor 999 que é a condição de parada, no final mostre quantos numeros foram digitados e qual a soma deles
'''
cont=0
user=0
user1=user
while user != 999:
    user=int(input('Digite um valor:(999 para parar)\n'))
    cont=cont+1
    user1=user1+user
print(f'O programa leu {cont-1} numeros e a soma deles é: {user1-999}')
