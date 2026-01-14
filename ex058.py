"""Exercício 58:
Melhore o jogo do DESAFIO 028 onde o computador vai ‘pensar’ em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

Exercício 28:
#Escreva um programa que faça o computador pensar em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descrobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu
"""
from time import sleep
from random import randint
computador = randint(0,10)
print('Sou seu computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
cont = 0
acertou = False
while not acertou:
    palpite  = int(input('Digite seu palpite: '))
    if computador == palpite:
        acertou = True
    if palpite < computador:
        print('O número que eu pensei é maior, tente outra vez')
    else:
        print('O número que eu pensei é menor, tente outra vez')
    cont += 1
print(f'Exato! O número que eu pensei é {palpite}! E você acertou após {cont} tentativas')