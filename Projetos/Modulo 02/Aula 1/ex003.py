n1=float(input('Digite um numero: '))
n2=float(input('Digite outro numero: '))

if n1>n2:
    print(f'o numero {n1} é maior que {n2}')
elif n2>n1:
    print(f'o numero {n2} é maior que o {n1}')
else:
    print(f'Não existe valor maior ou menor, {n1} e {n2} sao iguais')