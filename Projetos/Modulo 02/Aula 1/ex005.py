n1= float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2) /2

if media < 5:
    print(f'REPROVADO \nMedia {media} ??? \nBurro')
elif media >=5 and media <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')