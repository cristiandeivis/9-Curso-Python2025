#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print("""Escolha a opção:
                  [0] Pedra
                  [1] Papel
                  [2] Tesoura""")
jogador = int(input('>> '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print(f'O Jogador Escolheu {itens[jogador]}')
print(f'O computador Escolheu {itens[computador]}')
if computador == 0:
    if jogador == 0:
        print ('Houve um Empate')
    elif jogador == 1:
         print ('Papel Embrulha Pedra JOGADOR venceu')
    elif jogador == 2:
        print ('Pedra quebra Tesoura COMPUTADOR venceu')
    else:
        print('Opção Inválida!')
elif computador == 1:
    if jogador == 0:
        print ('Papel Embrulha Pedra COMPUTADOR venceu')
    elif jogador == 1:
        print ('Houve um Empate')
    elif jogador == 2:
        print ('Tesoura Corta Papel JOGADOR venceu')
    else:
        print('Opção Inválida!')    
elif computador == 2:
    if jogador == 0:
        print ('Pedra quebra Tesoura JOGADOR venceu')
    elif jogador == 1:
        print ('Tesoura Corta Papel COMPUTADOR venceu')
    elif jogador == 2:
        print ('Houve um Empate')
    else:
        print('Opção Inválida!')
