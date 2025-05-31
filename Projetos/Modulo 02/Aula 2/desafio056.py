'''faça um programa que leia o nome, idade e sexo de 4 pessoas, 
no final mostre a media de idade, 
o nome do homem mais velho 
e qunatas mulher tem menos de 20 anos'''

media=0
contador=0
somaidade=0
maioridade=0
nomemaisvelho=''

for c in range (1,5):
    print(f'-----{c}°-----')
    nome=str(input('Digite seu nome: ')).strip().title()
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Qual seu sexo ? [F/M] ')).strip().upper()

    somaidade= somaidade + idade
    media= somaidade / c

    if c ==1 and sexo =='M':
       maioridade = idade
       nomemaisvelho=nome
    if sexo =='M' and idade>maioridade:
       maioridade=idade
       nomemaisvelho=nome
          


    if sexo =='F' and idade <= 20:
      contador = contador + 1

print(f'\n\nA media de idade é: {media} anos. \nTemos {contador} menores de idade feminina. \nO homem mais velho tem: {maioridade} anos e se chama: {nomemaisvelho}')