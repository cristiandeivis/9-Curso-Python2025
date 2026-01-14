"""Exercício 70:
Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.

B) Quantos produtos custam mais de R$1000.

C) Qual é o nome do produto mais barato.
"""
total = mais_mil = maior = menor = cont = 0
desc_maior = desc_menor = ''
while True:
    cont += 1
    produto = input('Digite o nome do produto: ').capitalize().strip()
    valor = float(input('Digite o preço do produto: '))
    total += valor
    if cont == 1 or valor < menor:
        desc_menor = produto
        menor = valor
    if valor > 1000:
        mais_mil += 1
    if valor > maior:
        desc_maior = produto
        maior = valor
    opt = ' '
    while opt not in 'SN':
        opt = input('Deseja Continuar [S/N]: ').upper().strip()[0]
    if opt == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Há {mais_mil} produtos custando mais de R$1.000,00')
print(f'O produto mais caro foi {desc_maior} que custou R${maior:.2f}')
print(f'O produto mais barato foi {desc_menor} que custou R${menor:.2f}')
    