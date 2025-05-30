pt=int(input('Digite o primeiro termo da PA: '))
rz=int(input('Digite a razão da PA: '))
dezprimeiros= pt+rz*10

for c in range(pt,dezprimeiros,rz):
    print(c)