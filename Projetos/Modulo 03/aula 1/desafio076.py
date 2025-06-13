produtos = ('Pao', 1.50, 'Leite', 3.50, 'Frango', 10.90, 'Whey', 129.90, 'Açai', 53.90)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<30} R${produtos[i+1]:>6.2f}')

print('-'*40) 
