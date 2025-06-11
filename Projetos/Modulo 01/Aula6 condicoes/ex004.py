n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1+n2) /2

if media >=6:
    print(f'Parabens pela media {media}, você esta aprovado')
else:
    print(f'Infelizmente sua media foi: {media}, e você nao passou de ano :(')

print('Bom final de ano!!!')