valor = int(input('Qual valor deseja sacar: R$'))

total=valor
ced=50 # começa pela maior cédula
cont=0  # contador de cédulas daquela denominação

while True:
    if total>=ced:
        total=total-ced
        cont=cont+1
    else:
        if cont>0:
            print(f'Total de {cont} cedulas de {ced}')

        if ced ==50:
            ced=20

        elif ced ==20:
            ced=10

        elif ced==10:
            ced=1
        cont=0
        if total==0:
            break
            
            