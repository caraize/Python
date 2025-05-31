#Faça um programa que leia o peso de 5 pessoas, no final mostre qual foi o maior e o menor peso
maior=0
menor=0
for p in range (1,6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))

    if p == 1:
        maior=peso
        menor=peso
        
    elif peso > maior:
        maior=peso
    elif peso < menor:
        menor= peso
        
print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')