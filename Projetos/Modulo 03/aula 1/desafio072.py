numeros=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    user= int(input('Digite um numero entre 0-20: '))
    if user >=0 and user<=20:
        break
    print('Tente novamente')

print(f'Você digitou o numero: {numeros[user]}')

while True:
    continuar= (input('Deseja continuar? ')).strip().upper()
    if continuar =='S':
        user= int(input('Digite um numero entre 0-20: '))
        print(f'Você digitou o numero: {numeros[user]}')
    else:
        print('Encerrando')
        break


