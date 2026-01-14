"""Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9
B) Em que posição foi digitado o primeiro valor 3
C) Quais foram os números pares
"""
num = (int(input('Digite um número: ')), int(input('Digite um número: ')),int(input('Digite um número: ')),int(input('Digite um número: ')))
print (f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print (f'O número 3 está na posição {num.index(3)}')
for n in num:
    if n % 2 == 0 and n > 0:
        print(f'O número {n} é par')