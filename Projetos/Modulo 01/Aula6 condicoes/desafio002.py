print('-=-'*20) #só ajeitando
vc = float(input('Qual a velocidade do seu carro ? '))

if vc>80:
    print('Você infelizmente foi multado')
    multa = (vc-80) *7
    print(f'\nCada km/h a mais que ultrapassou, equivale a R$:7.00 \nComo você passou a {vc}km/h e você pagará R$:{multa}')
else:
    print('\nVoce esta livre, siga no limite da via')
print('-=-'*20) #só ajeitando
