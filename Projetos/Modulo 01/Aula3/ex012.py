a=float(input('Digite o tamanho da altura a parede:'))
l=float(input('Digite o tamanho da largura da parede'))

area=l*a
tinta=area/2

print(f'A parede mede {a}x{l} tem uma area de {area:.2f}m² e precisa de {tinta:.2f} litros de tinta para pintar tudo')