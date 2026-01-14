"""Exercício 61:
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão 
usando a estrutura while.
"""
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
c = 0
while c < 10:
    print (termo, end = ' ')
    c += 1
    termo = termo+razao
