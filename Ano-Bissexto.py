#Ano bissexto 


from datetime import date
ano = int(input('Digite um ano, ou coloque o ano atual digitando 0 (zero): '))

if ano == 0:
    ano = date.today().year. #Pega o ano do pc do usuário 
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O {} é BISSEXTO!'.format(ano))
else:
    print('O {} não é BISSEXTO'.format(ano))
