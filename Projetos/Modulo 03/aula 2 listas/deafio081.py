valores=[]
while True:
    num = int(input('Digite um valor: '))
    r=str(input('Deseja continuar?? ')).strip().upper()
    if r in 'Nn':
        break
    

   
print(f'\nForam digitados {len(valores)} numero(s)')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')

if 5 in valores:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 nao esta na lista')

