"""Exercício 69:
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas têm mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres têm menos de 20 anos.
"""
cont_idade = 0
cont_homens = 0
cont_mulheres = 0
while True:
    print('-'*20)
    idade = int(input('Digite sua idade: '))
    sexo =' '
    while sexo not in 'MF':        
        sexo = input('Digite seu Sexo [M/F]: ').strip().upper()[0]
    if idade >= 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1
    opt = ' '
    while opt not in 'SN':
        opt = input('Quer continuar? [S/N]').strip().upper()[0]
    if opt == 'N':
        break
print(f'Pessoas com mais de 18: {cont_idade}')
print(f'Homens cadastrados: {cont_homens}')
print(f'Mulheres com menos de 20 anos: {cont_mulheres}')