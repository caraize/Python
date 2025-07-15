''' Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [[],[],[]]

for l in range(3):#adiciona uma linha
    for c in range (3): #adiciona uma coluna
        num = (int(input(f'Digite o valor para [{l}, {c}]: '))) #pegamos dados
        matriz[l].append(num) #appendamos o num no matriz l 

for l in matriz: #aqui ele pega a linha da matriz como [1 2 3]
    for valor in l: #aqui distrincha a linha e ele pega cada valor dela
        print(f'[ {valor} ] ' , end='')
    print()

    
