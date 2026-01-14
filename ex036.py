"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o empréstimo será negado.
"""

valor = float(input('Digite o Valor da Casa: '))
salario = float(input('Digite o seu Salário: '))
tempo = int(input('Digite em Quantos Anos Você Irá Pagar: '))
percentual = salario*30/100
prestacao = valor/(tempo*12)

if (prestacao >= percentual):
    print (f'\033[0;31;40mFinanciamento Negado! O valor da prestação é de R$ {prestacao:.2f} maior do que 30% do seu salário que é de = R$ {percentual:.2f}\033[m')
elif (prestacao <= percentual):
    print (f'\033[0;32;40mO valor a ser financiado é possível R$ {prestacao:.2f} pois é menor do que 30% do seu salário que é de = R$ {percentual:.2f}\033[m')