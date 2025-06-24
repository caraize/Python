#Crie um programa onde o usuario vai digitar cinco valores numericos e cadastre-os em uma lista, ja na posição correta de inserção(sem usar o .sort(), no final mostre a lista ordenada)

valores=[]

for c in range(0,5): 
    num = int(input(f'Digite um valor: '))
    
    if c == 0 or num > valores[-1]: #se ele é o primeiro ou se ele é maior que o ultimo > maior do que estiver no final(ultimo de posição)
        valores.append(num)
        print('Adicionado ao final da lista')


    else:
        pos = 0
        while pos < len(valores): #le vai de 0 ate a ultima posição
            if num <= valores[pos]: #se o num é menor ou igual a lista na posição pos ou seja vai verificar em cada posição se o numero a ser inserido é menor ou igual a ele, se for menor, vai inserir
                valores.insert(pos, num) #na posição pos
                print(f'Adicionado a posição {pos} da lista')
                break
            pos=pos+1
print('-=-'*30)
print(f'Os valores digitados foram {valores}')