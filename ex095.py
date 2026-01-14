"""
DESAFIO 095

Aprimore o DESAFIO 93 para que ele
funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do
aproveitamento de cada jogador.
"""
dados = {}
gols = []
lista = []
while True:
    gols.clear()
    dados['Nome'] = input('Digite o nome do jogador: ').strip().lower().title()
    partidas = int(input('Quantas partidas ele jogou: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols ele fez na {c+1}ª partida: ')))
    dados['Partidas'] = partidas
    dados['Gols'] = gols.copy()
    dados['Total'] = sum(gols)
    lista.append(dados.copy())
    while True:
        opt = input('Deseja continuar? [S/N] ').upper()[0]
        if opt not in 'SN':
            print('Opção inválida digite S ou N ')
        else:
            break
    if opt == 'N':
        break
print('=-'*30)
print(lista)    
print('=-'*30)
print('Cod', end = '')
for i in dados.keys():
    print (f'{i:<15}', end = '')
print()
print('=-'*30)
for c,v in enumerate(lista):
    print(f'{c:>3}', end = '')
    for d in v.values():
        print(f'{str(d):<16}', end = '')
    print()
print('=-'*30)
while True:
    busca = int(input('Mostrar os dados de qual jogador? '))
    if busca >= len(lista):
        print('Código Inválido!')
    else:
        print (f'O jogador {lista[busca]['Nome']} jogou {lista[busca]['Partidas']} partidas')
        for cont,itens in enumerate(lista[busca]['Gols']):
            print (f'- Na partida {cont+1} o jogador {lista[busca]['Nome']} fez {itens} gols')
        while True:
            opt = input('Deseja continuar? [S/N] ').upper()[0]
            if opt not in 'SN':
                print('Opção inválida digite S ou N ')
            else:
                break
        if opt == 'N':       
            break
        