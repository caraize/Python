from random import randint #importo biblioteca
from time import sleep

computador = randint(0, 5) #executo a biblioteca
print('-=-'*20) #só ajeitando
print('Vou pensar em um numero de 0 - 5 e você vai tentar adivinhar, ok ?')

user= int(input('\nDigite um numero entre 0 e 5: ')) #'user' vira variavel e ele digita um numero

print('\nprocessando...') 
sleep(1) #usando a biblioteca importada sleep para demorar X segundos, como se fosse um delay

if user == computador: #condicional
    print('Parabens acertou vilão')
else:
    print(f'\nErrou, eu pensei no {computador} e você chutou {user}')
print('-=-'*20)#só ajeitando