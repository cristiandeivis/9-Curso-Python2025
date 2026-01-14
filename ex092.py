"""DESAFIO 092

Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

from datetime import date
dados = {}
dados['Nome'] = input('Digite o nome: ').strip().lower().title()
nascimento = int(input('Digite o ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['Carteira'] = int(input('Digite a carteira de trabalho: (0 = Não tem) '))
if dados['Carteira'] != 0:
    dados['Ano Contratação'] = int(input('Digite o ano de contratação: '))
    dados['Salário'] = float(input('Digite o salário R$: '))
    dados['Aposentadoria'] = ((dados['Ano Contratação'] + 35) - nascimento)
for c,v in dados.items():
    print (f'- {c} tem o valor: {v}')