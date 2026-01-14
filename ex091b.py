"""
DESAFIO 091

Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'Jogador A' : randint(1,6),
           'Jogador B' : randint(1,6),
           'Jogador C' : randint(1,6),
           'Jogador D' : randint(1,6)}

for k,v in sorteio.items():
    print(f'O jogador {k} tirou o valor {v}')
    sleep(0.5)
ordenado = sorted(sorteio.items(),key=itemgetter(1), reverse = True)
print('=-'*30)
for c,v in enumerate(ordenado):
    if c == 0:
        print(f'Jogador {v[0]} ficou em {c+1}º lugar e foi o campeão com o número {v[1]} Parabéns!')
    else:
        print(f'{v[0]} ficou em {c+1}º lugar {v[1]}.')
    sleep(0.5)

