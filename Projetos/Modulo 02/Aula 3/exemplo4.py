n = 1
par=0
impar=0
cont=0
while n !=0:
    n = int(input('Digite um valor: (0 para encerrar) '))
    
    if n!=0:
        cont=cont+1
        if n %2==0:
            par= par + 1
        if n%2!=0:
            impar= impar+1
        
print(f'Acabou...\nVocê digitou {cont} numeros\nCom {par} numeros pares e {impar} numeros impares')