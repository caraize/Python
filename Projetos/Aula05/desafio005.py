#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite sua frase aqui: ')).upper().strip()

contador =frase.count('A') #Contador de A
posicao =frase.find('A')+1 #Identifica o lugar que o primeiro A foi digitado  || +1 pq o programa começa a partir do 0 
posidireita =frase.rfind('A')+1 #Identifica o ultimo lugar que o A foi digitado  || +1 pq o programa começa a partir do 0 

print(f'A letra "a" aparece {contador}x na frase {frase}. A primeira vez que ela apareceu foi na posição {posicao} e a ultima na posição {posidireita}')