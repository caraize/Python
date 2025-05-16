import math
ang=int(input('Digite o valor o angulo: '))

rad=math.radians(ang)

seno=math.sin(rad)
cosseno=math.cos(rad)
tangente=math.tan(rad)

print(f'O angulo digitado foi: {ang} \nele em radianos fica: {rad:.2f} \no seno: {seno:.2f} \ncosseno: {cosseno:.2f} \ntangente: {tangente:.2f}')