contador_idade=0
contador_homens=0
mulheres_menores=0
while True:
    idade= int(input('Digite sua idade: '))

    sexo=' '
    while sexo not in 'MF': #enquanto sexo nao for FM, ele nao avança
        sexo= str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    print('-'*20)
    continar=' '
    while continuar not in 'SN': #enquanto continuar nao for SN, ele nao avança
        continuar= str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
    print('-'*20)

    if idade >=18:
        contador_idade= contador_idade+1
    if sexo == 'M':
        contador_homens= contador_homens+1
    if sexo =='F' and idade <20:
        mulheres_menores=mulheres_menores+1
    if continuar =='N':
        break
print(f'Total de pessoas com mais de 18 anos: {contador_idade}')
print(f'Ao todo temos {contador_homens} homens cadastrados')
print(f'E temos {mulheres_menores} mulher(es) com menos de 20 anos')