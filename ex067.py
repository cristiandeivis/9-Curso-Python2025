"""Exercício 67:
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    c = 0
    num = int(input('Deseja ver a tabuada de qual valor? '))
    if num < 0:
        break
    while c <= 10:
        print (f'{num} X {c} = {num*c}')
        c += 1
print('Programa encerrado!')