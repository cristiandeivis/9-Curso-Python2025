"""
DESAFIO 090

Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""
lista = {}
lista['Nome'] = input('Digite o nome: ').strip().lower().title()
lista['Média'] = float(input('Digite a média: '))
if lista['Média'] >= 7:
    print(f'O Aluno {lista['Nome']} está Aprovado! Com a média {lista['Média']} Parabéns')
    lista['Situação'] = 'Aprovado'
elif 5 <= lista['Média'] < 7:
    print(f'O Aluno {lista['Nome']} está em Recuperação! Com a média {lista['Média']}')
    lista['Situação'] = 'Recuperação'
if lista['Média'] < 5:
    print(f'Infelizmente o Aluno {lista['Nome']} está Reprovado com a média {lista['Média']}')
    lista['Situação'] = 'Reprovado'
for k,v in lista.items():
    print(f'{k}: {v}')