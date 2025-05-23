print('-=-'*20) #só ajeitando

distancia = float(input('Digite em KM, qual a distancia da viagem: '))

if distancia <= 200:
    valor= distancia*0.50
    print(f'O valor que pagará sera: {valor}')
else:
    valor2 = distancia*0.45
    print(f'O valor que pagará sera: {valor2}')
print('Boa viagem')