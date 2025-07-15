''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
princ=[] #lista principal
temp=[] #lista temporaria
maior = menor = 0

while True:
    temp.append(str(input('Digite seu nome: ')))  #adicionando valores a lista temporaria
    temp.append(float(input('Digite seu peso: '))) #adicionando valores a lista temporaria
    
    if len(princ) == 0: #se for o primeiro valor da lista principal todos vao receber esse valor como maior e menor
        maior = menor = temp[1]
    else: #se nao vai atribuir
        if temp[1] > maior: 
            maior = temp[1]
        if temp[1] < menor: 
            menor = temp[1]

    princ.append(temp[:]) #principal copia a temporaria só no nome e peso atual
    temp.clear() #temporaria se deleta
    
    r=str(input('Deseja continuar?? ')).strip().upper()
    if r in 'Nn':
        break

print(f'\nAo todo, você digitou {len(princ)} pessoa(s)') #tamanho da principal
print(f'\nLista completa: {princ}') #pega tudo da principal


print(f'\nO maior peso é: {maior}\nE quem tem esse peso é/são: ', end='') #maior peso
for p in princ: #p vira separado a lista principal
    if p[1]>=maior: #p1 vira peso pois p0 é nome, entao se p1 é >= o maior
        print(f'[{p[0]}]' , end=' ') #aqui printa o p0 que é o nome


print(f'\nO menor peso é: {menor}\nE quem tem esse peso é/são: ', end='') #menor peso
for p in princ:
    if p[1] <= menor:
        print(f'[{p[0]}]' , end=' ')

   



