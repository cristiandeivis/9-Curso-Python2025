"""Exercício 71:
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
cinq = 0
vint = 0
dez = 0
um = 0
valor = int(input('Digite o valor a ser sacado: '))
if valor >= 50:
    while (valor/50) >= 1:
        cinq += 1
        valor -= 50
if valor >= 20:
    while (valor/20) >= 1:
        vint += 1
        valor -= 20
if valor >= 10:
    while (valor/10) >= 1:
        dez += 1
        valor -= 10
if valor >= 1:
    while (valor/1) >= 1:
        um += 1
        valor -= 1
if cinq > 0:
    print(f'Total de {cinq} cédulas de R$50,00')
if vint > 0:
    print(f'Total de {vint} cédulas de R$20,00')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10,00')
if um > 0:
    print(f'Total de {um} cédulas de R$1,00')