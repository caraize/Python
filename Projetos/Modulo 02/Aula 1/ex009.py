valor = float(input('Digite o valor da compra: '))
op = input('\nDigite a forma de pagamento \n[1] para dinheiro \n[2] para a vista no cartão \n[3] para 2x no cartão \n[4] para 3x ou mais no cartao\n')

if op == '1':
    print(f'Você escolheu dinheiro e ganhou 10% de desconto, de {valor} ficou por apenas {valor-valor*0.10}')
elif op == '2':
    print(f'Você escolheu a vista no cartao e ganhou 5% de desconto, de {valor} ficou por apenas {valor-valor*0.05}')
elif op == '3':
    print(f'Você escolheu em 2x no cartao e não ganhou desconto, então o valor se mantem em {valor}')
elif op == '4':
    parcela = int(input('Em quantas parcelas ? '))
    print(f'Você escolheu parcelar em {parcela}x, dessa forma teve um pequeno juros, então o valor final ficou em {valor+valor*0.20}')
else:
    print('Numero digitado invalido')
    