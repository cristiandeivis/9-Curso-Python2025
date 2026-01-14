"""DESAFIO 081
Crie um programa que vai ler vários números e colocar em uma lista.

Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []
c = 0
while True:
    lista.append(int(input('Digite um número: ')))
    opt = input(str('Deseja Continuar S/N: '))
    if opt in 'Nn':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} elementos')    
print(lista)
if 5 in (lista):
    for pos, num in enumerate(lista):
        if num == 5:
            print(f'O número {num} está na lista na posição {pos}')
else:
    print('O número 5 não foi digitado.')