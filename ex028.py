#Escreva um programa que faça o computador pensar em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descrobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random
numero = int(input('Digite um número entre 0 e 5: '))
if (numero <0 or numero > 5):
    print('Número Inválido!')
else:
    lista = [0, 1, 2, 3, 4, 5]
    resultado = random.choice(lista)
    print(f'o Número escolhido foi: {resultado}')
    if (numero == resultado):
        print ('Você Venceu!')
    else:
        print ('Você Perdeu!')