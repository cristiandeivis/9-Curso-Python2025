"""Exercício 71:
Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai 
informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
Versão Guanabara
"""
valor = int(input('Digite o valor que deseja sacar: '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Volte Sempre ao banco virtual')