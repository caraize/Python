from datetime import date


ano_nasc=int(input('Qual seu ano de nascimento ?' ))
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade <=9:
    print('mirim')
elif idade <=14:
    print('infantil')
elif idade<=19:
    print('junior')
elif idade<=20:
    print('senior')
else:
    print('master')