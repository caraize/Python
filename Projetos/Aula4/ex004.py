import math

opo=float(input('Digite o valor o cateto oposto: '))
adj=float(input('Digite o valor do cateto adjacente: '))

#vp=(opo**2) + (adj**2)
#raiz=math.sqrt(vp)

#print(raiz)

hipotenusa=math.hypot(opo,adj)
print(hipotenusa)