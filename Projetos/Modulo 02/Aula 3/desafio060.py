#Faça um programa que leia um numero e mostre seu fatorial

nu=int(input('Digite o numero que deseja saber o fatorial: '))
n=nu
f=1
while n > 0:
    print(f'{n}' ,end='')
    print(' x ' if n>1 else ' = ', end='')
    f=f*n
    n=n-1
print(f'{f}')