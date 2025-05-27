valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salario: R$'))
anos= int(input('Digite em quantos anos deseja pagar: '))

meses= anos*12
trinta= salario*0.30


print(f'\nVocê pode pagar somente {trinta} de prestação')
print(f'\nPara pagar uma casa de R$:{valor} em {anos} anos, a prestação será de {valor/meses:.2f}')


if (valor/meses) <= trinta:
    print(f'Você vai conseguir financiar a casa em {anos}, pois seu salario permite')
else:
    print('Emprestimo negado')
   
