#Escreva um programaque pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
#Para inferiores ou iguais o aumento é de 15%

salario = float(input('Digite o seu salário: '))
if salario <= 1250:
    print (f'O salário ajustado é {salario + (salario * 15/100):.2f}')
else:
    print(f'O salário ajustado é {salario + (salario * 10/100):.2f}')