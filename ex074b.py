"""Crie um programa que vai gerar cinco números aleatórios e 
colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla"""

from random import randint
numeros = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ', end = '')
for n in numeros:           #esse "for" é para o sistema não mostrar os parênteses da tupla
    print(n, end =' ') 
print(f'\nO maior número é {max(numeros)} e o menor número é {min(numeros)}')