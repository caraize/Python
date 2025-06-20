valores=[]

while True:
    num = int(input('Digite um valor: '))

    if num in valores:
        print('Valor duplicado, impossivel adicionar')

    else:
        valores.append(num)

    while True:
        r=str(input('Deseja continuar?? ')).strip().upper()

        if r == 'S' or r == 'N':
            break
        print('Só aceitamos [S/N]. Tente novamente.')
        
    if r == 'N':
        break
            

valores.sort()
print(f'Final{valores}')