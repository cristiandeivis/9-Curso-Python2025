"""Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla"""

from random import randint
numeros = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))
maior = numeros[0]
menor = numeros[0]
print (f'Os números sorteados foram: {numeros}', end=' ')
c = 0
for c in range (0,5,1):
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
print(f'O maior número é {maior} e o menor número é {menor}')