#Crie um programa que leia um número real qualquer pelo teclado
#e mostre na tela sua porção inteira

from math import trunc
num = float(input('Digite um número fracionado: '))
print(f'A parte inteira de {num} é {trunc(num)}')
