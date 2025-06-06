soma=0
cont=0
while True:
    n=int(input('Digite um numero (999 para parar): '))
    if n ==999:
        break
    cont=cont+1
    soma=soma+n
    
print(f'Você digitou {cont} numeros, \nA soma entre eles deu {soma}')