import random
a1=input('Digite o nome do primeiro aluno: ')
a2=input('Segundo aluno: ')
a3=input('Terceiro aluno: ')
a4=input('Quarto aluno: ')
lista=[a1,a2,a3,a4]

ordem=random.shuffle(lista)
print(lista)