num = [2,5,9,1]
num[2] = 3
num.append(7) #adicionar o numero com append
num.sort() #ordenar a lista
num.sort(reverse=True) #ordenando mas descrescente
num.insert(2,2) #ele insere na posição 2 o numero 0|| primeiro posicao dps valor
num.pop()#remove o ultimo numero
num.pop(1)#remove o numero na posicao que selecionamos
if 7 in num:
    num.remove(7)#remove o numero digitado, mas so o primeiro
else:
    print('Nao achei o numero 4')

print(num)
print(f'Essa lista tem {len(num)} elementos') #usando len que faz a contagem