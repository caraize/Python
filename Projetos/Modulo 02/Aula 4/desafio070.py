total_gasto=0
mais_de_mil=0
cont=0
menor=0
barato=''
while True:
    nome = str(input('Nome do produto: '))
    preço= float(input('Preço: R$'))
    cont=cont+1
    
    total_gasto=total_gasto+preço

    if cont==1 or preço < menor:
        menor=preço
        barato=nome

    '''elif preço < menor:
        menor=preço
        barato=nome'''

    if preço >=1000:
        mais_de_mil=mais_de_mil+1


    continuar=' '
    while continuar not in 'SN':
        continuar= str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if continuar =='N':
        break
print(f'{"FIM DO PROGRAMA":-^40}')
print(f'O total gasto foi: R${total_gasto:.2f}')
print(f'{mais_de_mil} custa(m) mais de R$:1000,00')
print(f'A coisa mais barata que você comprou foi um(a): {barato} que custou: R${menor}')
    