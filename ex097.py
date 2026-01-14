"""
DESAFIO 097

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva("Olá Mundo!")

Saída:
------------
Olá Mundo!
------------
"""

def escreva (a):
    tama = len(a)+4
    
    print('~'*tama)
    print (f'  {a}')
    print('~'*tama)


escreva ('Cristian')
escreva ('Cristian Deivis Mecabô')
escreva ('CDM')
