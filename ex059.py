"""Exercício 59:
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

opc = 0
while opc != 5:
    opc = 0
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    while opc != 5:
        opc = int(input("""Digite as opções:
                        [1] somar
                        [2] multiplicar
                        [3] maior
                        [4] novos números
                        [5] sair do programa
                        """))
        if opc == 1:
            print(f'A soma entre {num1} + {num2} é {num1+num2}')
        elif opc == 2:
            mult = num1*num2
            print (f'A multiplicação entre {num1} * {num2} é {num1*num2}')
        elif opc == 3:
            if num1 > num2:
                print(f'O número {num1} é maior que {num2}')
            elif num1 < num2:
                print(f'O número {num2} é maior que {num1}')
            else:
                print(f'Os números são iguais. {num2} = {num1}')
        elif opc == 4:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
        elif opc == 5:
            print('Encerrando o programa.')
        else:
            print('Opção inválida, tente novamente.')
