"""
Faça um programa que calcule a soma entre todos os números impares que são
múltiplos de três e que se encontram no intervalo de 1 até 500
"""
soma = 0
num = 0
for c in range (0,501,3):
    if c%2 != 0:
        soma +=c
        num +=1
print (f'A Soma dos {num} números é {soma}')