#Leia 6 numeros inteiros e mostre a soma apenas dos que forem pares, desconsidere os impares
cont=0
soma=0

for c in range(0,6):
    n1=int(input('Digite um numero inteiro: '))
    if n1%2==0:
        soma=soma + n1
        cont=cont + 1
print(f'Numeros digitados {c+1}, {cont} pares, e a soma dos pares da {soma}')