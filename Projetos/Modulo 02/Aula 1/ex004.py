from datetime import date

nome= input('Qual seu nome? ')
ano_nasc=int(input('Qual seu ano de nascimento ?' ))
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade <=17:
    print(f'Ainda precisa se alistar, {nome}, pois você ainda tem {idade} anos')
elif idade == 18:
    print(f'Esta na hora de se alistar, {nome}, pois você ainda ja {idade} anos')
else:
    print(f'Ja passou da hora de se alistar, {nome}, pois você ainda ja {idade} anos')