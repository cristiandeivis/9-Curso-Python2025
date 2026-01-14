"""Exercício 68
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
Versão Guanabara com eu tentando fazer...
"""
from random import randint
ganhou = 0
while True:
    num = int(input('Digite um número: '))
    comp = randint(0,10)
    soma = num + comp
    opc = ' '
    while opc not in 'PI':
        opc = input('Par ou Impar? [P/I]').strip().upper()[0]
    print (f'Você jogou {num} e o computador jogou {comp} e o total deu {soma}')
    print ('Deu Par!' if soma % 2 == 0 else 'Deu Impar!')
    if soma % 2 == 0:
        if opc == 'P':
            print('Você Ganhou')
            ganhou += 1
        else:
            break
    if soma % 2 != 0:
        if opc == 'I':
            print('Você Ganhou!')
            ganhou += 1
        else:
            break
print (f'Você perdeu, você ganhou {ganhou} vez(es)!')