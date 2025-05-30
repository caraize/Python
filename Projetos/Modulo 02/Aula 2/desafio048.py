#faça um programa que calcule a soma de todos os numeros impares que são multiplos de 3 e que são encontrado no intervalo de 0 e 500

s = 0 #soma dos valores
x3 = 0 #numeros que são divisiveis por 3
tudo = 0 #contagem de numeros impares

for c in range(1,500,2): #for de 1-500 pulando de 2 em 2
    if  c%3 == 0: #se dividido por 3 o resto for igual 0
        s+=c #somando os valores que sao divisiveis por 3
        x3+=1 #quantos valores sao divisiveis por 3
    tudo+=1 #somando os valores impares
    
print(f'Entre 1 e 500 existem {tudo} numeros impares \nEntre eles {x3} é divisivel por 3 \nE a soma deles é {s}')