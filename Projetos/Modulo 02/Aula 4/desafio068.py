from random import randint

print('-=-'*10)
print('Vamos jogar PAR ou ÍMPAR')
print('-=-'*10)

while True:
    user=int(input('Diga um valor: '))
    escolha=str(input('Par ou Ímpar ? [P/I] ')).strip().upper()
    computador = randint(0, 100)

    if escolha == 'P':
        resu=user+computador
        if resu %2==0:
            print('\nVocê ganhou')
            print(f'O computador jogou: {computador} e você escolheu: {user}. Total deu: {resu}, PAR')
            print('Vamos jogar até você perder, ok ?')
        else:
            print('\nVocê perdeu :(')
            print(f'O computador jogou: {computador} e você escolheu: {user}. Total deu: {resu}, IMPAR')
            print('Agora vamos parar, hihihi')
            break
    if escolha == 'I':
        resu=user+computador
        if resu %2!=0:
            print('\nVocê ganhou')
            print(f'O computador jogou: {computador} e você escolheu: {user}. Total deu: {resu}, IMPAR')
            print('Vamos jogar até você perder, ok ?')
        else:
            print('\nVocê perdeu :(')
            print(f'O computador jogou: {computador} e você escolheu: {user}. Total deu: {resu}, PAR')
            print('Agora vamos parar, hihihi')
            break
