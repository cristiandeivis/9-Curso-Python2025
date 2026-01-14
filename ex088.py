""""Desafio 088

Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
jogos = int(input('Digite a quantidade de jogos: '))
print('-='*20)
print()
print(f'Sorteando {jogos} jogos: ')
print()
lista = []
numeros = []
num = 0
for d in range (0,jogos):
    c = 0
    while c < 6:
        num = randint(1,61)
        if num not in lista:
            lista.append(num)
            c += 1
    lista.sort()
    numeros.append(lista[:])
    lista.clear()
for c, v in enumerate(numeros):
    print(f'{c+1}º Jogo: {v}')
    sleep(1)
print('-='*20)