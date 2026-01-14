"""
DESAFIO 044
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro/cheque: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
"""
print('{:=^40}'.format(' LOJA DA PROGRAMAÇÃO '))
valor = float(input('Digite o preço do produto: ').replace(',', '.'))
print('\033[0;31;40m'+ '='*30)
print("""Digite a Forma de pagamento:
[1] - À vista dinheiro/cheque, 
[2] - À vista no cartão, 
[3] - Em até 2x no cartão, 
[4] - 3x ou mais no cartão""")
print('='*30)
opcao = int(input('>> '))
print('\033[m')
if opcao <=4 and opcao >=1:
    if opcao == 1:
        nvalor = valor*10/100
        print(f'Você irá pagar o valor de R$ {valor-nvalor:.2f}. À vista dinheiro/cheque, o desconto foi de 10% = R${nvalor:.2f}')
    elif opcao == 2:
        nvalor = valor*5/100
        print(f'Você irá pagar o valor de R$ {valor-nvalor:.2f}. À vista no cartão, o desconto foi de R${nvalor:.2f}')
    elif opcao == 3:
        print(f'Você irá pagar o valor de R$ {valor:.2f}. Em até 2x no cartão, não há desconto.')
    elif opcao == 4:
        nvalor = valor*20/100
        print(f'Você irá pagar o valor de R$ {valor+nvalor:.2f}. Em 3x ou mais no cartão, o acréscimo será de R${nvalor:.2f}')
else:
    print('Opção Inválida!')
    
