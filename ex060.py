"""Exercício 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial, fazer em While e depois em FOR

Ex:
5! = 5 × 4 × 3 × 2 × 1 = 120”
"""

num = int(input('Digite um número: '))
c = num
tot = 1
print (f'Calculando {num}! = ', end = '')
while c > 0:
    print (c, end = '')
    if c > 1:
        print (f' X ', end = '')
        tot = tot*c
    c -= 1
print (f' O fatorial de {num}! = {tot}') 