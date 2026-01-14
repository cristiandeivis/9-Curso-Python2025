"""Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição na tabela está o time da Chapecoense"""

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Vasco da Gama', 'Red Bull Bragantino','Corinthians', 'Atlético-MG', 'Ceará', 'Vitória', 'Santos', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')
print(f'Os 5 primeiros times são', times[0:5])
print(f'Os últimos 4 colocados são', times[-4:])
print ('Os times em ordem alfabética são:', sorted(times))
print(f'Corinthians está {times.index('Corinthians')+1}ª na posição')