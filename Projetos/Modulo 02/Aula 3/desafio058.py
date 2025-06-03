#Aprimorando o jogo da aula 06 de condições, onde o computador vai pensar em um numero de 0-10 só que o jogador vai tentar adivinhar ate acertar, mostrando no final quantos palpites foram feitos

from random import randint #importo biblioteca
from time import sleep

computador = randint(0, 11) #executo a biblioteca
cont=0

print('Vou pensar em um numero de 0 - 10 e você vai tentar adivinhar, ok ?')

user= int(input('\nDigite um numero entre 0 e 10: ')) #'user' vira variavel e ele digita um numero
cont=cont+1
print('\nprocessando...') 
sleep(0.5)

while user != computador:
    
    if user != computador:
        cont=cont+1
        if user > computador:
            user= int(input('\nVocê errou, chute um numero menor, mas pode tentar novamente: '))
            print('\nprocessando...') 
            sleep(0.5)
        if user < computador:
            user= int(input('\nVocê errou, chute um numero maior, mas pode tentar novamente: '))
            print('\nprocessando...') 
            sleep(0.5)
if cont==0:
    print(f'ACERTOU DE PRIMEIRA \O/ \O/ \O/ \O/\nPARABENS, VOCÊ É GENIO\nEu pensei no {computador} e você chutou exatamente {user}')
elif cont <=3:
    print(f'\nVOCÊ ACERTOUUUUUUUUU\nEu pensei no {computador} e você chutou exatamente {user} \nE precisou apenas de {cont} tentativas')
elif cont <=7:
    print(f'\nVOCÊ ACERTOU\nEu pensei no {computador} e você chutou {user} \nMas precisou de {cont} tentativas')
else:
    print(f'Acertou, mas, ta ruim de palpite, meu deu em...\n\nEu pensei no {computador} e você chutou {user} \nMas tambem precisou de {cont} tentativas')
