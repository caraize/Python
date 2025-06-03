#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado peça para digitar novamente ate ter um valor correto

sexo= ''

while sexo != 'M' and sexo != 'F':
    
    sexo=str(input('Digite seu sexo: ')).strip().upper()

    if sexo != 'M' and  sexo != 'F':
        print('Só aceitamos [M/F]')
    else:
        print('Tudo certo!!!')

print('encerrando...')