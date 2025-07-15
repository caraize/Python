'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = mai = somacoluna = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]:'))
        
print('-=-' *30)
for l in range (3):
    for c in range (3):
        print(f'[ {matriz[l][c]:^5} ]' ,end='')
        if matriz[l][c] % 2 ==0:
            somapar = somapar +matriz[l][c]
    print()

print('-=-' *30)
print(f'Soma dos pares é: {somapar}')

for l in range(3):
    somacoluna = somacoluna + matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {somacoluna}')

for c in range(3):
    if c == 0 or matriz[1][c] > mai:
        mai=matriz[1][c]
print(f'O maior valor da segunda linha é: {mai}')
        