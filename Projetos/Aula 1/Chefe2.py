dia= input ('Qual o dia que você nasceu ? ')
mes= input ('Qual o mes que você nasceu ? ')
ano= int(input ('Qual o ano que voce nasceu? ')) #converte para inteiro
idade= 2025 - ano
print('Olá, então voce nasceu no dia' , dia, 'do mes',mes, 'e do ano de' , ano , '?', 
      '\ne tem', idade , 'anos se ja fez aniversario esse ano' , 
      '\nse não, ainda tem ' , idade-1 )