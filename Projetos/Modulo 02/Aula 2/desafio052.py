#usuario vai digitar um numero, temos que verificar se ele é ou nao primo

num= int(input('Digite um numero: '))
total_divisoes=0

for c in range (1,num+1):
    if num % c ==0:
        total_divisoes= total_divisoes+1
if total_divisoes == 2:
        print(f'{num} é numero primo')
else:
        print(f'{num} não é primo')