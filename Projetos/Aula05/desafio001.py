 #Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome:')).strip() #strip para remover os espaços

print(f'Seu nome em letras maiusculas fica: {nome.upper()}') #deixar tudo em maiusculo
print(f'Seu nome em letras minusculas fica: {nome.lower()}') #deixar tudo em minusculo
print(f"Seu nome tem: {len(nome)-nome.count(' ')} letras") #ele vai contar quantos caracteres tem o nome todo com espaços e depois contar quantos espaços tem e remove-los
#print(f"Seu primeiro nome tem: {nome.find(' ')} letras") #ele vai pesquisar onde tem o primeiro espaço do nome, consequentemente sendo a quantidade de caracteres do primeiro nome
separa = nome.split()
print(f'seu primeiro nome é: {separa[0]} e tem: {len(separa[0])} letras')