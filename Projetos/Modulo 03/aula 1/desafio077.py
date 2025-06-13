lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batatas Fritas')

for comida in lanche:
    print(f'\nNa palavra {comida.upper()} temos as vogais:', end=' ')
    for vogais in comida:
        if vogais.lower() in 'aeiou':
            print(vogais , end=' ')