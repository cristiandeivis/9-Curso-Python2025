#DESAFIO 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
atual = date.today().year
idade = (atual-ano)
if idade == 18:
    print(f'Seu ano de alistamento é {atual}')
    print(f'Você está com {idade} já está na hora de se alistar meu amigão!')
elif idade < 18:
    tempo = (18-idade)
    ano = atual + tempo
    print(f'Seu ano de alistamento será {ano} ')
    print(f'Você está com {idade} anos e faltam {tempo} anos para você se alistar')
else:
    tempo = (idade-18)
    ano = atual - tempo
    print(f'Seu ano de alistamento foi em {ano} ')
    print(f'Você está com {idade} anos e já passou {tempo} anos do seu alistamento.')
