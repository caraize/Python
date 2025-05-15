n=input('Digite algo: ')
print('Voce digitou {}' .format(n))

print('O que voce digitou é numerico ?' ,(n.isnumeric()))
print('O que voce digitou é alfabetico ?', (n.isalpha()))
print('O que voce digitou é alfanumerico ?' ,(n.isalnum()))
print('O que voce digitou é maiusculo ?' ,(n.isupper()))
print('O que voce digitou é minusculo ?' ,(n.islower()))

#print(n.isnumeric()) #se o que foi digitado é numerico
#print(n.isalpha()) #se o que foi digitado é alfabetico
#print(n.isalnum()) #se o que foi digitado é alfanumerico > alfabeto e numerico
#print(n.isupper()) #se o que foi digitado é maiusculo
#print(n.islower()) #se o que foi digitado é minusculo