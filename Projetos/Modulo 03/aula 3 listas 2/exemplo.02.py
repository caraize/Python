galera = [['Joao',19], ['Ana', 33], ['Joaquim', 13] ,['Maria', 45]]#lista dentro de outra lista
print(galera[2][1]) #exibindo alguns dado espeicifico dentro da lista > primeiro a lista depois o dado da lista

print('-=-'*10)
for p in galera: #para cada p em galera
    print(f'A pessoa {p[0]}, tem {p[1]} anos de idade')