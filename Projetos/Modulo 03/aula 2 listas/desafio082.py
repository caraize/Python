valores=[]
valorespares=[]
valoresimpares=[]

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)

    r=str(input('Deseja continuar?? ')).strip()

    if num % 2 == 0:
        valorespares.append(num)
    else: 
        valoresimpares.append(num)

    if r in 'Nn':
        break

   
print(f'\nLista completa: {valores}')
print(f'A lista de pares é: {valorespares}')
print(f'A lista de impares é: {valoresimpares}')