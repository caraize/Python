valor_digitado = (int(input('Digite um valor: '))), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))
aleatorio = valor_digitado


print(f'Foi digitado o valor 9 -> {aleatorio.count(9)}x')

if 3 in valor_digitado:
    print(f'O valor 3 apareceu na {aleatorio.index(3)+1}° posição')
else:
    print('O valor 3 não foi digitado')


print('Os pares são: ')

for n in valor_digitado:
    if n % 2 ==0:
        print(f'{n}', end=' ')

