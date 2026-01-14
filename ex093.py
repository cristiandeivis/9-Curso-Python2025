"""
DESAFIO 093

Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois 
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols 
feitos durante o campeonato.
"""
dados = {}
dados['Nome'] = input('Digite o nome do jogador: ').strip().lower().title()
dados['Partidas'] = int(input(f'Quantas partidas {dados['Nome']} jogou? '))
jogos = []
for c in range(0,dados['Partidas']):
     jogos.append(int(input(f'Quantos gols o jogador {dados['Nome']} fez na partida {c+1}: ')))
soma = sum(jogos)
dados['Gols'] = jogos
dados['Total'] = soma
print('=-'*30)
print (dados)
print('=-'*30)
for k, v in dados.items():
     print (f'O campo {k} tem valor {v}')
print('=-'*30)
print (f'O jogador {dados['Nome']} jogou {dados['Partidas']} partidas')
for c, v in enumerate(jogos):
     print(f'No jogo {c+1} o jogador {dados['Nome']} fez {v} gols')
print (f'Foi um total de {dados['Total']} gols')