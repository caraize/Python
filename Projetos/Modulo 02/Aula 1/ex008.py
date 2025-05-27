#calcular imc
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura(em metros): '))
imc = peso/(altura*altura)

if imc<18.5:
    print(f'Abaixo do peso \n{imc}')
elif imc >=18.5 and imc<25:
    print(f'Peso ideal \n{imc}')
elif imc <=30:
    print(f'Sobrepeso \n{imc}')
elif imc <=40:
    print(f'Obesidade \n{imc}')
else:
    print(f'Obesidade mórbida \n{imc}')