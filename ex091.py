"""
DESAFIO 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
lista ={'Valor':0, 'Nome':'','Estado': False}
jogada = []
ordena = []
for c in range (0,4):
    lista['Valor'] = randint(1,6)
    lista['Nome'] = (f'Jogador {c+1}')
    sleep(1)
    print(f'O jogador {lista['Nome']} tirou o valor {lista['Valor']} no dado')
    jogada.append(lista.copy())
#Ordenar a lista
for c,v in enumerate(jogada):
    ordena.append(v['Valor'])
    ordena.sort(reverse=True)
#Avaliar e imprimir a ordem
for c, z in enumerate(ordena):
    for v in jogada:
        if v['Estado'] == False:
            if c == 0:
                if v['Valor'] == z:
                    sleep(1)
                    print(f'O {v['Nome']} tirou o valor {v['Valor']} e foi o campeão do dado')
                    v['Estado'] = True
            else:
                if v['Valor'] == z:
                    sleep(1)
                    print(f'O {v['Nome']} tirou o valor {v['Valor']}')
                    v['Estado'] = True