n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('É possivel formar um triangulo')
    if n1==n2 and n2==n3:
        print('Triangulo equilatero')
    elif n1 != n2 != n3 != n1:
         print('Triangulo escaleno')
    else:
        print('Triangulo isósceles')


else:
    print('Não é possivel formar um triangulo')