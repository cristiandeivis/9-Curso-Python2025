"""Exercício 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial, fazer em While e depois em FOR

Ex:
5! = 5 × 4 × 3 × 2 × 1 = 120”
"""

num = int(input('Digite um número: '))
fat = num
for c in range (num-1,0,-1):
    print (f'O número {fat} * {c} é {fat*c}')
    fat = fat*c