n = int(input('Digite um numero: '))
op = input('1 para Binario \n2 para octal \n3 para hexadecimal\n')

if op == '1':
    print(bin(n))
elif op == '2':
    print(oct(n))
elif op == '3':
    print(hex(n))
else:
    print('Numero digitado invalido')
    