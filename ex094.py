
"""
DESAFIO 094

Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final,
mostre:

A) Quantas pessoas foram cadastradas.
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com
idade acima da média.
"""
dados = {}
lista = []
soma = 0
while True:
    dados['Nome'] = input('Digite o nome: ').strip().lower().title()
    dados['Idade'] = int(input('Digite a idade: '))
    soma += dados['Idade']
    while True:
        sexo = input('Digite o sexo: [M/F]: ')
        if sexo not in 'MmFf':
            print(f'Valor {sexo} inválido digite apenas M ou F')
        else:
            dados['Sexo'] = sexo.upper()
            break
    lista.append(dados.copy())
    while True:
        opt = input('Deseja continuar? [S/N] ')
        if opt not in 'SsNn':
            print(f'Opção "{opt}" inválida digite S ou N')
        else:
            break
    if opt in 'Nn':
        break
print (f'A) Foram cadastradas {len(lista)} pessoas')
media = soma/len(lista)
print (f'B) A média é {media:.2f}')
print('C) Foram cadastradas as mulheres: ', end = '')
for e in lista:
    if e['Sexo'] in 'F':
        print(f'{e['Nome']}', end = ' ')
print()
print('D) As pessoas acima da média são: ')
for e in lista:
    if e['Idade'] >= media:
        for k,v in e.items():
            print (f'{k}: {v}; ', end = '')
        print()