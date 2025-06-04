'''Crie um programa que leia dois valores e mostre um menu na tela
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair
Seu programa devera realizar a operação solicitada em cada caso
'''

n1=float(input('Digite um valor: '))
n2= float(input('Digite outro valor: '))
opcao=0
while opcao != 5:
    opcao=int(input('\nDigite qual operação deseja: \n[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos numero\n[5] Sair\n'))
    if opcao == 1:
        soma= n1+n2
        print(f'O resultado da soma é: {soma}')
    elif opcao == 2:
        mult=n1*n2
        print(f'O resultado da multiplicação é: {mult}')
    elif opcao == 3:
        if n1>n2:
            print(f'O maior é: {n1}')
        if n2>n1:
            print(f'O maior é: {n2}')
        if n1==n2:
            print('Os numeros são iguais')
    elif opcao == 4:
        n1=float(input('Digite um valor: '))
        n2= float(input('Digite outro valor: '))
print('\nVocê encerrou o programa')