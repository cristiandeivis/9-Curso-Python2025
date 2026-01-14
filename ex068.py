"""Exercício 68
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
Meu programa.
"""
from random import randint
ganhou = 0
num = 0 
while True:
    soma = 0
    num = int(input('Digite um valor: '))
    opc = str(input('Par ou Impar (P/I)? ')).strip().upper()[0]
    pc = randint(0,10)
    soma = pc + num
    if opc in 'Pp' and (soma % 2 == 0):
        ganhou += 1
        print(f'Jogador jogou {num} e o computador jogou {pc} a soma é {soma} par, jogador ganha!')
    elif opc in 'Pp' and (soma % 2 != 0):
        print(f'A soma é {soma} e é ímpar, jogador perdeu')
        break
    if opc in 'Ii' and (soma % 2 != 0):
        print(f'Jogador jogou {num} e o computador jogou {pc} a soma é {soma} ímpar, jogador ganha!')
        ganhou += 1
    if opc in 'Ii' and (soma % 2 == 0):
        print(f'Jogador jogou {num} e o computador jogou {pc} a soma é {soma} ímpar, jogador ganha!')
        ganhou += 1
        print(f'A soma é {soma} e é par, jogador perdeu')
        break
print (f'O jogador ganhou {ganhou} vezes.')