#Crie um programa onde o usuario digite uma expressao qualquer que use parenteses, seu aplicativo deverá analisar se a expressao passada esta com os parenteses abertos e fechados na ordem correta
expr = str(input('Digite a expressão: '))
pilha=[]
for simb in expr:
    if simb=='(':
        pilha.append('(')
    
    elif simb==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break


if len(pilha) == 0:
    print('Sua expressão esta válida !!')
else:
    print('Tem algo de errado ai...\nERRO')



