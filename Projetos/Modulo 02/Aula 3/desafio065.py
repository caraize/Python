r='S'
media=0
maior=0
menor=0
cont=0
vd=0
while r == 'S':
    v=int(input('Digite um valor: '))
    vd=vd+v
    cont=cont+1

    media=vd/cont

    if cont == 1:
        maior = v
        menor = v
    if v > maior:
        maior=v
    if v < menor:
        menor=v


    r=str(input('Quer continuar ? ')).upper() #aqui tem que ser a mesma variavel pois se nao ele nao muda a variavel e o while nao para


print(f'Você digitou: {cont} numeros.\nA soma deles é: {vd}.\nA media é: {media}')
print(f'O maior é: {maior}\nE o menor é: {menor}')