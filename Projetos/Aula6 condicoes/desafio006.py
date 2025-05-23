print('-=-'*20) #só ajeitando
n1= float(input('Digite um numero: '))
n2= float(input('Digite outro numero: '))
n3= float(input('Digite e outro numero: '))


#Achando o maior
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#Achando o menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O maior digitado foi: {maior} e o menor foi: {menor}')

