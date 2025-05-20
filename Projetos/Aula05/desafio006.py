#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Qual seu nome completo? ')).strip()
dividido = nome.split()
print(f'Muito prazer te conhecer!! \nSeu primeiro nome é: {dividido[0]} \nE seu ultimo nome é: {dividido[-1]}')
