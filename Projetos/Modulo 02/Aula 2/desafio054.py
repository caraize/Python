#Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quais são maiores de idade
from datetime import date
ano_atual = date.today().year
maiores= 0
menores= 0

for c in range(0,8):
    data_nasc=int(input('Digite o seu ano de nascimento: '))
    idade = ano_atual - data_nasc

    if idade >= 18:
        maiores= maiores + 1
        
    else:
        menores= menores + 1
        
print(f'Os maiores de idade são: {maiores}')
print(f'Os menores são: {menores}')