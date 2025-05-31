#Crie um programa que leia uma frase e diga se ela é um palindromo 

frase = str(input('Digite uma frase: ')).strip().upper()#strip desconsidera espaços antes e depois

palavras = frase.split() #split separa palavra por palavra
junto=''.join(palavras)
inverso= junto[::-1]

if junto == inverso:
    print(f'Voce digitou {frase}.\nEla tudo junto fica{junto}. \nE ela ao contrario fica {inverso}. \nDevido a isso ela É palindromo')
else:
    print(f'Você digitou {frase}.\nEla tudo junto fica {junto}. \nE ela ao contrario fica {inverso}. \nDevido a isso ela NÃO é palindromo')