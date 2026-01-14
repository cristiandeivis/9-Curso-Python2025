"""Desafio 086

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta."""

lista = [[],[],[]]
for c in range (0,3):
    lista[c].append(int(input(f'Digite um valor para [{c}, {0}]: ')))
    lista[c].append(int(input(f'Digite um valor para [{c}, {1}]: ')))
    lista[c].append(int(input(f'Digite um valor para [{c}, {2}]: ')))
print ('-='*20)
for c in lista:
    print (f'[{c[0]:^5}] [{c[1]:^5}] [{c[2]:^5}]')