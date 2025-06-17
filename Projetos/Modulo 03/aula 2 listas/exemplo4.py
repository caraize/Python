a = [2, 3, 4, 7]
b=a[:] #isso cria uma copia da lista A, se deixar somente o igual ele faz uma ligação e muda a lista A também
b[2] = 8


print(f'Lista A: {a}')
print(f'Lista B: {b}')