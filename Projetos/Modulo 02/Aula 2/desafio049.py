#Faça a tabuada usando FOR de um numero que o usuario digitar
n=int(input('Digite um numero que gostaria de saber a tuabada: '))

for c in range(0,11):
    print(f'{c} X {n} = {c*n}')

