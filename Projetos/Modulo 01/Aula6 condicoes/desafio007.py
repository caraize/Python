print('-=-'*20) #só ajeitando

salario = float(input('Qual seu salario? '))

if salario > 1250:
    aumento= (salario * 0.10) + salario
else:
    aumento= (salario * 0.15) + salario

print(f'Seu salario antigo era de R$: {salario}. E  o atualizado é de R$: {aumento}')