print('-=-'*20) #só ajeitando

ano = int(input('Digite um ano que deseja sabe se ele é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #ano bissexto ocorre de 4 em 4 anos -> exceto anos multiplos de 100 que nao sao multiplos de 400
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')