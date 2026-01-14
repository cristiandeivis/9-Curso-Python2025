"""Desafio 086

Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta."""

lista = [[0,0,0],[0,0,0],[0,0,0]]
for c in range (0,3):
    for d in range (0,3):
        lista[c][d] = input (f'Digite um valor para [{c}, {d}]: ')
for c in range (0,3):
    for d in range (0,3):
        print(f'[{lista[c][d]:^5}]', end = ' ')
    print()