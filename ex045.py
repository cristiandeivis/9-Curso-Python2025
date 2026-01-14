#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
jogador = input("""Escolha a opção:
                  [1] Pedra
                  [2] Papel
                  [3] Tesoura
                  >>  """)

if jogador == '1' or jogador == '2' or jogador =='3':
    computador = str(randint(1,3))
    if jogador == '1':
        opcao = jogador.replace('1','Pedra')
    if jogador == '2':
        opcao = jogador.replace('2', 'Papel')
    if jogador == '3':
        opcao = jogador.replace('3', 'Tesoura')
    if computador == '1':
        opcao2 = computador.replace('1','Pedra')
    if computador == '2':
        opcao2 = computador.replace('2', 'Papel')
    if computador == '3':
        opcao2 = computador.replace('3', 'Tesoura')        
    print(f'O jogador apostou em {opcao} e o computador apostou em {opcao2}')
    if jogador == computador:
        print('Houve um Empate')
    elif opcao == 'Pedra' and opcao2 == 'Tesoura':
        print('Pedra quebra tesoura, Jogador venceu!')
    elif opcao == 'Pedra' and opcao2 == 'Papel':
        print('Papel embrulha pedra, Computador venceu!')
    elif opcao == 'Papel' and opcao2 == 'Pedra':
        print('Papel embrulha pedra, Jogador venceu!')
    elif opcao == 'Papel' and opcao2 == 'Tesoura':
        print('Tesoura corta o papel, Computador venceu!')
    elif opcao == 'Tesoura' and opcao2 == 'Papel':
        print('Tesoura corta o papel, Jogador venceu!')
    elif opcao == 'Tesoura' and opcao2 == 'Pedra':
        print('Pedra quebra tesoura, Computador venceu!')
else:
    print ('Opção Inválida!')