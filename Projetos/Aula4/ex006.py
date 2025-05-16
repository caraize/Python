import random
a1=input('Digite o nome do primeiro aluno: ')
a2=input('Segundo aluno: ')
a3=input('Terceiro aluno: ')
a4=input('Quarto aluno: ')

lista=[a1,a2,a3,a4]
aluno=random.choice(lista)
print(f'O aluno escolhido foi o: {aluno}')