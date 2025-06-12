brasileirao=('Corinthians', 'Palmeiras', 'São Paulo', 'Flamengo', 'Santos', 'Grêmio', 'Internacional', 'Atlético-MG', 'Cruzeiro', 'Vasco', 'Botafogo', 'Fluminense', 'Athletico-PR', 'Bahia', 'Fortaleza', 'Ceará', 'Goiás', 'Chapecoense', 'América-MG', 'Red Bull Bragantino')



print('-'*30)
print(f'Os que vão para Libertadores são: {brasileirao[0:5]}') #5 primeiros
print('-'*30)

print(f'Os rebaixados são: {brasileirao[-4:]}') #4 ultimos
print('-'*30)
print(f'Os times em ordem alfabetica ficam assim: {sorted(brasileirao)}') #ordem alfabetica
print('-'*30)
print(f'O flamengo terminou na {brasileirao.index("Flamengo")+1}° colocação') #qual posição esta o Flamengo