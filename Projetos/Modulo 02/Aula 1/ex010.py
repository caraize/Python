import random

itens= ('Pedra', 'Papel' , 'Tesoura')
jogador_maquina = random.randint(0, 2)

print('=====VAMOS JOGAR=====')
print('Escolha uma opção: \n[0] Pedra \n[1] Papel \n[2] Tesoura')
jogador_humano= int(input('Qual a sua jogada ? \n'))

print('-=' *12)
print(f'O computador escolheu {itens[jogador_maquina]}')
print(f'Você jogou {itens[jogador_humano]}')
print('-=' *12)

if jogador_maquina == 0: #comp jogou pedra
    if jogador_humano ==0:
        print('EMPATOU, os dois jogaram pedra')

    elif jogador_humano ==1:
        print('GANHOU, embrulhou a Pedra')

    elif jogador_humano ==2:
        print('PERDEU, jogou tesoura e o computador Pedra')
    else:
        print('Opção invalida')

if jogador_maquina == 1: #comp jogou papel
    if jogador_humano ==0:
        print('PERDEU, o computador te embrulhou')

    elif jogador_humano ==1:
        print('EMPATOU, os dois jogaram papel')

    elif jogador_humano ==2:
        print('GANHOU, picotou o papel dele')
    else:
        print('Opção invalida')


if jogador_maquina == 2: #comp jogou tesoura
     if jogador_humano ==0:
        print('GANHOU, destruiu a tesoura')

     elif jogador_humano ==1:
        print('PERDEU, ele te cortou')

     elif jogador_humano ==2:
        print('EMPATOU, duas tesouras')
     else:
        print('Opção invalida')

else:
    print('Numero digitado invalido')